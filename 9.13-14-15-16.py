import random

class Die:
    """Dice Class"""
    def __init__(self, sides = 6):
        self.sides = sides

    def rolldie(self):
        print(random.randint(1, self.sides))

    def rollmulti(self, times):
        self.times = times
        rolls = 0
        while rolls < times:
            self.rolldie()
            rolls = rolls + 1


lottolist = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e']
def lotto():
    pos1 = lottolist[random.randint(0, 14)]
    pos2 = lottolist[random.randint(0, 14)]
    pos3 = lottolist[random.randint(0, 14)]
    pos4 = lottolist[random.randint(0, 14)]
    lottowin = pos1+pos2+pos3+pos4
    print(f"The winning ticket is is {lottowin}")
    return lottowin

def lottogen():
    pos1 = lottolist[random.randint(0, 14)]
    pos2 = lottolist[random.randint(0, 14)]
    pos3 = lottolist[random.randint(0, 14)]
    pos4 = lottolist[random.randint(0, 14)]
    lottowin = pos1+pos2+pos3+pos4
    return lottowin

def runlotto(rigged = 0):
    ticket = lottogen()
    count = 0
    win = 0
    while win == 0:
        current_winner = lotto()
        if rigged == 1:
            current_winner = ticket
        if current_winner == ticket:
            print("You won!")
            win = 1
            print(f"It took {count} tries!")
        else:
            print("Better luck next time!")
            count = count + 1
            print(count)
            print(ticket)



print("Dice")
dye = Die()
dye.rollmulti(3)

print()

d10 = Die(10)
d10.rollmulti(3)

print()

d20 = Die(20)
d20.rollmulti(3)

print("Lotto")
runlotto()

#9.16
#yeet