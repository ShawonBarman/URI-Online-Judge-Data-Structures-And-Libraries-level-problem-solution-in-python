n = int(input())
while n > 0:
    n -= 1
    l = int(input())
    order = list(map(int, input().split()))

    swap = 0
    for i in range(l):
        for j in range(i + 1, l):
            if (order[i] > order[j]):
                temp = order[i]
                order[i] = order[j]
                order[j] = order[i]
                swap += 1

    print('Optimal train swapping takes %d swaps.' % swap)