import time
import random
import sys

sys.setrecursionlimit(200000)

class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        # Path Compression
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        # Already in same set
        if rootX == rootY:
            return

        # Union by Rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

    def are_friends(self, x, y):
        return self.find(x) == self.find(y)

def performance_analysis():
    sizes = [1, 10, 100, 1000, 10000, 100000]
    
    print("\n--- Performance Analysis (DSU: N Union ops) ---")
    print(f"{'N':<10} | {'Time Taken (seconds)':<20}")
    print("-" * 36)
    
    for n in sizes:
        dsu = DSU(n)
        
        start_time = time.time()
        for _ in range(n):
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            dsu.union(u, v)
        end_time = time.time()
        
        time_taken = end_time - start_time
        print(f"{n:<10} | {time_taken:<20.6f}")
    print("-" * 36)

def main():
    dsu = None
    while True:
        print("\n====================================")
        print(" SOCIAL NETWORK FRIEND GROUPS (DSU) ")
        print("====================================")
        print("1. Initialize Network (N users)")
        print("2. Make Friends (Union)")
        print("3. Check Friendship (Find)")
        print("4. Run Performance Analysis")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                n = int(input("Enter number of users in network: "))
                if n <= 0:
                    print("Invalid number of users!")
                    continue
                dsu = DSU(n)
                print(f"Network of {n} users created. User IDs: 0 to {n-1}")
            except ValueError:
                print("Invalid input!")
                
        elif choice == '2':
            if not dsu:
                print("Initialize network first!")
                continue
            try:
                u, v = map(int, input("Enter two User IDs to connect (e.g., 2 4): ").split())
                if 0 <= u < dsu.n and 0 <= v < dsu.n:
                    dsu.union(u, v)
                    print(f"User {u} and User {v} are now in the same friend group!")
                else:
                    print("Invalid User IDs!")
            except ValueError:
                print("Invalid input! Please enter two integers.")
                
        elif choice == '3':
            if not dsu:
                print("Initialize network first!")
                continue
            try:
                x, y = map(int, input("Enter two User IDs to check friendship: ").split())
                if 0 <= x < dsu.n and 0 <= y < dsu.n:
                    if dsu.are_friends(x, y):
                        print(f"Yes! User {x} and User {y} belong to the same friend group.")
                    else:
                        print(f"No. User {x} and User {y} are in different groups.")
                else:
                    print("Invalid User IDs!")
            except ValueError:
                print("Invalid input! Please enter two integers.")
                
        elif choice == '4':
            performance_analysis()
            
        elif choice == '5':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
