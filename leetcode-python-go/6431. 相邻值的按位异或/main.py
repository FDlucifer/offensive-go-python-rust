from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)

        # 检查特殊情况，当派生数组derived只有一个元素时，返回False
        if n == 1 and derived[0] == 1:
            return False
        elif n == 1 and derived[0] == 0:
            return True

        # 遍历原始数组的第一个元素，范围为[0, 1]
        for first_element in [0, 1]:
            # 构造原始数组
            original = [0] * n
            original[0] = first_element

            # 计算派生数组
            for i in range(n - 1):
                original[i + 1] = derived[i] ^ original[i]

            # 检查计算得到的派生数组是否与给定的derived数组相等
            if derived == [original[i] ^ original[(i + 1) % n] for i in range(n)]:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    derived = [1,1,0]
    print(s.doesValidArrayExist(derived))
