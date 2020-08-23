class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        
        for w in words:
            x = self.root
            for c in reversed(w):
                if c in x.children:
                    x = x.children[c]
                else:
                    x.children[c] = TrieNode()
                    x = x.children[c]
            x.is_word = True
            
        self.s = ""
        self.w = max(map(len, words))

    def query(self, letter: str) -> bool:
        
        self.s = (letter+self.s)[:self.w]
        x = self.root
        res = False
        
        for c in self.s:
            if c in x.children:
                x = x.children[c]
                if x.is_word:
                    return True
            else:
                return False
            
        return res
        
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
