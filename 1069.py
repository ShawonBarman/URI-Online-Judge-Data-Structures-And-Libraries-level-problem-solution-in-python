n = int(input())
for i in range(n):
    text = input()
    myList = []
    ans = 0
    for x in text:
        if x == '<':
            myList.append('<')
        elif x == ">":
            if myList == []:
                continue
            else:
                myList.pop()
                ans += 1
    print(ans)