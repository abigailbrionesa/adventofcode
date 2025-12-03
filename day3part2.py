# lobby
def max_jolt(input):
    s = input.strip()
    n = len(s)
    if n <= 11:
        return
    if n == 12:
        return s
    res = []
    start = 0
    need = 12
    while need > 0:
        last = n - (need - 1)
        val = float('-inf')
        idx = start
        
        for i in range(start,last):
            c = int(s[i])
            if c > val:
                val = c
                idx = i
        res.append(str(val))
        start = idx + 1
        need -= 1
    return ''.join(res)
    
def total_output(inputs):
    total = 0
    for row in inputs:
        total += int(max_jolt(row))
    return total

def main():
    with open("input3.txt") as f:
        lines = f.readlines()
    total = total_output(lines)
    print('result:', total)

if __name__ == "__main__":
    main()

    
    

        