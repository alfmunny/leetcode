class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.bitmasks = []
        for mask in range(1 << len(characters)):
            if bin(mask).count('1') == self.combinationLength:
                res = ""
                for i in range(len(characters)):
                    res = str(mask%2) + res
                    mask >>= 1
                self.bitmasks.append(res)
        self.bitmasks = self.bitmasks[::-1]


    def next(self) -> str:
        ans = ""
        mask = self.bitmasks.pop(0)
        for i in range(len(mask)):
            if mask[i] == "1":
                ans += self.characters[i]
        return ans

    def hasNext(self) -> bool:
        return self.bitmasks != []
