"""
Write an Age in 2049 program that asks your age and outputs how old you'll be 31 years from now.

Examples:

How old are you?
> 10
In 2056, you will be 41 years old!
--
How old are you?
> 25
In 2056, you will be 56 years old!
"""

print("How old are you?")
age = input()
year = int(2025) - int(age)
final = int(2049) - int(year)

print("In 2056, you will be " + str(final) + " years old!")