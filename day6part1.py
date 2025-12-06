def main():
    with open("input6example.txt") as f:
        content = f.read()
    rows = [line.split() for line in content.splitlines()]
    results = []
    for i in range(len(rows[0])):
        operation = rows[len(rows) - 1][i]
        if operation == '*':
            result = 1
            for j in range(len(rows)-1):
                result *= int(rows[j][i])
        elif operation == '+':
            result = 0
            for j in range(len(rows)-1):
                result += int(rows[j][i])
        results.append(result)
    print('sum:',sum(results)) 
            
if __name__ == "__main__":
    main()