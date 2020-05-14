# 208 - Implement Trie (Prefix Tree)

[leetcode](https://leetcode.com/problems/implement-trie-prefix-tree/)

## Problem

> Implement a trie with insert, search, and startsWith methods.
> 
> Example:
> 
> Trie trie = new Trie();
> 
> trie.insert("apple"); trie.search("apple"); */ returns true trie.search("app"); /* returns false trie.startsWith("app"); // returns true trie.insert("app"); trie.search("app"); // returns true

## Solution

Trie.

Use a "END" Symbol for word ending.

`search` method checks for "END", `startsWith` not.

```python
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
```
