# gift shop

def is_invalid(input):
    str_input = str(input)
    n = len(str_input)
    mid = n//2
    if n % 2 == 1:
        left  = str_input[:mid]
        right = str_input[mid+1:]
    else:
        left  = str_input[:mid]
        right = str_input[mid:]
    if not left or not right:
        return False
    if left[0] == '0' or right[0] == '0':
        return False
    return left == right

def invalid_count(input):
    count = 0
    for id in input:
        if is_invalid(id):
            count +=1
    return count
    
def main():
    with open("input2.txt") as f:
        line = f.read().strip()
    ids = []
    for group in line.split(','):
        a,b = group.split('-')
        for ids_range in range(int(a), int(b)+1):
            ids.append(ids_range)
    result = sum(is_invalid(id) for id in ids)
    print("invalid count:", result)

if __name__ == "__main__":
    main()
