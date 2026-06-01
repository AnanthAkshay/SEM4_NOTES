import time
import random

class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
            # Swap with parent
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_max(self):
        if len(self.heap) == 0:
            print("Priority Queue is empty!")
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        # Move last element to root
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            # Swap with largest child
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    def peek(self):
        if len(self.heap) == 0:
            print("Priority Queue is empty!")
            return None
        return self.heap[0]

    def display(self):
        print(self.heap)


def performance_analysis():
    sizes = [1, 10, 100, 1000, 10000, 100000]
    
    print("\n--- Performance Analysis (Extract Max Time) ---")
    print(f"{'N':<10} | {'Time Taken (seconds)':<20}")
    print("-" * 36)
    
    for n in sizes:
        pq = MaxHeap()
        # Insert N random elements
        for _ in range(n):
            pq.insert(random.randint(1, 1000000))
            
        # Measure time taken to extract max N times
        start_time = time.time()
        for _ in range(n):
            pq.extract_max()
        end_time = time.time()
        
        time_taken = end_time - start_time
        print(f"{n:<10} | {time_taken:<20.6f}")
    print("-" * 36)

def main():
    pq = MaxHeap()
    while True:
        print("\n==================================")
        print(" AIRLINE BOARDING PRIORITY SYSTEM ")
        print("==================================")
        print("1. Insert Passenger (Priority Score)")
        print("2. Extract Highest Priority (Board)")
        print("3. Peek Highest Priority")
        print("4. Display All Waiting Passengers")
        print("5. Run Performance Analysis")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                val = int(input("Enter Priority Score: "))
                pq.insert(val)
                print(f"Passenger with score {val} inserted.")
            except ValueError:
                print("Invalid input! Please enter an integer.")
                
        elif choice == '2':
            val = pq.extract_max()
            if val is not None:
                print(f"Boarding passenger with score: {val}")
                
        elif choice == '3':
            val = pq.peek()
            if val is not None:
                print(f"Next passenger to board has score: {val}")
                
        elif choice == '4':
            print("Waiting passengers (Heap Array): ", end="")
            pq.display()
            
        elif choice == '5':
            performance_analysis()
            
        elif choice == '6':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
