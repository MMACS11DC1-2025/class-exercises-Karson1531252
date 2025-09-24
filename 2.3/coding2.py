"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""

print("This is an Olympic Judging program that ooutputs the average scores from 5 different judges. Please input the first judge's score out of 10:")
j1 = input()
print("Please input the second judge's score")
j2 = input()
print("Please input the third judge's score")
j3 = input()
print("Please input the forth judge's score")
j4 = input()
print("Please input the fifth judge's score")
j5 = input()

total = float(j1) + float(j2) + float(j3) + float(j4) + float(j5)
final = int(total) / 5

print("Your Olympic score is " + str(final))



