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
    fresh_ranges.sort()
    new = []
    for l,r in fresh_ranges:
        if not new or l > new[-1][1] + 1:
            new.append([l,r])
        else:
            new[-1][1] = max(new[-1][1],r)
    count = sum(r-1+1 for l,r in new)
    print('count:', count)

if __name__ == "__main__":
    main()