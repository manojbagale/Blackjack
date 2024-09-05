user_hand_value = int(input())
if user_hand_value == 21:
    print("BLACKJACK!")
elif user_hand_value < 4 or user_hand_value > 31:
    print("BAD HAND VALUE!")
elif user_hand_value >= 4 and user_hand_value <= 20: 
    pass
elif user_hand_value >= 22 and user_hand_value <=31:
    print("BUST.")