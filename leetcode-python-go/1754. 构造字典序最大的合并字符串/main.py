word1 = "abcabc"
word2 = "abdcaba"

def largestMerge(word1: str, word2: str) -> str:
    merge = []
    i, j, n, m = 0, 0, len(word1), len(word2)
    while i < n or j < m:
        if i < n and word1[i:] > word2[j:]:
            merge.append(word1[i])
            i += 1
        else:
            merge.append(word2[j])
            j += 1
    return ''.join(merge)

print(largestMerge(word1, word2))