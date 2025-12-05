#cafeteria

def create_fresh_lst(lst_ranges):
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
    fresh_ranges = create_fresh_lst(lst1)
    fresh_set = set()
    for l,r in fresh_ranges:
        for i in range(l,r+1):
            fresh_set.add(i)
    print(len(fresh_set))

if __name__ == "__main__":
    main()