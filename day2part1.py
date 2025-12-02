# gift shop

def is_valid(input):
    n = len(str(input))
    left = str(input)[:(n//2)-1]
    right = str(input)[(n//2)+1:n]
    return not left == right

print(is_valid(1188511885))
