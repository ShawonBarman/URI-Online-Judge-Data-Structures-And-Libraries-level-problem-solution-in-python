n = int(input())
while n != 0:
    n -= 1
    m = int(input())
    m_dic = {}
    while m != 0:
        m -= 1
        name, price = input().split()
        m_dic[name] = float(price)

    p = int(input())
    p_dic = {}
    while p != 0:
        p -= 1
        name, value = input().split()
        p_dic[name] = int(value)

    ans = 0
    for x,y in p_dic.items():
        ans += (m_dic[x]*y)

    print("R$ {:.2f}".format(ans))