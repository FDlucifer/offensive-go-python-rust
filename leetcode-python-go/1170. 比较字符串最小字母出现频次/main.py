from typing import List

class Solution:
    def numSmallerByFrequency(self, queries, words):
        def f(s):
            return s.count(min(s))

        word_counts = [f(word) for word in words]
        word_counts.sort()
        answer = []

        for query in queries:
            query_count = f(query)
            left, right = 0, len(word_counts) - 1
            count = 0

            while left <= right:
                mid = (left + right) // 2

                if word_counts[mid] <= query_count:
                    left = mid + 1
                else:
                    count = len(word_counts) - mid
                    right = mid - 1

            answer.append(count)

        return answer

s = Solution()
queries = ["cbd"]
words = ["zaaaz"]
print(s.numSmallerByFrequency(queries, words))
