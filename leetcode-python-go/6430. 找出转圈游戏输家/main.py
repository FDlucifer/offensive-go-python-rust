from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        answer = []
        curr_player = 1
        answer.append(curr_player)

        # 在第 i 轮中计算持球者需要传球给的下一个玩家
        for i in range(1, 50):
            next_player = (curr_player + i * k) % n

            # 如果下一个玩家是 0，则将其转换为 n
            if next_player == 0:
                next_player = n

            # 如果下一个玩家已经在答案中，表示他接到了球两次，游戏结束
            if next_player in answer:
                break

            # 将下一个玩家添加到答案中
            answer.append(next_player)
            curr_player = next_player
        result = [i for i in range(1, n + 1) if i not in sorted(answer)]
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.circularGameLosers(5, 2))  # 输出: [4, 5]
    print(solution.circularGameLosers(4, 4))
