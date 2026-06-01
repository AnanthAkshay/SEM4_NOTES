import time
import random
import sys

# Increase recursion depth for testing arrays up to 100,000
sys.setrecursionlimit(200000)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_partition(arr, low, high):
    # Select a random pivot index
    random_idx = random.randint(low, high)
    # Swap the random pivot with the last element
    arr[random_idx], arr[high] = arr[high], arr[random_idx]
    
    return partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

def performance_analysis():
    sizes = [1, 10, 100, 1000, 10000, 100000]
    
    print("\n--- Performance Analysis ---")
    print(f"{'N':<10} | {'Time Taken (seconds)':<20}")
    print("-" * 36)
    
    for n in sizes:
        arr = [random.randint(1, 1000000) for _ in range(n)]
        
        start_time = time.time()
        randomized_quick_sort(arr, 0, n - 1)
        end_time = time.time()
        
        time_taken = end_time - start_time
        print(f"{n:<10} | {time_taken:<20.6f}")
    print("-" * 36)

def main():
    while True:
        print("\n=====================================")
        print("  COURIER PACKAGE SORTING (R-QUICK)  ")
        print("=====================================")
        print("1. Sort Custom Array (Manual Input)")
        print("2. Run Performance Analysis")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                arr = list(map(int, input("Enter package weights separated by space: ").split()))
                if not arr:
                    print("Array is empty!")
                    continue
                    
                print("\nUnsorted Packages:", arr)
                randomized_quick_sort(arr, 0, len(arr) - 1)
                print("Sorted Packages:  ", arr)
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
