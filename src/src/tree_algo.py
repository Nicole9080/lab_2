class BST:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = self.Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = self.Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if not node.right:
                node.right = self.Node(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_node = node.right
            while min_node.left:
                min_node = min_node.left
            node.value = min_node.value
            node.right = self._delete(node.right, min_node.value)
        return node

def heap_sort(arr):
    def heapify(n, i):
        largest, left, right = i, 2*i+1, 2*i+2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)
    return arr
