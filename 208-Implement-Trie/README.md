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
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            node = node.next[c]

        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root

        for c in word:
            node = node.next.get(c)
            if not node:
                return False

        return node.isWord


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            node = node.next.get(c)
            if not node:
                return False

        return True

class Node:
    def __init__(self):
        self.next = defaultdict(Node)
        self.isWord = False


s = Trie()

s.insert("apple")
s.insert("banana")
print(s.search("app"))
print(s.search("bananananana"))
print(s.search("banana"))
print(s.startsWith("ban"))
```
