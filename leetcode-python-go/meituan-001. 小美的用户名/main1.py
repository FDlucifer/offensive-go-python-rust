letter, nums = {chr(i) for i in range(97,97+26)}|{chr(i) for i in range(65,65+26)}, {str(i) for i in range(10)}

def is_accept(s):
    if not s or s[0] not in letter:
        return False
    if (m1:=len(set((sets:=set(s))&letter))) and (m2:=len(set(sets&nums))) and m1 + m2 == len(sets):
        return True
    else:
        return False

for i in range(int(input())):
    print('Accept' if is_accept(input()) else 'Wrong')
