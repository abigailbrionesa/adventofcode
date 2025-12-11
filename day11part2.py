def main():
    with open('input11.txt') as f:
        content = f.read().splitlines()

    graph = {}
    for line in content:
        if not line.strip():
            continue
        left, right = line.split(":")
        node = left.strip()
        outputs = right.strip().split()
        graph[node] = outputs

    to_find_nodes = {'dac', 'fft'}

    memo = {}

    def dfs(node, seen):
        key = (node, frozenset(seen)) #unique key for memoization
        if key in memo: #if already computed
            return memo[key]

        if node in to_find_nodes:
            seen = seen | {node} 

        if node == 'out':
            result = 1 if seen == to_find_nodes else 0
            memo[key] = result
            return result

        total = 0
        for next_node in graph.get(node, []):
            total += dfs(next_node, seen) #recursively explored each

        memo[key] = total
        return total

    count = dfs('svr', set()) #start dfs from svr bc the elves start there
    print(f"n paths:", count) #number of paths with the special nodes

main()
