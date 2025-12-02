def dial(rotations):
    dial = 50
    password = 0
    for rotation in rotations:
        steps = int(rotation[1:])
        if rotation[0] == "R":
            password += (dial + steps) // 100
            dial = (dial + steps) % 100
        elif rotation[0] == "L":
            steps = steps % 100
            if steps > dial:
                password += 1 + (steps - dial - 1) // 100
            dial = (dial - steps) % 100

    return password

def main():
    with open("puzzleinputexample.txt") as f:
        instructions = [line.strip() for line in f if line.strip()]
    password = dial(instructions)
    print("password (part 2):", password)

if __name__ == "__main__":
    main()
