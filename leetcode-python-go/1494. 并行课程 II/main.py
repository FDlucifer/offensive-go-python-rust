from typing import List
from itertools import combinations # 求出k n
from functools import lru_cache
from collections import defaultdict

class Solution:
    @lru_cache(None) # 使用lru_catch缓存以更快的查找
    def recurse(self, mask, in_degrees):
        # 如果所有的位都是0，我们就上了所有的课
        if not mask: return 0

        # 现在所有的节点都*可以*被取走，遵循这两个属性
        nodes = [i for i in range(self.n) if mask & 1 << i and in_degrees[i] == 0]

        ans = float('inf')
        # 列举所有可能的组合
        for k_nodes in combinations(nodes, min(self.k, len(nodes))):
            new_mask, new_in_degrees = mask, list(in_degrees)

            # 更新new_mask和new_in_degrees会发生什么
            # 如果我们考虑k_nodes中的节点
            for node in k_nodes:
                # 因为我们知道这个位已经设置好了，所以我们取消了这个位的设置，把它标记为"considered"。
                new_mask ^= 1 << node
                # 更新每一个in-degree，因为"parents"已经被拿走了
                for child in self.graph[node]:
                    new_in_degrees[child] -= 1

            # 递归的核心
            # 注意+1!
            ans = min(ans, 1+self.recurse(new_mask, tuple(new_in_degrees)))
        return ans

    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # 保存n和k以备以后使用
        self.n = n
        self.k = k
        in_degrees = [0]*self.n
        # 图形布局保持不变，尽管in_degrees改变了。
        # 这允许我们将graph保持为self.graph
        # 而不是一遍又一遍地传递。
        self.graph = defaultdict(list)
        for prev_course, next_course in relations:
            # 记住，它现在是0索引了!
            in_degrees[next_course - 1] += 1
            self.graph[prev_course - 1].append(next_course - 1)

        # 从所有位设置开始
        return self.recurse((1 << self.n) - 1, tuple(in_degrees))


s = Solution()
n = 5
relations = [[2,1],[3,1],[4,1],[1,5]]
k = 2
print(s.minNumberOfSemesters(n, relations, k))

