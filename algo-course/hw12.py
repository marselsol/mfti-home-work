from PIL import Image
from collections import Counter
import heapq
import numpy as np


class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq_map):
    heap = [Node(value, freq) for value, freq in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def build_huffman_codes(root, code="", huffman_codes={}):
    if root is None:
        return
    if root.value is not None:
        huffman_codes[root.value] = code
    build_huffman_codes(root.left, code + "0", huffman_codes)
    build_huffman_codes(root.right, code + "1", huffman_codes)
    return huffman_codes


def compress_image(image, huffman_codes):
    compressed = []
    for pixel in image.getdata():
        compressed.append(huffman_codes[pixel])
    return "".join(compressed)


def decompress_image(compressed_data, huffman_tree, width, height):
    decompressed = []
    node = huffman_tree
    for bit in compressed_data:
        node = node.left if bit == "0" else node.right
        if node.value is not None:
            decompressed.append(node.value)
            node = huffman_tree

    image_data = np.array(decompressed, dtype=np.uint8).reshape((height, width))
    return Image.fromarray(image_data, mode="L")


def print_huffman_tree(node, indent=0):
    if node is not None:
        if node.value is not None:
            print(" " * indent + f"Pixel: {node.value}, Freq: {node.freq}")
        else:
            print(" " * indent + f"Node Freq: {node.freq}")
        print_huffman_tree(node.left, indent + 4)
        print_huffman_tree(node.right, indent + 4)


# Шаг 1: Открытие изображения и построение дерева Хаффмана
image_path = "gray.bmp"
image = Image.open(image_path).convert("L")
freq_map = Counter(image.getdata())
huffman_tree = build_huffman_tree(freq_map)

# Печать дерева Хаффмана
print("Дерево Хаффмана:")
print_huffman_tree(huffman_tree)

# Шаг 2: Сжатие изображения
huffman_codes = build_huffman_codes(huffman_tree)
compressed_data = compress_image(image, huffman_codes)

# Шаг 3: Восстановление изображения
width, height = image.size
decompressed_image = decompress_image(compressed_data, huffman_tree, width, height)

# Сохранение восстановленного изображения
decompressed_image.save("decompressed_image.bmp")

print("Сжатие и восстановление завершены. Результат сохранен в 'decompressed_image.bmp'")
