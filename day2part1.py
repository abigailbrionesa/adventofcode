# gift shop

def is_invalid(input):
    str_input = str(input)
    n = len(str_input)
    left = str_input[:(n//2)]
    right = str_input[(n//2):n]
    if left[0] == '0':
        return False
    return left == right

print(is_invalid(1188511885))
