# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint
# Write all of your part 2A code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

card_rank = randint(1, 13)
card_rank_2 = randint(1, 13)

if card_rank == 1:
  # A 1 stands for an ace.
  card_name = "Ace"
elif card_rank == 11:
  # An 11 stands for a jack.
  card_name = "Jack"
elif card_rank == 12:
  # A 12 stands for a queen.
  card_name = "Queen"
elif card_rank == 13:
  # A 13 stands for a king.
  card_name = "King"
else:
  # All other cards are named by their
  # number, or rank.
  card_name = str(card_rank)

if card_rank == 1 or card_rank == 8:
  drew_prefix = 'Drew an '
else:
  drew_prefix = 'Drew a '

if card_rank < 1 or card_rank > 13:
  print('BAD CARD')
else:
  print(drew_prefix + card_name)




if card_rank_2 == 1:
  # A 1 stands for an ace.
  card_name_2 = "Ace"
elif card_rank_2 == 11:
  # An 11 stands for a jack.
  card_name_2 = "Jack"
elif card_rank_2 == 12:
  # A 12 stands for a queen.
  card_name_2 = "Queen"
elif card_rank_2 == 13:
  # A 13 stands for a king.
  card_name_2 = "King"
else:
  # All other cards are named by their
  # number, or rank.
  card_name_2 = str(card_rank_2)

if card_rank_2 == 1 or card_rank_2 == 8:
  drew_prefix_2 = 'Drew an '
else:
  drew_prefix_2 = 'Drew a '

if card_rank_2 < 1 or card_rank_2 > 13:
  print('BAD CARD')
else:
  print(drew_prefix_2 + card_name_2)
  
if card_rank_2 == 11 or card_rank_2 == 12 or card_rank_2 == 13:
  # Jacks, Queens, and Kings are worth 10.
  card_value_2 = 10
elif card_rank_2 == 1:
  # Aces are worth 11.
  card_value_2 = 11
else:
  # All other cards are worth the same as
  # their rank.
  card_value_2 = card_rank_2

if card_rank_2 > 13 or card_rank_2 < 1:
  print('BAD CARD')
else:
  pass


if card_rank == 11 or card_rank == 12 or card_rank == 13:
  # Jacks, Queens, and Kings are worth 10.
  card_value = 10
elif card_rank == 1:
  # Aces are worth 11.
  card_value = 11
else:
  # All other cards are worth the same as
  # their rank.
  card_value = card_rank

if card_rank > 13 or card_rank < 1:
  print('BAD CARD')
else:
  pass

total_hand_after_two = card_value + card_value_2

if total_hand_after_two >= 4 and total_hand_after_two < 17:
  print(f"Dealer has {total_hand_after_two}.")
if total_hand_after_two == 21:
  print("Final hand: 21.")
  print('BLACKJACK!')
elif total_hand_after_two > 21 and total_hand_after_two <= 31:
  print(f"Final hand: {total_hand_after_two}.")
  print('BUST.')
elif total_hand_after_two > 31 or total_hand_after_two < 4:
  print('BAD HAND VALUE!')
elif total_hand_after_two >= 17 and total_hand_after_two < 21 :
  print(f'Final hand: {total_hand_after_two}.')


while total_hand_after_two >= 4 and total_hand_after_two < 17:

  card_rank = randint(1, 13)
  
  if card_rank == 1:
  # A 1 stands for an ace.
    card_name = "Ace"
  elif card_rank == 11:
  # An 11 stands for a jack.
    card_name = "Jack"
  elif card_rank == 12:
  # A 12 stands for a queen.
    card_name = "Queen"
  elif card_rank == 13:
  # A 13 stands for a king.
    card_name = "King"
  else:
  # All other cards are named by their
  # number, or rank.
    card_name = str(card_rank)

  if card_rank == 1 or card_rank == 8:
    drew_prefix = 'Drew an '
  else:
    drew_prefix = 'Drew a '

  

  if card_rank < 1 or card_rank > 13:
    print('BAD CARD')
  else:
    print(drew_prefix + card_name)

    if card_rank == 11 or card_rank == 12 or card_rank == 13:
  # Jacks, Queens, and Kings are worth 10.
      card_value = 10
    elif card_rank == 1:
  # Aces are worth 11.
      card_value = 11
    else:
  # All other cards are worth the same as
  # their rank.
      card_value = card_rank

    if card_rank > 13 or card_rank < 1:
      print('BAD CARD')
    else:
      pass

    total_hand_after_two += card_value

    if total_hand_after_two == 21:
      print("Final hand: 21.")
      print('BLACKJACK!')
    elif total_hand_after_two > 21 and total_hand_after_two <= 31:
      print(f"Final hand: {total_hand_after_two}.")
      print('BUST.')
    elif total_hand_after_two > 31 or total_hand_after_two < 4:
      print(f"Final hand: {total_hand_after_two}.")
      print('BAD HAND VALUE!')
    elif total_hand_after_two >= 17 and total_hand_after_two < 21 :
      print(f'Final hand: {total_hand_after_two}.')
    else: 
      print(f"Dealer has {total_hand_after_two}.")