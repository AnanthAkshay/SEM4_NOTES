import time
import random

def merge(arr, left, mid, right):
    """
    Merges two sub-arrays of arr[].
    First sub-array is arr[left..mid]
    Second sub-array is arr[mid+1..right]
    """
    n1 = mid - left + 1
    n2 = right - mid
 
    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2
 
    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
 
    # Merge the temp arrays back into arr[left..right]
    i = 0     # Initial index of first sub-array
    j = 0     # Initial index of second sub-array
    k = left  # Initial index of merged sub-array
 
    while i < n1 and j < n2:
        if L[i] <= R[j]: # Stable condition (<=)
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    """
    Main function that sorts arr[left..right] using merge()
    """
    if left < right:
        mid = left + (right - left) // 2
 
        # Sort first and second halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        
        # Merge the sorted halves
        merge(arr, left, mid, right)

def performance_analysis():
    sizes = [1, 10, 100, 1000, 10000, 100000]
    
    print("\n--- Performance Analysis ---")
    print(f"{'N':<10} | {'Time Taken (seconds)':<20}")
    print("-" * 36)
    
    for n in sizes:
        # Generate random array for testing
        arr = [random.randint(1, 1000000) for _ in range(n)]
        
        start_time = time.time()
        merge_sort(arr, 0, n - 1)
        end_time = time.time()
        
        time_taken = end_time - start_time
        print(f"{n:<10} | {time_taken:<20.6f}")
    print("-" * 36)

def main():
    while True:
        print("\n==================================")
        print("    ONLINE RETAIL ORDER SORTING   ")
        print("==================================")
        print("1. Sort Custom Array (Manual Input)")
        print("2. Run Performance Analysis")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                arr = list(map(int, input("Enter the order amounts separated by space: ").split()))
                if not arr:
                    print("Array is empty!")
                    continue
                    
                print("\nUnsorted Orders:", arr)
                merge_sort(arr, 0, len(arr) - 1)
                print("Sorted Orders:  ", arr)
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
