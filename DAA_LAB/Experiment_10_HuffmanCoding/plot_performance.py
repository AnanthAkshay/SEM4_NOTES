import matplotlib.pyplot as plt
import time
import random
import string
import os

try:
    from Huffman import build_huffman_tree, get_huffman_codes
except ImportError:
    import heapq
    class HuffmanNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None
        def __lt__(self, other):
            return self.freq < other.freq

    def build_huffman_tree(text):
        freq_map = {}
        for char in text:
            freq_map[char] = freq_map.get(char, 0) + 1
        heap = []
        for char, freq in freq_map.items():
            heapq.heappush(heap, HuffmanNode(char, freq))
        if len(freq_map) == 1:
            char = list(freq_map.keys())[0]
            root = HuffmanNode(None, freq_map[char])
            root.left = HuffmanNode(char, freq_map[char])
            return root
        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            merged = HuffmanNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(heap, merged)
        return heap[0] if heap else None

    def get_huffman_codes(root, current_code="", codes_dict=None):
        if codes_dict is None:
            codes_dict = {}
        if root is None:
            return codes_dict
        if root.char is not None:
            codes_dict[root.char] = current_code
            return codes_dict
        get_huffman_codes(root.left, current_code + "0", codes_dict)
        get_huffman_codes(root.right, current_code + "1", codes_dict)
        return codes_dict

def generate_random_text(length):
    charset = string.ascii_letters + string.digits + " "
    return "".join(random.choices(charset, k=length))

def plot_performance():
    sizes = [100, 1000, 10000, 50000, 100000, 200000]
    times = []

    print("Generating performance data for Huffman Coding. This may take a few seconds...")
    
    for n in sizes:
        text = generate_random_text(n)
        
        start_time = time.time()
        root = build_huffman_tree(text)
        codes = get_huffman_codes(root)
        # Simulate representation/encoding process
        dummy_list = [codes[char] for char in text]
        end_time = time.time()
        
        time_taken = end_time - start_time
        times.append(time_taken)
        print(f"Processed N = {n:<10} | Time = {time_taken:.6f} s")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-', color='purple', linewidth=2, markersize=8)
    
    plt.title('Performance Analysis of Huffman Coding O(N + C log C)', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Text Length (N)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    
    plt.grid(True, which="both", ls="--", alpha=0.6)
    
    for i, txt in enumerate(times):
        plt.annotate(f"{txt:.5f}s", (sizes[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center')

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Huffman_Performance.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nGraph saved successfully to: {save_path}")

if __name__ == "__main__":
    plot_performance()
