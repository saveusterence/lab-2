import random
dealer = []
player = []
def main():
    name = start()
    hits = 0
    hos = 0
    print(f"Welcome {name}.")
    for x in range(2):
        draw(dealer)
        draw(player)
    print(f"The dealer shows {dealer[0]}")
    for x in range(len(player)):
        print(f"Your cards are {player[x]}")
    while hits < 3 and hos != 'S':
        hos = input(f"{name} would you like to hit(H) or stand(S)").upper()
        hits += 1
        match hos:
            case 'H':
                draw(player)
                print("You drew a ", player[hits+1])
                print(player)
            case 'S':
                print("The dealers second card is ",dealer[1])
            case _:
                print("Error")
    i =1
    while (count(dealer) < 16):
        i +=1
        draw(dealer)
        print("Dealer drew ",dealer[i])
    if (count(dealer) == 1):
        print("Dealer has 21.")
    elif (count(player) == 1):
        print(f"{name} has 21.")
    elif (count(dealer) >21):
        print("Dealer bust")
    elif (count(player) > 21):
        print("player bust")
    elif (count(dealer) >= count(player)):
        print("Dealer wins.")
    else:
        print(f"{name} wins.")

def count(user):
    total =0
    for x in range(len(user)):
        total += user[x]
    if total == 21:
        return 1
    elif total > 21:
        return total
    else:
        return total
    
def start():
    name = input("Please enter your name: ")
    return name
def cards():
    x = random.randint(1,11)
    return x
def draw(user):
    card = cards()
    #if card == 1 or card == 11:
        #card = "Ace"
    user.append(card)
    return



if __name__ == "__main__":
    main()