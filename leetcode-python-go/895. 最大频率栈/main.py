from collections import defaultdict

input = ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        self.maxFreq = max(self.maxFreq, self.freq[val])

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1
        if len(self.group[self.maxFreq]) == 0:
            self.maxFreq -= 1
        return val

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