import heapq
import time
import random
import string
import sys

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison operators for heap operations
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if other is None:
            return False
        return self.freq == other.freq

def build_huffman_tree(text):
    if not text:
        return None

    # Calculate frequencies
    freq_map = {}
    for char in text:
        freq_map[char] = freq_map.get(char, 0) + 1

    # Create leaf nodes and push to priority queue (min-heap)
    heap = []
    for char, freq in freq_map.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(heap, node)

    # Edge case: text contains only one unique character
    if len(freq_map) == 1:
        char = list(freq_map.keys())[0]
        root = HuffmanNode(None, freq_map[char])
        root.left = HuffmanNode(char, freq_map[char])
        return root

    # Iterate until heap contains only one root node
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        # Merge nodes
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    return heap[0]

def get_huffman_codes(root, current_code="", codes_dict=None):
    if codes_dict is None:
        codes_dict = {}

    if root is None:
        return codes_dict

    # If it's a leaf node
    if root.char is not None:
        codes_dict[root.char] = current_code
        return codes_dict

    get_huffman_codes(root.left, current_code + "0", codes_dict)
    get_huffman_codes(root.right, current_code + "1", codes_dict)

    return codes_dict

def compress(text, verbose=True):
    if not text:
        print("Empty text cannot be compressed.")
        return "", 0, {}

    root = build_huffman_tree(text)
    codes = get_huffman_codes(root)

    # Build the compressed bitstream
    compressed_bits = "".join(codes[char] for char in text)
    
    if verbose:
        freq_map = {}
        for char in text:
            freq_map[char] = freq_map.get(char, 0) + 1
            
        print("\n--- Huffman Codes Generated ---")
        print(f"{'Character':<10} | {'Frequency':<10} | {'Huffman Code':<15}")
        print("-" * 45)
        for char in sorted(freq_map.keys()):
            display_char = repr(char) if char in ('\n', '\t', ' ') else char
            print(f"{display_char:<10} | {freq_map[char]:<10} | {codes[char]:<15}")

        print(f"\nOriginal Text: {text}")
        print(f"Compressed Bitstream: {compressed_bits}")
        
        orig_size_bits = len(text) * 8
        comp_size_bits = len(compressed_bits)
        compression_ratio = orig_size_bits / comp_size_bits if comp_size_bits > 0 else 0
        space_savings = (1 - (comp_size_bits / orig_size_bits)) * 100 if orig_size_bits > 0 else 0
        
        print("\n--- Compression Metrics ---")
        print(f"Original Size: {orig_size_bits} bits ({len(text)} bytes)")
        print(f"Compressed Size: {comp_size_bits} bits (~{(comp_size_bits + 7) // 8} bytes)")
        print(f"Compression Ratio: {compression_ratio:.2f}")
        print(f"Space Savings: {space_savings:.2f}%")

    return compressed_bits, len(compressed_bits), codes

def generate_random_text(length):
    charset = string.ascii_letters + string.digits + " "
    return "".join(random.choices(charset, k=length))

def performance_analysis():
    sizes = [100, 1000, 5000, 10000, 20000, 50000]
    
    print("\n--- Performance Analysis (Huffman Coding: O(N + C log C)) ---")
    print(f"{'Text Length (N)':<20} | {'Time Taken (seconds)':<20}")
    print("-" * 45)
    
    for n in sizes:
        text = generate_random_text(n)
        
        start_time = time.time()
        root = build_huffman_tree(text)
        codes = get_huffman_codes(root)
        # Simulate representation/encoding process
        dummy_list = [codes[char] for char in text]
        end_time = time.time()
        
        time_taken = end_time - start_time
        print(f"{n:<20} | {time_taken:<20.6f}")
    print("-" * 45)

def main():
    while True:
        print("\n=========================================")
        print(" TELECOM TEXT COMPRESSION SYSTEM (HUFFMAN) ")
        print("=========================================")
        print("1. Compress String")
        print("2. Run Performance Analysis")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            text = input("Enter text to compress: ")
            compress(text)
        elif choice == '2':
            performance_analysis()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
