from typing import List

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(int(num) if num.isdigit() else len(num) for num in strs)


s = Solution()
strs = ["alic3","bob","3","4","00000"]
print(s.maximumValue(strs))
