from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0  # 记录总的移动次数

        def dfs(node):
            if not node:
                return 0

            left_moves = dfs(node.left)  # 处理左子树
            right_moves = dfs(node.right)  # 处理右子树

            # 计算当前节点的总移动次数
            self.moves += abs(left_moves) + abs(right_moves)

            # 返回当前节点的硬币数量与1之间的差，用于上一层节点的计算
            return node.val + left_moves + right_moves - 1

        dfs(root)
        return self.moves


# 创建树节点
root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(0)

# 创建Solution实例
solution = Solution()

# 调用distributeCoins方法并打印结果
result = solution.distributeCoins(root)
print(result)
