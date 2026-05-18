class MinStack:

    def __init__(self):
        
        self.stack = []

    def push(self, val: int) -> None:
        
        self.stack.append(val)

    def pop(self) -> None:
        
        self.stack.pop()

    def top(self) -> int:
        
        l = len(self.stack) -1
        return self.stack[l]

    def getMin(self) -> int:
        
        minq = self.stack.copy()

        heapq.heapify(minq)

        return heapq.heappop(minq)
