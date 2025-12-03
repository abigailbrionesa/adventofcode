# lobby
def max_jolt(input):
    s = str(input)
    n = len(s)
    max = float('-inf')
    last = 0
    for i in range(0,n-1):
        c = s[i]
        if int(c) > max:
            max = int(c)
            last = i
    if last == (n-2):
        return s[n-2:n]
    res = [str(max)]
    max = float('-inf')
    for j in range(last+1,n):
        c = s[j]
        print(c)
        if int(j) > max:
            max = int(c)
    res.append(str(max))
    return ''.join(res)

print(max_jolt(234234234234278))