def larg_area(input):
    max_a = 0
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            x1, y1 = input[i]
            x2, y2 = input[j]
            if x1 != x2 and y1 != y2:
                x_dist = abs(x1 - x2) + 1
                y_dist = abs(y1 - y2) + 1
                area = x_dist * y_dist
                max_a = max(max_a, area)
    return max_a

def main():
    with open("input9example.txt") as f:
        data = f.read()
    points = [tuple(map(int, line.split(','))) for line in data.strip().splitlines()]
    print(larg_area(points))

if __name__ == "__main__":
    main()
