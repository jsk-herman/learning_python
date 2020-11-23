# This script finds your birthday in MMDDYY format among the digits of pi.
# Actually, the script accepts any numerical string as long as it is 6 digits long.
# So you can probably use any 6-digit combination with it.

file = open('pi_1m.txt', 'r')                                                            # Opens the file containing the number pi
pi_1m = file.read()                                                                      # Reads the file and stores the string to a variable
birthday = input("What is your birthday in the MMDDYY format? ")                         # Asks for the user for their birthday in MMDDYY format
try:
    int(birthday)                                                                        # Checks to see if the input is a numerical string
    length = len(birthday)                                                               # Determines the length of the string
except:
    print("Please input your birthday according to the format and try again.\n")         # Outputs an error message if the input is not according to the format because it failed the int() test
if length ==  6:                                                                         # Checks to see if the input is 6 digits long.
    pos = int(pi_1m.find(birthday))                                                      # Finds the 6-digit combination in pi using the find() method
    if pos > 0:
        print("Your birthday was first found at digit " + str(pos) + " of pi.\n")        # If pos is not -1 then print a message of the 6-digit comnbination's position in pi
    else:
        print("Your birthday was not found in the first million digits of pi.\n")        # If pos is -1 then print an error message saying it was not found.
else:
    print("Please input your birthday according to the format and try again.\n")         # If the input is not 6 digits long just like the format then print an error message.