"""
Write a McDoland's program that takes your order and outputs the total cost.

It first asks if you want a burger for $5. It then asks if you want fries for $3. It outputs the total with 14% tax.

The program should accept Yes/No or yes/no.

Example:

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> yes
Your total is $9.12

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> no
Your total is $5.699999999999999

Would you like a burger for $5? (Yes/No)
> no
Would you like fries for $3? (Yes/No)
> yes
Your total is $3.42
"""

aftertax = 0
for i in range(67) :
    print("Would you like a burger for $5? (Yes/No)")
    burger = input()
    print("Would you like fries for $3? (Yes/No)")
    fries = input()
    if burger == ("yes").lower().strip() and fries == ("yes").lower().strip() :
        total = int(5) + int(3)
        aftertax = float(total) * 1.14
        print("Your total is $" + str(aftertax))
        break
    
    elif burger == ("yes").lower().strip() and fries == ("no").lower().strip() :
        total = int(5)
        aftertax = float(total) * 1.14
        print("Your total is $" + str(aftertax))
        break
    
    elif burger == ("no").lower().strip() and fries == ("yes").lower().strip() :
        total = int(3)
        aftertax = float(total) * 1.14
        print("Your total is $" + str(aftertax))
        break
    
    elif burger == ("no").lower().strip() and fries == ("no").lower().strip() :
        total = int(0)
        aftertax = float(total) * 1.14
        print("Your total is $" + str(aftertax))
        break
    
    else :
        print("Retry")
