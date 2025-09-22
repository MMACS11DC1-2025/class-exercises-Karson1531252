"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""

"""
Happiness calculator
Author: Karson Lum
Date : Sept 22, 2025
"""

print("Hello i am a calc that can calculate your happiness. Are you happy? Answer with yes, no, or maybe for every question\n")
answer1 = input()
happiness = 3
for i in range(1) :
    if answer1 == ("yes").lower().strip() :
        print("Great \n")
        happiness = happiness + 1
        break
    
    elif answer1 == ("no").lower().strip() :
        print("Turn that frown upside down \n")
        happiness = happiness - 1
        break
    
    elif answer1 == ("maybe").lower().strip() :
        print("Atleast u arent sad \n")
        happiness = happiness + 0
        break
    
    else:
        print("Skipping question im assuming you aren't \n")
        break
    
print("Now do you like dogs or cats?\n")
answer2 = input()
for i in range(1) :
    if answer2 == ("yes").lower().strip() :
        print("Same")
        happiness = happiness + 1
        break
    
    elif answer2 == ("no").lower().strip() :
        print("You probably like rats")
        happiness = happiness - 1
        break
    
    elif answer2 == ("maybe").lower().strip() :
        print("unless you are allergic there is no excuse")
        happiness = happiness + 0
        break
    
    else:
        print("Skipping question im assuming you don't \n")
        happiness = happiness - 1
        break
    
print("Last question, do you like ice cream on a hot sunny day?\n")
answer3 = input()
for i in range(1) :
    if answer3 == ("yes").lower().strip() :
        print("That's great")
        happiness = happiness + 1
        break
    
    elif answer3 == ("no").lower().strip() :
        print("You dont deserve ice cream on any day")
        happiness = happiness - 1
        break
    
    elif answer3 == ("maybe").lower().strip() :
        print("You should")
        happiness = happiness + 0
        break
    
    else:
        print("Skipping question im assuming you don't \n")
        happiness = happiness - 1
        break
    
print("TIME TO CALCULATE...\n")

print(happiness/6 *100)
print("% is your happiness level.")
