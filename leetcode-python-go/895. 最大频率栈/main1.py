from collections import defaultdict, Counter, deque

input = ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]

class FreqStack:

    def __init__(self):
        self.count,self.stack,self.maxFre=Counter(),[deque()]+[None]*20005,0

    def push(self, val: int) -> None:
        num=self.count[val]+1
        if num>self.maxFre:
            self.maxFre=num
            self.stack[num]=deque()
        self.count[val]=num
        self.stack[num].append(val)

    def pop(self) -> int:
        ans=self.stack[self.maxFre].pop()
        self.count[ans]=self.maxFre-1
        if not self.stack[self.maxFre]:
            self.maxFre-=1
        return ans

FreqStack = FreqStack()
result = []
result.append(FreqStack.push(5))
result.append(FreqStack.push(7))
result.append(FreqStack.push(5))
result.append(FreqStack.push(7))
result.append(FreqStack.push(4))
result.append(FreqStack.push(5))
result.append(FreqStack.pop())
result.append(FreqStack.pop())
result.append(FreqStack.pop())
result.append(FreqStack.pop())
print(result)