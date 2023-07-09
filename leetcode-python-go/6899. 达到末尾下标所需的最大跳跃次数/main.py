from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        def find_longest_path(edges, start, end):
            graph = {}
            for edge in edges:
                if edge[0] not in graph:
                    graph[edge[0]] = []
                graph[edge[0]].append(edge[1])

            def dfs(node, path):
                if node == end:
                    return path
                if node not in graph:
                    return None

                longest_path = None
                for neighbor in graph[node]:
                    if neighbor not in path:
                        result = dfs(neighbor, path + [neighbor])
                        if result is not None and (
                            longest_path is None or len(result) > len(longest_path)
                        ):
                            longest_path = result

                return longest_path

            return dfs(start, [start])

        lis = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if -target <= nums[j] - nums[i] <= target:
                    lis.append([i, j])

        res = find_longest_path(lis, 0, len(nums) - 1)
        if res == None:
            return -1
        else:
            return len(res) - 1


s = Solution()
nums = [1, 3, 6, 4, 1, 2]
target = 3
print(s.maximumJumps(nums, target))
