class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.getMin() or self.getMin() >= x:
            self.min.append(x)

    def pop(self) -> None:
        if self.stack:
            x = self.stack.pop()
            if x == self.min[-1]:
                self.min.pop()
        else:
            None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            None

    def getMin(self) -> int:
        if self.min:
            return self.min[-1]
        else:
            return None
