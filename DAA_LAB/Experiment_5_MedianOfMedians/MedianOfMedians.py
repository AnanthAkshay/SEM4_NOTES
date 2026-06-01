import time
import random
import sys

sys.setrecursionlimit(200000)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def partition(arr, left, right, pivot_val):
    # Find the pivot element and move it to the end
    for i in range(left, right + 1):
        if arr[i] == pivot_val:
            arr[i], arr[right] = arr[right], arr[i]
            break
            
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
    arr[i], arr[right] = arr[right], arr[i]
    return i

def kth_smallest(arr, left, right, k):
    if 0 < k <= right - left + 1:
        n = right - left + 1
        
        # Divide arr into groups of 5 and find medians
        medians = []
        i = 0
        while i < n // 5:
            group = arr[left + i*5 : left + i*5 + 5]
            medians.append(insertion_sort(group)[2])
            i += 1
            
        if i * 5 < n:
            group = arr[left + i*5 : left + n]
            medians.append(insertion_sort(group)[len(group)//2])
            
        # Find median of medians
        if len(medians) == 1:
            med_of_med = medians[0]
        else:
            med_of_med = kth_smallest(medians, 0, len(medians)-1, len(medians)//2 + 1)
            
        # Partition array around med_of_med
        pos = partition(arr, left, right, med_of_med)
        
        # If position is same as k
        if pos - left == k - 1:
            return arr[pos]
        if pos - left > k - 1:
            return kth_smallest(arr, left, pos - 1, k)
        return kth_smallest(arr, pos + 1, right, k - pos + left - 1)
        
    return -1

def performance_analysis():
    sizes = [1, 10, 100, 1000, 10000, 100000]
    
    print("\n--- Performance Analysis (Median of Medians) ---")
    print(f"{'N':<10} | {'Time Taken (seconds)':<20}")
    print("-" * 36)
    
    for n in sizes:
        arr = [random.randint(1, 10000) for _ in range(n)]
        k = n // 2 + 1
        
        start_time = time.time()
        kth_smallest(arr, 0, n - 1, k)
        end_time = time.time()
        
        time_taken = end_time - start_time
        print(f"{n:<10} | {time_taken:<20.6f}")
    print("-" * 36)

def main():
    while True:
        print("\n==================================")
        print(" HOSPITAL ANALYTICS (MEDIAN FIND) ")
        print("==================================")
        print("1. Find Median Waiting Time")
        print("2. Run Performance Analysis")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                arr = list(map(int, input("Enter patient waiting times separated by space: ").split()))
                if not arr:
                    print("Array is empty!")
                    continue
                    
                n = len(arr)
                print("\nWaiting Times:", arr)
                median = kth_smallest(arr, 0, n - 1, n // 2 + 1)
                print(f"Median Waiting Time: {median} minutes")
            except ValueError:
                print("Invalid input! Please enter integers.")
                
        elif choice == '2':
            performance_analysis()
            
        elif choice == '3':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
