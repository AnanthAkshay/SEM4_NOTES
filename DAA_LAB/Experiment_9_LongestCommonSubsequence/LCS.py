import time
import random
import string

def lcs(X, Y, verbose=False):
    m = len(X)
    n = len(Y)
    
    # L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Build L[m+1][n+1] in bottom up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
                
    length = L[m][n]
    
    if verbose:
        # Code to print the LCS
        index = length
        lcs_algo = [""] * index
        
        i = m
        j = n
        while i > 0 and j > 0:
            if X[i - 1] == Y[j - 1]:
                lcs_algo[index - 1] = X[i - 1]
                i -= 1
                j -= 1
                index -= 1
            elif L[i - 1][j] > L[i][j - 1]:
                i -= 1
            else:
                j -= 1
                
        print(f"Longest Matching Sequence: \"{''.join(lcs_algo)}\"")
        print(f"Length of LCS: {length}")
        
    return length

def generate_random_string(length):
    return ''.join(random.choices("ACTG", k=length))

def performance_analysis():
    sizes = [10, 100, 500, 1000, 2000]
    
    print("\n--- Performance Analysis (LCS DP: O(M*N)) ---")
    print(f"{'String Lengths (N)':<20} | {'Time Taken (seconds)':<20}")
    print("-" * 45)
    
    for n in sizes:
        X = generate_random_string(n)
        Y = generate_random_string(n)
        
        start_time = time.time()
        lcs(X, Y)
        end_time = time.time()
        
        time_taken = end_time - start_time
        print(f"{n:<20} | {time_taken:<20.6f}")
    print("-" * 45)

def main():
    while True:
        print("\n=========================================")
        print(" PLAGIARISM DETECTION SYSTEM (LCS DP)    ")
        print("=========================================")
        print("1. Compare Two Strings (Detect Plagiarism)")
        print("2. Run Performance Analysis")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            X = input("Enter first string (Essay 1): ")
            Y = input("Enter second string (Essay 2): ")
            
            print("\nAnalyzing...")
            lcs(X, Y, verbose=True)
                
        elif choice == '2':
            performance_analysis()
            
        elif choice == '3':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
