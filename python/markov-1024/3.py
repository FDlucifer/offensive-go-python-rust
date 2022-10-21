digits = 4
target = 1024


class Solution2:
    def calculate(self, nums, ops):
        from itertools import permutations
        for n in permutations(nums, digits):
            for o in permutations(ops, digits - 1):
                for exp in self.parentheses(n, o, 0, len(o)):
                    result = eval(exp)
                    if result == target:
                        print(exp, "=", result)

    def parentheses(self, nums, ops, l, r) -> list[str]:
        ways = []
        [[[ways.append("(" + left + ops[i] + right + ")") for right in self.parentheses(nums, ops, i + 1, r)] for left
          in self.parentheses(nums, ops, l, i)] for i in range(l, r)]
        return ways if ways else [str(nums[l])]


if __name__ == '__main__':
    Solution2().calculate([2, 12, 13, 0, 6], ["+", "|", "&"])


