# This is a breakdown for while loops, it is for my understanding
# but its free fro anyone to use if it helps understand coding better

# First assign a variable to use in your while loop 
# this will be the starting number that the loop will reference too
# lets make the variable 2 equal to ANUM (any number)

ANUM = 2

# next we set up the while loop

while ANUM < 5:
    print (ANUM)
    ANUM +=1

# To start we type "while"  then we instert our variable for 4
# then we say that ANUM (2) is less than 5, setting up the conditons for the loop
# In human 
# speak we are saying "run this function in a loop as long as the number is less than 5 and we are going to start at the number 2"
# next we want the functon to print out the resulting number of the loop everytime
# and ANUM += 1 in human speak basically translates to
# "keep adding plus one to ANUM"

# the opposite can be achived by switching arround a few things to count down from 5

ANUM2 = 5

while ANUM2 > 2:
    print (ANUM2)
    ANUM2 -=1

# this new loop changes the variable to ANUM2 and has it equal to 5
# The loop setup now translates to human as 
# "run the loop as long as ANUM2 is greater than 2"
# the += has now been changed to -= so that is subracts instead of adds
# in human speak that translates to 
# keep subtracting one from ANUM2"

# the output for both of these should be 234543 in decending order


