user_number = int(input())

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
