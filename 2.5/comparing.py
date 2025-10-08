"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
# Algorithm:
# 1 Load data from file.
# 2 Count "Dog" and "Cat" in data.
# 3 Ask user which count to show.
# 4 Show count with basic observations.
# 5 Compare counts and print result.
# 6 Allow up to 67 tries for valid input.

print("What is your name?")
name = input()

print("Hi " + name + "! Do you want to know how many people like dogs or cats?")

# Read the data file
file = open("2.4/responses.csv")
data = file.read()
file.close()

# Count dogs and cats
dog_count = data.count("Dog")
cat_count = data.count("Cat")

# Functionality previously in observations()
def show_observations(animal, count):
    print("There are " + str(count) + " people that like " + animal + "s.")
    if count > 14:
        print("More than half the class likes " + animal + "s.")
    elif count == 0:
        print("Nobody likes " + animal + "s.")
    else:
        print("Only a few people like " + animal + "s.")

# Input loop - up to 67 tries
for i in range(67):
    answer = input("Type 'dogs' or 'cats': ").strip().lower()
    if answer == "cats":
        print("Okay, let's see!")
        print("There are " + str(cat_count) + " people that like cats.")
        if cat_count > 14:
            print("More than half the class likes cats.")
        elif cat_count == 0:
            print("Nobody likes cats.")
        else:
            print("Only a few people like cats.")
        break
    elif answer == "dogs":
        print("Okay, let's see!")
        print("There are " + str(dog_count) + " people that like dogs.")
        if dog_count > 14:
            print("More than half the class likes dogs.")
        elif dog_count == 0:
            print("Nobody likes dogs.")
        else:
            print("Only a few people like dogs.")
        break
    else:
        print("Please type 'dogs' or 'cats'.")
else:
    print("Too many invalid attempts. Try again later.")
    exit()

# Difference and comparison
diff = cat_count - dog_count
if diff < 0:
    diff = -diff

if diff > 5:
    print("Difference of " + str(diff) + ".")
else:
    print("Counts are close, mixed preferences.")

if dog_count > cat_count:
    print("More people like dogs.")
elif dog_count < cat_count:
    print("More people like cats.")
else:
    print("Equal number like dogs and cats.")

# Testing:
# - Input tested with valid and invalid answers.
# - Observations correct for different counts.
# - Comparison works in all cases.
