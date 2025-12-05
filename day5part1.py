#cafeteria

def create_fresh_set(lst_ranges):
    fresh_ranges = []
    for range in lst_ranges:
        l,r = map(int, range.split('-'))
        fresh_ranges.append((l, r))
    return fresh_ranges

def main():
    with open("input5.txt") as f:
        content = f.read().strip()
    lst1,lst2 = content.split("\n\n")
    lst1 = lst1.splitlines()
    lst2 = lst2.splitlines()
    fresh_ranges = create_fresh_set(lst1)
    count = 0
    for id in lst2:
        id = int(id)
        for l,r in fresh_ranges:
            if l <= id <= r:
                count += 1
                break
    print('count:', count)

if __name__ == "__main__":
    main()

    