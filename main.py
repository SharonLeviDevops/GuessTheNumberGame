import random
class GuessTheNumber(object):
    count = 0
    def __init__(self):
        GuessTheNumber.count+=1
        self.number = random.randint(0,2)
        self.tries =0
    def __call__(self, *args, **kwargs):
        if (args[0] > self.number):
            print("Your number is bigger")
            self.tries +=1
            return False
        elif (args[0] < self.number):
            print("your number is lower")
            self.tries += 1
            return False
        else:
            print("Your WiN!!")
            return True
while True:
    game = GuessTheNumber()
    number = int(input("[+] Guess the number > "))
    while not game(number):
        number = int(input("[+] Guess the number > "))
    else:
        print("You win in {0} tries".format(game.tries))
        exit()
print("Game end in {0} tries".format(game.count))