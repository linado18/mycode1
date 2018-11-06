#!/usr/bin/env python3

message = input('please enter your score: ')

print('This is the score you enter '+ message)

grade = float(message)

if grade >= 90:
    message = message + 'This is Grade A '
elif grade >= 80:
    message = message + 'This is Grade B '
elif grade >= 70:
    message = message + 'This is Grade C '
elif grade>=60:
    message = message+ 'This is grade D '
else:
    message = message + 'This is Grade F '
print(message)
