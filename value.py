user_number = int(input())
if user_number == 1:
    print(f"Your hand value is 11.")
elif user_number>= 2 and user_number<= 10:
    card_value = user_number
    print(f"Your hand value is {card_value}.")
elif user_number == 11 or user_number == 12 or user_number == 13:
    print(f"Your hand value is 10.")
else:
    print("BAD CARD")
    #fdgdfg
    