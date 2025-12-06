def main():
    with open("input6.txt") as f:
        lines = f.read().splitlines()

    w = max(len(l) for l in lines)
    h = len(lines)
    g = [list(l.ljust(w)) for l in lines]

    ops = [c for c in g[-1] if c in '+*']
    res = []
    cur = w - 1

    while cur >= 0:
        if all(g[r][cur] == ' ' for r in range(h)):
            cur -= 1
            continue

        if not ops:
            break
        op = ops.pop()

        nums = []

        while cur >= 0:
            if all(g[r][cur] == ' ' for r in range(h-1)) and nums:
                break

            col = [g[r][cur] for r in range(h-1)]
            if any(c != ' ' for c in col):
                nstr = ''.join(col).strip()
                if nstr:
                    try:
                        nums.append(int(nstr))
                    except ValueError:
                        pass

            cur -= 1

        if op == '+':
            r = sum(nums)
        else:
            r = 1
            for n in nums:
                r *= n

        res.append(r)

    print("total:", sum(res))


if __name__ == "__main__":
    main()
