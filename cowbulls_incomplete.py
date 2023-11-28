import random

def compare_numbers(number, user_guess):
    ## your code here
    x=[]
    y=[]
    for a in number:
        y.append(int(a))
    cowcount=0
    bullcount=0
    for i in user_guess:
        x.append(int(i))
    for j in x:
        if str(j) in str(number):
            cowcount+=1
    for b in range(0,4):
        if x[b]==y[b]:
            bullcount+=1
    cowbull=[str(cowcount),str(bullcount)]
    return cowbull

playing = True #gotta play the game
number = str(random.randint(1000,9999)) #random 4 digit number, changed 0 to 1000
guesses = 0
 #removed "print (number)"

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!") #removed raw_
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")