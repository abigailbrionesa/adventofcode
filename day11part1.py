
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
        
    memo = {}
    
    def dfs(node):
        if node == 'out':
            return 1
        if node == 'dac' or node == 'fft':
            print('found!')
        if node in memo:
            return memo[node]
        total = 0
        for next in graph[node]:
            total += dfs(next)
        memo[node] = total
        return total

    result = dfs('you')
    print(f"n paths:", result)

    
    
main()

    