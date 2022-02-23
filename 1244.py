n = int(input())
for i in range(n):
    set_string = input().split()
    #print(set_string)
    ans = ""
    l = len(set_string)
    for j in range(l):
        maxi = -99999
        string_v = ""
        for x in set_string:
            if len(x) > maxi:
                maxi = len(x)
                string_v = x
        set_string.pop(set_string.index(string_v))
        ans += string_v + " "
    ans = ans.rstrip()
    print(ans)