import time
import random

def print_optimal_parens(s, i, j):
    if i == j:
        return f"A{i}"
    else:
        left = print_optimal_parens(s, i, s[i][j])
        right = print_optimal_parens(s, s[i][j] + 1, j)
        return f"({left}{right})"

def matrix_chain_order(p, n, verbose=False):
    # m[i][j] = Minimum number of scalar multiplications needed
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # L is chain length
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                # q = cost/scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    min_cost = m[1][n]

    if verbose:
        optimal_parens = print_optimal_parens(s, 1, n)
        print(f"\nOptimal Parenthesization: {optimal_parens}")
        print(f"Minimum scalar multiplications: {min_cost}")

    return min_cost

def performance_analysis():
    # N is limited because O(N^3) in Python becomes extremely slow past N=500
    sizes = [10, 25, 50, 100, 200, 400]
    
    print("\n--- Performance Analysis (Matrix Chain DP: O(N^3)) ---")
    print(f"{'Matrices (N)':<15} | {'Time Taken (seconds)':<20}")
    print("-" * 40)
    
    for n in sizes:
        p = [random.randint(1, 100) for _ in range(n + 1)]
        
        start_time = time.time()
        matrix_chain_order(p, n)
        end_time = time.time()
        
        time_taken = end_time - start_time
        print(f"{n:<15} | {time_taken:<20.6f}")
    print("-" * 40)

def main():
    while True:
        print("\n=========================================")
        print(" VIDEO PROCESSING ENGINE (MCM DP)        ")
        print("=========================================")
        print("1. Calculate Optimal Matrix Multiplication")
        print("2. Run Performance Analysis")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                n = int(input("Enter number of matrices: "))
                if n <= 1:
                    print("Requires at least 2 matrices.")
                    continue
                    
                p = list(map(int, input(f"Enter the dimensions array (size {n + 1}) separated by space: ").split()))
                if len(p) != n + 1:
                    print(f"Error: Expected {n + 1} dimensions.")
                    continue
                
                matrix_chain_order(p, n, verbose=True)
                
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
