n = int(input())
odd = []
even = []
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

even.sort()
odd.sort(reverse=True)
for x in even:
    print(x)
for x in odd:
    print(x)