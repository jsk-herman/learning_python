# This script finds your birthday in MMDDYY format among the digits of pi.
# Actually, the script accepts any numerical string as long as it is 6 digits long.
# So you can probably use any 6-digit combination with it.

file = open('pi_1m.txt', 'r')
pi_1m = file.read()
birthday = input("What is your birthday in the MMDDYY format? ")
try:
    int(birthday)
    length = len(birthday)
except:
    print("Please input your birthday according to the format and try again.\n")
if length ==  6:
    pos = int(pi_1m.find(birthday))
    if pos > 0:
        print("Your birthday was first found at digit " + str(pos) + " of pi.\n")
    else:
        print("Your birthday was not found in the first million digits of pi.\n")
else:
    print("Please input your birthday according to the format and try again.\n")