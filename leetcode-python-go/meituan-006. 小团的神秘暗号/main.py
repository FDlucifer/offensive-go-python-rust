n = int(input())
words = input()
left, right, l_comp, r_comp = 0, n - 1, ["T", "M"], ["M", "T"]
while l_comp or r_comp:
    if l_comp:
        if words[left] == l_comp[-1]:
            l_comp.pop()
        left += 1
    if r_comp:
        if words[right] == r_comp[-1]:
            r_comp.pop()
        right -= 1
print(words[left:right + 1])
