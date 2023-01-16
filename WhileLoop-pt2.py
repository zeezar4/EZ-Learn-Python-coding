# In this section we will go over break and continue statements
# I will be using a different numbers and variables in this
# please go back to part one if you are confused.

n = 27

while n < 50:
    print (n)
    if n == 48:
      break
    n += 1

# Alright that is allot more new things goin on there so lets break it down to human speak
# the while loop has a new varable name and numbers to work with but is the same as part 1
# we are now incorporating an "if" condition and "break statement"
# the if condition in human speech translates to 
# "If n(27) becomes equal to 48"
# and thats it! What comes next is the action to take "if" the conditions are met
# in this case its "break" where the loop will stop once the number meets 48
# this should result in a print out of the number 27-48


# Next lets look at Continue statements

x = 2

while x < 22:
    x += 2
    if x == 16:
        continue
    print (x)

"""
So not much looks different but the if statement has changed its action when conditions are ment
instead of taking a break once we reach 16 the loop will just skip 16
this results in a steing of numbers increasing by 2 starting from the number 2
BUT it will notably exclude the number 16 in the outputs
"""

"""
lets finish up with else statements

Else in human terms can roughtly mean "unless" or in better terms "or else"
this is basically what happens when you have met the conditions of the loop or function
and provides an alternate pathway

"""


f = 34
while f < 104:
    print(f)
    f *= 1.5 
else:
    print ("we have reached the last number in this math sequence without going over 104")

# try messing with any ofg the loops above to see different outcomes
# also try to comment out the loops to see them work individually
# for best results copy the loops individually into a compiler.
