# https://leetcode.cn/circle/discuss/OV9VUd/

import operator

nums = [2, 12, 13, 0, 6]
ops = {
    '|': operator.pow,
    '+': operator.add,
}

def do(nums, ops):

    gg = set()
    path = []
    used = [False] * len(nums)
    target = 1024
    def bt(now, s):
        # print(f'{path=}, {now=}')
        if now == target and len(path)==3:
            print('found', path, s)
            return

        for op in ops:
            if op not in gg:
                gg.add(op)

                for i in range(len(nums)):
                    if not used[i]:
                        used[i] = True
                        path.append('%s %s %s' % (now, op, nums[i]))
                        try:
                            v = ops[op](now, nums[i])
                        except Exception:
                            pass
                        else:
                            bt(v, '(%s)%s%s' % (s, op, nums[i]))
                        path.pop()
                        used[i] = False
                gg.remove(op)

    for i, v in enumerate(nums):
        used[i] = 1
        bt(v, str(v))
        used[i] = 0
# 任选其一就行
do(nums, ops)

