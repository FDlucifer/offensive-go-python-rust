from collections import defaultdict, Counter
import heapq

input = ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]

class FreqStack:

    def __init__(self):
        self.q,self.count,self.t=[],Counter(),0

    def push(self, val: int) -> None:
        self.t+=1
        self.count[val]+=1
        heapq.heappush(self.q,[-self.count[val],-self.t,val])

    def pop(self) -> int:
        arr=heapq.heappop(self.q)
        self.count[arr[2]]-=1
        return arr[2]

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