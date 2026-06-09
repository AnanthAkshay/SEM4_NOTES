import random
import time

def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


n = 1000

orders = [random.randint(1, 10000)
          for _ in range(n)]

start = time.time()

merge_sort(orders)

end = time.time()

print("First 20 Sorted Order IDs:")
print(orders[:20])

print("Execution Time =", end - start,
      "seconds")
