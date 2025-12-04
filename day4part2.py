# printing department
def is_accessible(matrix,row,col):
    if matrix[row][col] != '@':
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    rolls = 0
    directions = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1), (0,1),
        (1,-1), (1,0), (1,1)
    ]
    for d1,d2 in directions:
        new_row, new_col = row + d1, col + d2
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if matrix[new_row][new_col] == '@':
                rolls +=1
    return rolls < 4 

def forklift_count(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if is_accessible(matrix,row,col) is True:
                count += 1
    return count

def remover(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    pend = []
    for row in range(rows):
        for col in range(cols):
            if is_accessible(matrix, row, col):
                pend.append((row, col))
    for (row, col) in pend:
        matrix[row][col] = 'x'
    return len(pend)
        
def removed_count(matrix):
    count = 0
    while True:
        removed= remover(matrix)
        if removed == 0:
            break
        count += removed
    return count
        
def main():
    with open("input4.txt") as f:
        lines = f.read().splitlines()
    matrix = [list(line) for line in lines]
    print('count:', removed_count(matrix))
    
if __name__ == "__main__":
    main()

    
            