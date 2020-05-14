class Trie:
    def __init__(self):
        self.root = Node()

    def search(self, s):
        node = self.root
        for c in s:
            node = node.next[ord(c) - ord('a')]
            if not node:
                return False
        return node.next[26] != None
        
    def insert(self, s):
        node = self.root
        for c in s:
            i = ord(c) - ord('a')
            if not node.next[i]:
                node.next[i] = Node()
            node = node.next[i]
        node.next[26] = Node()
        
    def startsWith(self, s):
        node = self.root
        for c in s:
            node = node.next[ord(c) - ord('a')]
            if not node:
                return False
        return True

class Node:
    def __init__(self):
        self.next = [ None for i in range(27) ]
        
s = Trie()

s.insert("apple")
s.insert("banana")
print(s.search("app"))
print(s.search("bananananana"))
print(s.search("banana"))
print(s.startsWith("ban"))
