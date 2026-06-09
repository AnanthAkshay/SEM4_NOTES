import heapq
import time

class Node:

    def __init__(
        self,
        char,
        freq
    ):

        self.char = char
        self.freq = freq

        self.left = None
        self.right = None

    def __lt__(self, other):

        return self.freq < other.freq


def print_codes(root, code=""):

    if root is None:
        return

    if root.char:

        print(
            root.char,
            ":",
            code
        )

    print_codes(
        root.left,
        code + "0"
    )

    print_codes(
        root.right,
        code + "1"
    )


chars = ['A','B','C','D','E','F']

freqs = [5,9,12,13,16,45]

heap = []

for c, f in zip(chars, freqs):

    heapq.heappush(
        heap,
        Node(c, f)
    )

start = time.time()

while len(heap) > 1:

    left = heapq.heappop(heap)

    right = heapq.heappop(heap)

    merged = Node(
        None,
        left.freq + right.freq
    )

    merged.left = left
    merged.right = right

    heapq.heappush(
        heap,
        merged
    )

root = heap[0]

print("Huffman Codes:")

print_codes(root)

end = time.time()

print()

print(
    "Execution Time =",
    end - start,
    "seconds"
)
