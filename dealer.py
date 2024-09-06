# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint
# Write all of your part 2A code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
user_number = randint(1, 13)
if user_number == 1:
    print("Drew an Ace")
elif user_number>= 2 and user_number<= 10 and not user_number == 8:
    print(f"Drew a {user_number}")
elif user_number == 8:
    print(f"Drew an 8")
elif user_number == 11:
    print("Drew a Jack")
elif user_number == 12:
    print("Drew a Queen")
elif user_number == 13:
    print("Drew a King")
else:
    print("BAD CARD")