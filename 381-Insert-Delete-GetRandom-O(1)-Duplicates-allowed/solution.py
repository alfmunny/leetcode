class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.list.append(val)
        if val not in self.dict:
            ret = True
        else:
            ret = False
        self.dict[val].add(len(self.list) - 1)
        return ret
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.dict[val]:
            rm_index = self.dict[val].pop()
            last = self.list[-1]
            self.list[rm_index] = last
            self.dict[last].add(rm_index)
            self.dict[last].discard(len(self.list) - 1)
            self.list.pop()
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
