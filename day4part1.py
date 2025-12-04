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
        
def main():
    with open("input4example.txt") as f:
        lines = f.read().splitlines()
    matrix = [list(line) for line in lines]
    print('count:', forklift_count(matrix))
    
if __name__ == "__main__":
    main()

    
            