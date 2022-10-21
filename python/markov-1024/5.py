cals = ["<<", "*", "+"]
nums = [16, 2, 16, 0]
target=1024

nums=[str(x) for x in nums]
exp =[]
def rec(cs, ns):
    if len(exp)>=7:
        return
    for (i,n) in enumerate(ns):
        exp.append(n)
        if len(exp)==7:
            expstr = ''.join(exp);
            if '//0' in expstr or '%0' in expstr:
                exp.pop()
                continue
            s=exp[0]
            for (y,x) in zip(list(range(7))[2::2],exp[2::2]):
                s=str(eval(s+exp[y-1]+x))
            if(int(s)==target):
                print(expstr)
        ns.pop(i)
        for(j,c) in enumerate(cs):
            exp.append(c)
            cs.pop(j)
            rec(cs,ns)
            cs.insert(j,c)
            exp.pop()
        ns.insert(i,n)
        exp.pop()

rec(cals, nums)

