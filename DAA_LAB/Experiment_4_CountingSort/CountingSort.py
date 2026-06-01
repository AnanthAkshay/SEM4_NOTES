import time
import random

MAX_MARK = 100

def counting_sort(arr):
    n = len(arr)
    # The output array that will have sorted elements
    output = [0] * n
    
    # Create a count array to store count of individual characters and initialize count array as 0
    count = [0] * (MAX_MARK + 1)
    
    # Store count of each character
    for i in range(n):
        if 0 <= arr[i] <= MAX_MARK:
            count[arr[i]] += 1
        else:
            print(f"Error: Mark {arr[i]} out of bounds (0-100)")
            return arr
            
    # Change count[i] so that count[i] now contains actual position of this character in output array
    for i in range(1, MAX_MARK + 1):
        count[i] += count[i - 1]
        
    # Build the output array
    # To make it stable we are operating in reverse order.
    i = n - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
        
    # Copy the output array to arr
    for i in range(n):
        arr[i] = output[i]
        
    return arr

def performance_analysis():
    sizes = [1, 10, 100, 1000, 10000, 100000]
    
    print("\n--- Performance Analysis (Counting Sort) ---")
    print(f"{'N':<10} | {'Time Taken (seconds)':<20}")
    print("-" * 36)
    
    for n in sizes:
        arr = [random.randint(0, MAX_MARK) for _ in range(n)]
        
        start_time = time.time()
        counting_sort(arr)
        end_time = time.time()
        
        time_taken = end_time - start_time
        print(f"{n:<10} | {time_taken:<20.6f}")
    print("-" * 36)

def main():
    while True:
        print("\n==================================")
        print(" EXAM EVALUATION (COUNTING SORT)  ")
        print("==================================")
        print("1. Sort Custom Marks Array")
        print("2. Run Performance Analysis")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                arr = list(map(int, input("Enter student marks (0-100) separated by space: ").split()))
                if not arr:
                    print("Array is empty!")
                    continue
                    
                print("\nUnsorted Marks:", arr)
                counting_sort(arr)
                print("Sorted Marks:  ", arr)
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
