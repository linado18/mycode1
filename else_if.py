#! /usr/bin/env/ python3

Monty=input("Please seclect one of this name:  Tom and Jerry, Gone with the Wind, Lord of the Ring \n")
print("The movie you select is: " + Monty)
if Monty == 'Tom and Jerry':
    print("Correct")
elif Monty == 'Gone with the Wind':
    print("Sorry, try again!")
elif Monty == 'Lord of the Ring':
    print("Sorry, try again!")
else:
    print("Sorry, the answer was Tom and Jerry")