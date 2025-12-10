#factory

#bit method


#gaussian method (We could use bits?)
def fewest_presses(options,goal):
    n = len(goal)
    m = len(options)
    A = [[0]*m for _ in range(n)]
    for j, btn in enumerate(options):
        for i in btn:
            A[i][j] = 1
    b = [1 if c == '#' else 0 for c in goal]

    def gauss_jordan(A, b):
        #gaussian elimination
        n = len(A)
        m = len(A[0])
        A = [row[:] for row in A]
        b = b[:]
        where = [-1]*m
        row = 0
        for col in range(m):
            sel = -1
            for i in range(row, n):
                if A[i][col]:
                    sel = i
                    break
            if sel == -1:
                continue
            A[row], A[sel] = A[sel], A[row]
            b[row], b[sel] = b[sel], b[row]
            where[col] = row
            for i in range(n):
                if i != row and A[i][col]:
                    for j in range(col, m):
                        A[i][j] ^= A[row][j]
                    b[i] ^= b[row]
            row += 1
        for i in range(row, n):
            if b[i]:
                return None
        from itertools import product
        free_vars = [i for i in range(m) if where[i] == -1]
        min_presses = None
        for free_vals in product([0,1], repeat=len(free_vars)):
            x = [0]*m
            for idx, val in zip(free_vars, free_vals):
                x[idx] = val
            for i in range(m):
                if where[i] != -1:
                    s = b[where[i]]
                    for j in range(m):
                        if j != i and A[where[i]][j]:
                            s ^= x[j]
                    x[i] = s
            presses = sum(x)
            if min_presses is None or presses < min_presses:
                min_presses = presses
        return min_presses

    return gauss_jordan(A, b)

def main():
    with open('input10.txt') as f:
        content = f.read().strip().splitlines()

    def parse_line(line):
        parts = line.split()
        bracket_part = parts[0][1:-1]
        tuple_parts = parts[1:-1]
        tuples = []
        for part in tuple_parts:
            nums = part[1:-1].split(',')
            nums = [int(x) for x in nums if x]
            tuples.append(tuple(nums))
        return (bracket_part, tuples)

    parsed = [parse_line(line) for line in content]
    total = 0
    for goal, options in parsed:
        presses = fewest_presses(options, goal)
        total += presses
    print(total)

main()