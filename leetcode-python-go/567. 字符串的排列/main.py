s1 = "ab"
s2 = "eidbaooo"

def checkInclusion(s1: str, s2: str) -> bool:
    '''
    思路：怎么判断s2的字串和s1的排列之一相等，假如排序的话，遍历s2的同时，每次都排序，总的时间复杂度太高了。
    因此，我们采用一个有序字典来比较，由于只包含小写字母，我们采用数组来模拟有序字典，
    这样判断s2的子串和s1的排列之一相等就很容易了。总的时间复杂度为O(n),n为s2的长度。
    空间复杂度为:O(26)*2 == O(1) 

    '''
    m1 = len(s1)
    m2 = len(s2)
    if m1 > m2:
        return False
    dic1 = [0]*26
    dic2 = [0]*26
    for i in range(m1):
        dic1[ord(s1[i])-ord('a')] += 1
        dic2[ord(s2[i])-ord('a')] += 1
    if dic1 == dic2:
        return True

    for i in range(m1,m2):
        dic2[ord(s2[i-m1])-ord('a')] -= 1
        dic2[ord(s2[i])-ord('a')] += 1
        if dic1 == dic2:
            return True
    return False

print(checkInclusion(s1, s2))