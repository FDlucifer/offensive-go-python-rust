from typing import List

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]

def calc_statistic(input_str) -> str:  # 计算英文字母出现的频率
    result = [0] * 26      # 构建结果列表
    char = []
    for c in input_str:    # 对于每个输入字符串中的字符
        if c.isalpha():    # 必须是26*2个字符之一
            c = c.lower()  # 统一转换成小写字符
            index = ord(c) - ord('a')   # 计算出其对应的位置
            result[index] = result[index] + 1   # 将出现的次数加一
    for ele in range(0, 26):                    # 显示打印结果
        c = chr(ord('a') + ele)                 # 将位置转换成字符
        if result[ele] != 0:
            # print("[%s] Shows Up %d Times" % (c, result[ele]))  # 显示结果
            char.append(c) # 将出现次数不为0的字母加入到数列中
 
    return char
    

def countConsistentStrings(allowed: str, words: List[str]) -> int:
    count = 0
    for word in words:
        if set(calc_statistic(word)) <= set(calc_statistic(allowed)):
            count += 1
    return count


print(countConsistentStrings(allowed, words))