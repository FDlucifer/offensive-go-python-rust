def main():
    res = 0
    a, b, c, d, e, f, g = map(int, input().split())
    if e < f:
        a, b, e, f = b, a, f, e
    if e < g:
        a, c, e, g = c, a, g, e
    if f < g:
        b, c, f, g = c, b, g, f
    if a >= d:
        return d * e
    res, d = res + a * e, d - a
    if b >= d:
        return res + d * f
    res, d = res + b * f, d - b
    return res + min(c, d) * g

print(main())
