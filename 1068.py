while True:
    try:
        n = input()
        myList = []
        for x in n:
            if x == '(':
                myList.append('(')
            elif x == ")":
                if myList == []:
                    myList.append(")")
                else:
                    myList.pop()
        if myList == []:
            print('correct')
        else:
            print('incorrect')

    except EOFError:
        break