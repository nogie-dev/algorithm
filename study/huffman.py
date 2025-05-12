import heapq

class Node:
    def __init__(self, weight, left=None, right=None):
        self.weight = weight
        self.left = left
        self.right = right

    def __lt__(self, other):  # heapq에서 사용될 비교 연산
        return self.weight < other.weight

# 1. 입력 가중치 (빈도)
weights = [5, 10, 12, 16, 17, 25]

# 2. 초기 힙 구성 (Node 객체로 변환)
heap = [Node(weight=w) for w in weights]
heapq.heapify(heap)

# 3. 허프만 트리 만들기
while len(heap) > 1:
    node1 = heapq.heappop(heap)
    node2 = heapq.heappop(heap)
    merged = Node(weight=node1.weight + node2.weight, left=node1, right=node2)
    heapq.heappush(heap, merged)

# 최종 루트 노드
root = heap[0]

# 4. 허프만 코드 생성
huffman_codes = {}

def generate_codes(node, code=""):
    if node.left is None and node.right is None:  # 리프 노드
        huffman_codes[node.weight] = code
        return
    if node.left:
        generate_codes(node.left, code + "0")
    if node.right:
        generate_codes(node.right, code + "1")

generate_codes(root)

# 5. 출력 (빈도 높은 순으로)
for weight in sorted(huffman_codes.keys(), reverse=True):
    print(f"{weight} : {huffman_codes[weight]}")
