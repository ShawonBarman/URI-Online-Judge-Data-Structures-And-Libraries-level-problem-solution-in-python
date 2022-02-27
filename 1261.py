m, n = map(int, input().split())
hay_point_dic = {}

while m != 0:
    m -= 1
    word, value = input().split()
    hay_point_dic[word] = int(value)

while n != 0:
    n -= 1
    description = input().split()
    dot = input()
    ans = 0
    for x in description:
        try:
            ans += hay_point_dic[x]
        except KeyError:
            continue

    print(ans)