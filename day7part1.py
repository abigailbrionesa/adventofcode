from collections import deque

def find_s(grid):
    for i,c in enumerate(grid[0]):
        if c == 'S':
            return i
    return None

def count_splitting(grid):
    w = len(grid[0])
    h = len(grid)
    start_x = find_s(grid)
    visited = set()
    count = 0
    queue = deque()
    queue.append((0,start_x))
    
    while queue:
        row,col = queue.popleft()
        #bound check
        if row >= h or col < 0 or col >= w:
            continue
        #not re processing
        if (row,col) in visited:
            continue
        visited.add((row,col))
        c = grid[row][col]
        if c == '^':
            count +=1
            queue.append((row+1, col-1))
            queue.append((row+1, col+1))
        else:
            queue.append((row+1, col))
    return count

def main():
    with open("input7.txt") as f:
        grid = f.read().splitlines()
        grid = [list(line) for line in grid]
        count = count_splitting(grid)
        print('count:', count)


if __name__ == "__main__":
    main()
