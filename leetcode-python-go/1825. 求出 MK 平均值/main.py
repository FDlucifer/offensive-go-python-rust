from collections import deque
from sortedcontainers import SortedList

class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.q = deque()
        self.s_s = SortedList()  # small 即最小的 k 个元素
        self.s_m = SortedList()  # middle 即中间的 m-2k 个元素
        self.s_l = SortedList()  # large 即最大的 k 个元素
        self.s = 0

    def addElement(self, num: int) -> None:
        self.q.append(num)
        if len(self.q) == self.m:
            # 此次加进 num 元素后满足了元素数量，开始构造三个有序集合

            self.s_m.update(list(self.q))
            for _ in range(self.k):
                num = self.s_m.pop(0)
                self.s_s.add(num)
            for _ in range(self.k):
                num = self.s_m.pop(-1)
                self.s_l.add(num)
            self.s = sum(self.s_m)
        elif len(self.q) > self.m:
            # 后续维护三个有序集合

            # 维护的第一步：本次新增的元素应该加到哪个集合
            if num <= self.s_s[-1]:
                self.s_s.add(num)
                num = self.s_s.pop(-1)
                self.s_m.add(num)
                self.s += num
            elif num >= self.s_l[0]:
                self.s_l.add(num)
                num = self.s_l.pop(0)
                self.s_m.add(num)
                self.s += num
            else:
                self.s_m.add(num)
                self.s += num

            # 维护的第二步：本次过期的元素应该从哪个集合删掉
            num = self.q.popleft()
            if num in self.s_s:
                self.s_s.remove(num)
                num = self.s_m.pop(0)
                self.s_s.add(num)
                self.s -= num
            elif num in self.s_l:
                self.s_l.remove(num)
                num = self.s_m.pop(-1)
                self.s_l.add(num)
                self.s -= num
            else:
                self.s_m.remove(num)
                self.s -= num

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        else:
            # 在 .addElement() 中已经完成了维护工作，.s 一直都是中间 m-2k 个元素的和
            return self.s // (self.m - self.k * 2)