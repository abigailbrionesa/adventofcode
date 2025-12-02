#secret entrance
def dial(inputs):
    password = 0
    dial_num = 50
    for instruction in inputs:
        if instruction[0] == 'L':
            dial_num = (dial_num - int(instruction[1:])) % 100
        elif instruction[0] == 'R':
            dial_num = (dial_num + int(instruction[1:])) % 100

        if dial_num == 0:
            password += 1

    return password

def main():
    with open("puzzleinput.txt", "r") as f:
        instructions = [line.strip() for line in f if line.strip()]
    print("password:", dial(instructions))

main()