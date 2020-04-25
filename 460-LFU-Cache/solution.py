class Node:
    def __init__(self, key, value):
        self.freq = 1
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self._head = Node(0, 0)
        self._tail = Node(0, 0)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def append(self, node):
        self._connect(node, self._head.next)
        self._connect(self._head, node)
        self._size += 1

    def pop(self, node):
        self._connect(node.prev, node.next)
        node.next = None
        node.prev = None
        self._size -= 1
        return node

    def pop_last(self):
        return self.pop(self._tail.prev)

    def get_size(self):
        return self._size

    def _connect(self, p, n):
        p.next, n.prev = n, p


class LFUCache:
    def __init__(self, capacity):
        self.nodes = {}
        self.freq = {}
        self.min_freq = 1
        self.capacity = capacity

    def get(self, key):
        if key in self.nodes:
            node = self.nodes[key]
            l = self.freq[node.freq]
            l.pop(node)
            if l.get_size() == 0 and self.min_freq == node.freq:
                self.min_freq += 1

            node.freq += 1
            if self.freq.get(node.freq):
                self.freq[node.freq].append(node)
            else:
                l = DoubleLinkedList()
                l.append(node)
                self.freq[node.freq] = l
            return node.value
        else:
            return -1

    def put(self, key, value):

        if self.capacity == 0:
            return

        if key in self.nodes:
            self.nodes[key].value = value
            self.get(key)
        else:
            node = Node(key, value)
            if len(self.nodes) == self.capacity:
                l = self.freq[self.min_freq]
                n = l.pop_last()
                self.nodes.pop(n.key)

            self.nodes[key] = node

            if 1 in self.freq:
                self.freq[1].append(node)
            else:
                l = DoubleLinkedList()
                l.append(node)
                self.freq[1] = l
            self.min_freq = 1


c = LFUCache(3)
c.put(1, 1)
c.put(2, 2)
print(c.get(1))
print(c.get(2))
print(c.get(1))
c.put(3, 3)
print(c.get(2))
print(c.get(3))
c.put(4, 4)

print(c.get(4))
