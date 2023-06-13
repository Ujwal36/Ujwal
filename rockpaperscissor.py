mapp = {"r":"s","p":"r","s":"p"}
import random
# r --> s
# p --> r
# s --> p

#computer moves are randomly generated
while True:
    playagain = input("Play again???? Type  y/n")
    if playagain not in ['y','Y']:
        break    
    llist = list(mapp.keys())
    print(llist)
    computermove = random.choice(llist)

    while True:
        playermove  = input("Enter r, p or s")
        if playermove.lower() not in mapp.keys():

            playermove  = input("Wrong input!! Enter r, p or s")
        break
    print("computer move is:", " ", computermove )

    if playermove == computermove:
        print("Its a Tie!!")

    elif mapp.get(playermove) == computermove:
        print("You won")

    else:
        print("You lost!!!!")




