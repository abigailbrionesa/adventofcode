from collections import Counter

def generate_pairs(points):
    edges = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = points[i]
            x2, y2, z2 = points[j]
            euc = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            edges.append((euc, i, j))
    return edges

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, size, parent):
    x_root = find(x, parent)
    y_root = find(y, parent)
    if x_root == y_root:
        return False
    if size[x_root] < size[y_root]:
        x_root, y_root = y_root, x_root
    parent[y_root] = x_root
    size[x_root] += size[y_root]
    return True

def main():
    with open("input8.txt") as f:
        data = f.read()
    points = [tuple(map(int, line.split(','))) for line in data.strip().splitlines()]
    edges = generate_pairs(points)
    edges.sort()
    n = len(points)
    parent = list(range(n))
    size = [1] * n
    max_connections = 1000 
    count = 0
    for dist, i, j in edges:
        union(i, j, size, parent)
        count += 1
        if len(circuit_count) == 1:
            break
        for i in range(n):
            find(i, parent)

    circuit_count = Counter(find(i, parent) for i in range(n))
    largest_sizes = sorted(circuit_count.values(), reverse=True)

    result = 1
    for s in largest_sizes[:3]:
        result *= s

    print("sizes:", largest_sizes)
    print("result:", result)

if __name__ == "__main__":
    main()
