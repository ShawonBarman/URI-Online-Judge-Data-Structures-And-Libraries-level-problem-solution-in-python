while True:
    n = int(input())
    if n == 0:
        break

    cards = []
    for i in range(n):
        cards.append(i + 1)

    discarded_cards = []
    while len(cards) > 1:
        x = cards.pop(0)
        y = cards.pop(0)
        discarded_cards.append(x)
        cards.append(y)
    print("Discarded cards:", end="")
    for x in discarded_cards:
        print("",x,end="")
    print()
    print("Remaining card:", cards[0])