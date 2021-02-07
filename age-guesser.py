print('Hello! My name is Chives.')
print('I was created in 2021.')
print("")
print("")
print('What is your name?:     ')

user_name = input()

print()
print()
print(f'What a great name you have, {user_name}!')
print()
print('Let me guess your age.')
print()
print('Enter remainders of dividing your age by 3, 5 and 7.')
print()
print()
print('Example:    30/3=10. There are no remainders')
print('            31/3=10+1 There is a remainder of 1')
print('            32/3=10+2 There is a remainder of 2')
print()
print()

# remainders
print('What is the remainder of dividing your age by 3?:')
remainder3 = int(input()) * 70
print('What is the remainder of dividing your age by 5?:')
remainder5 = int(input()) * 21
print('What is the remainder of dividing your age by 7?:')
remainder7 = int(input()) * 15

# age calculation
your_age = (remainder3 + remainder5 + remainder7) % 105

print(f"Your age is '{your_age}'; that's a good time to start programming!")
