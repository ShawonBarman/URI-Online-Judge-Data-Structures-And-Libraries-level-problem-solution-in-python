n = int(input())
check = 0
while n != 0:
    n -= 1
    if check == 1:
        print()
    m, c = map(int, input().split())
    hash = {str(x): [] for x in range(m)}
    arr_c = list(map(int, input().split()))[:c]
    for x in arr_c:
        remainder = x % m
        hash[str(remainder)].append(int(x))

    for x in hash:
        print(f"{x} -> ",end="")
        for y in hash[x]:
            print(f"{y} -> ",end="")
        print('\\')

    check = 1