import heapq
from collections import Counter, namedtuple

# Node definition
class Node(namedtuple("Node", "freq char left right")):
    def __lt__(self, other):
        return self.freq < other.freq

# Recursive function to generate codes
def generate_codes(node, code="", codes={}):
    if node:
        if node.char:
            codes[node.char] = code
        generate_codes(node.left, code + "0", codes)
        generate_codes(node.right, code + "1", codes)
    return codes

def huffman(text):
    freq = Counter(text)
    # print(freq)
    heap = [Node(freq[c], c, None, None) for c in freq]
    print(heap)
    heapq.heapify(heap)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, Node(a.freq + b.freq, None, a, b))

    root = heap[0]
    return generate_codes(root)

# Example
text = "Huffman coding in Python"
codes = huffman(text)
for char in sorted(codes):
    print(f"{repr(char)}: {codes[char]}")
