# This program says hello and asks for my name.

print('JSK : Hello World!')
print('JSK : What is your name?')     # ask for their name
myName = input('ME  : ')
print('\nJSK : It is nice to meet you, ' + myName + '!')
print('JSK : The length of your name is ' + str(len(myName)))

print('\nJSK : What is your age?')      # ask for their age
myAge = input('ME  : ')
print('JSK : You will be ' + str(int(myAge) + 1) + ' in a year.' )
print()