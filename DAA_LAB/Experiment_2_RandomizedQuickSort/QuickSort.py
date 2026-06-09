import random
import time

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

    random_index = random.randint(low, high)

    arr[random_index], arr[high] = \
        arr[high], arr[random_index]

    return partition(arr, low, high)


def quick_sort(arr, low, high):

    if low < high:

        pi = randomized_partition(
            arr, low, high
        )

        quick_sort(arr, low, pi - 1)

        quick_sort(arr, pi + 1, high)


n = 1000

arr = [random.randint(1, 10000)
       for _ in range(n)]

start = time.time()

quick_sort(arr, 0, n - 1)

end = time.time()

print("First 20 Sorted Package IDs:")
print(arr[:20])

print("Execution Time =", end - start,
      "seconds")
