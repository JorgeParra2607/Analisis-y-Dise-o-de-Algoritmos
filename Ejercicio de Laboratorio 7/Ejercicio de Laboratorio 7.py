import heapq
from collections import defaultdict
import os

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequency(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    return frequency

def build_heap(frequency):
    heap = []
    for key in frequency:
        node = Node(key, frequency[key])
        heapq.heappush(heap, node)
    return heap

def merge_nodes(heap):
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

def build_codes_helper(root, current_code, codes):
    if root == None:
        return

    if root.char!= None:
        codes[root.char] = current_code

    build_codes_helper(root.left, current_code + "0", codes)
    build_codes_helper(root.right, current_code + "1", codes)

def build_codes(root):
    codes = {}
    build_codes_helper(root, "", codes)
    return codes

def huffman_encoding(text):
    frequency = calculate_frequency(text)
    heap = build_heap(frequency)
    merge_nodes(heap)

    root = heap[0]
    codes = build_codes(root)

    encoded_text = ""
    for char in text:
        encoded_text += codes[char]

    return encoded_text, root, codes

def huffman_decoding(encoded_text, root):
    decoded_text = ""
    current_node = root

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char!= None:
            decoded_text += current_node.char
            current_node = root

    return decoded_text

def write_to_file(data, filename):
    with open(filename, "w") as f:
        f.write(data)

def write_codes_to_file(codes, filename):
    with open(filename, "w") as f:
        for char, code in codes.items():
            f.write(f"{char}: {code}\n")

def main():
    text = input("Ingresa un texto: ")

    if not text:
        print("Error: El texto no debe estar vacio.")
        return

    encoded_text, root, codes = huffman_encoding(text)

    write_to_file(text, "original_text.txt")
    write_to_file(encoded_text, "encoded_text.txt")
    write_codes_to_file(codes, "huffman_codes.txt")

    print("Texto Original:", text)
    print("Texto Codificado:", encoded_text)

    decoded_text = huffman_decoding(encoded_text, root)

    print("Texto Decodificado:", decoded_text)

if __name__ == "__main__":
    main()
