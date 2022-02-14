i = 0
while True:
    n, q = map(int, input().split())

    if n == 0 and q == 0:
        break

    marble_numbers = []
    while n>0:
        n -= 1
        num = int(input())
        marble_numbers.append(num)
    marble_numbers.sort()

    i += 1
    print(f"CASE# {i}:")
    while q > 0:
        q -= 1
        qy = int(input())
        if qy in marble_numbers:
            print(f"{qy} found at {marble_numbers.index(qy) + 1}")
        else:
            print(f"{qy} not found")