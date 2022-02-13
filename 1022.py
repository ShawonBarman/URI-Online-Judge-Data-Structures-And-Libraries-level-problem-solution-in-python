def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())

while n != 0:
    n -= 1
    n1, x1, d1, op, n2, x2, d2 = input().split()
    n1, d1, n2, d2 = int(n1), int(d1), int(n2), int(d2)
    numerator, denumerator = 0, 0
    if op == "+":
        numerator = n1 * d2 + n2 * d1
        denumerator = d1 * d2
    elif op == "-":
        numerator = n1 * d2 - n2 * d1
        denumerator = d1 * d2
    elif op == "*":
        numerator = n1 * n2
        denumerator = d1 * d2
    elif op == "/":
        numerator = n1 * d2
        denumerator = n2 * d1

    ans1 = numerator/gcd(numerator, denumerator)
    ans2 = denumerator/gcd(numerator, denumerator)
    print(f"{numerator}/{denumerator} = {int(ans1)}/{int(ans2)}")