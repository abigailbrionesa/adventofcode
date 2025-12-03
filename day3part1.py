# lobby
def max_jolt(input):
    s = input.strip()
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
        if int(c) > max:
            max = int(c)
    res.append(str(max))
    return ''.join(res)

def total_output(inputs):
    total = 0
    for row in inputs:
        total += int(max_jolt(row))
    return total

def main():
    with open("input3example.txt") as f:
        lines = f.readlines()
    total = total_output(lines)
    print('result:', total)

if __name__ == "__main__":
    main()

    
    

        