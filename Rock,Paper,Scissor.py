import random #importing the random module

# creating a function for the game
def playgame():
    
    # taking a random value for computer's turn using the random module
    comp=random.randint(1,3)
    # changing the random value to the available options - rock,paper and scissor
    if comp==1:
        comp="rock"
    elif comp==2:
        comp="paper"
    elif comp==3:
        comp="scissor"
    # info for users input
    print("Choose rock(r), paper(p) or scissor(s)")
    # taking user's input
    user=input("Your turn :")
    # analyzing user's input
    if (user=="r"):
        user="rock"
    elif (user=="p"):
        user="paper"
    elif(user=="s"):
        user="scissor"

    # All the scenarios if the computer chooses rock
    if comp=="rock":
        if user=="rock":
            result="It's a Tie"
        elif user=="scissor":
            result="You Lose..."
        elif user=="paper":
            result="You Won!"
    
    # All the scenarios if the computer chooses paper
    elif comp=="paper":
        if user=="paper":
            result="It's a Tie"
        elif user=="rock":
            result="You Lose..."
        elif user=="scissor":
            result="You Won!"
    
    # All the scenarios if the computer chooses scissor
    elif comp=="scissor":
        if user=="scissor":
            result="It's a Tie"
        elif user=="rock":
            result="You Won!"
        elif user=="paper":
            result="You Lose..."
    
    # displaying computer and user's choosed option
    print("Comp:",comp)
    print("You:",user)
    
    # displaying the final result
    print(result)

# finally calling the function
playgame()