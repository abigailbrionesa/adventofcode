def dial(inputs):
    dial = 50
    password = 0
    for instruction in inputs:
        steps = int(instruction[1:])
        if instruction[0] == "R":
            for _ in range(steps):
                dial = (dial + 1) % 100
                if dial == 0:
                    password += 1
        elif instruction[0] == "L":
            for _ in range(steps):
                dial = (dial - 1) % 100
                if dial == 0:
                    password += 1
    return password

def main():
    with open("puzzleinput.txt") as f:
        instructions = [line.strip() for line in f if line.strip()]
    password = dial(instructions)
    print("password (part 2):", password)

if __name__ == "__main__":
    main()
