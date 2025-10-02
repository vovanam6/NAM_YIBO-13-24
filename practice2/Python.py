Бинарная куча (Binary Heap)
import heapq

values = [9, 1, 6, 3, 7, 2, 8, 5]
heapq.heapify(values)
heapq.heappush(values, 0)
smallest = heapq.heappop(values)
print("Минимальный элемент:", smallest)
print("Состояние кучи:", values)

Куча Фибоначчи (Fibonacci Heap)
class FibonacciHeap:
    class Node:
        def __init__(self, key):
            self.key = key
            self.degree = 0
            self.marked = False
            self.parent = None
            self.child = None
            self.left = self
            self.right = self

    def __init__(self):
        self.minimum = None
        self.size = 0

    def insert(self, key):
        node = self.Node(key)
        if not self.minimum:
            self.minimum = node
        else:
            self._link_to_root(node)
            if node.key < self.minimum.key:
                self.minimum = node
        self.size += 1

    def _link_to_root(self, node):
        node.right = self.minimum.right
        node.left = self.minimum
        self.minimum.right.left = node
        self.minimum.right = node

    def min(self):
        return self.minimum.key if self.minimum else None


fib = FibonacciHeap()
fib.insert(11)
fib.insert(3)
fib.insert(17)
print("Минимум в куче Фибоначчи:", fib.min())

Биноминальная куча
    class Node:
        def __init__(self, key):
            self.key = key
            self.degree = 0
            self.parent = None
            self.child = None
            self.sibling = None

    def __init__(self):
        self.head = None

    def merge(self, other):
        if not self.head:
            return other.head
        if not other.head:
            return self.head

        if self.head.degree <= other.head.degree:
            result = self.head
            h1, h2 = self.head.sibling, other.head
        else:
            result = other.head
            h1, h2 = self.head, other.head.sibling

        tail = result
        while h1 and h2:
            if h1.degree <= h2.degree:
                tail.sibling, h1 = h1, h1.sibling
            else:
                tail.sibling, h2 = h2, h2.sibling
            tail = tail.sibling

        tail.sibling = h1 if h1 else h2
        return result

    def link(self, y, z):
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree += 1

    def union(self, other):
        self.head = self.merge(other)
        if not self.head:
            return

        prev = None
        curr = self.head
        nxt = curr.sibling

        while nxt:
            if (curr.degree != nxt.degree) or (nxt.sibling and nxt.sibling.degree == curr.degree):
                prev, curr, nxt = curr, nxt, nxt.sibling
            elif curr.key <= nxt.key:
                curr.sibling = nxt.sibling
                self.link(nxt, curr)
                nxt = curr.sibling
            else:
                if prev:
                    prev.sibling = nxt
                else:
                    self.head = nxt
                self.link(curr, nxt)
                curr = nxt
                nxt = nxt.sibling

    def insert(self, key):
        new_heap = BinomialHeap()
        new_heap.head = self.Node(key)
        self.union(new_heap)

    def get_min(self):
        if not self.head:
            return None
        min_node = self.head
        curr = self.head.sibling
        while curr:
            if curr.key < min_node.key:
                min_node = curr
            curr = curr.sibling
        return min_node.key

    def extract_min(self):
        if not self.head:
            return None

        min_node, min_prev = self.head, None
        prev, curr = None, self.head
        while curr:
            if curr.key < min_node.key:
                min_node, min_prev = curr, prev
            prev, curr = curr, curr.sibling

      
        if min_prev:
            min_prev.sibling = min_node.sibling
        else:
            self.head = min_node.sibling
       
        child_heap = BinomialHeap()
        child = min_node.child
        prev_child = None
        while child:
            next_child = child.sibling
            child.sibling = prev_child
            child.parent = None
            prev_child = child
            child = next_child
        child_heap.head = prev_child

        self.union(child_heap)
        return min_node.key

Хеш таблица
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        if self.table[index] and self.table[index][0] == key:
            return self.table[index][1]
        return None

ht = HashTable(10)
ht.set("Alice", 25)
ht.set("Bob", 30)
print(ht.get("Alice")) 
