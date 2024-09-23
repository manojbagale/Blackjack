 DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint
# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# The user's starting hand has 2 cards.
print('-----------')
print('YOUR TURN')
print('-----------')

# A starting hand has two cards.
card_rank = randint(1, 13)
if card_rank == 1:
  # A 1 stands for an ace.
  card_name = 'Ace'
elif card_rank == 11:
  # An 11 stands for a jack.
  card_name = 'Jack'
elif card_rank == 12:
  # A 12 stands for a queen.
  card_name = 'Queen'
elif card_rank == 13:
  # A 13 stands for a king.
  card_name = 'King'
else:
  # All other cards are named by their
  # number, or rank.
  card_name = card_rank

if card_rank == 1 or card_rank == 8:
    print('Drew an ' + str(card_name))
else:
    print('Drew a ' + str(card_name))

if card_rank == 11 or card_rank == 12 or card_rank == 13:
  # Jacks, Queens, and Kings are worth 10.
  card1_value = 10
elif card_rank == 1:
  # Aces are worth 11.
  card1_value = 11
else:
  # All other cards are worth the same as
  # their rank.
  card1_value = card_rank

card_rank = randint(1, 13)
if card_rank == 1:
  # A 1 stands for an ace.
  card_name = 'Ace'
elif card_rank == 11:
  # An 11 stands for a jack.
  card_name = 'Jack'
elif card_rank == 12:
  # A 12 stands for a queen.
  card_name = 'Queen'
elif card_rank == 13:
  # A 13 stands for a king.
  card_name = 'King'
else:
  # All other cards are named by their
  # number, or rank.
  card_name = card_rank

if card_rank == 1 or card_rank == 8:
    print('Drew an ' + str(card_name))
else:
    print('Drew a ' + str(card_name))

if card_rank == 11 or card_rank == 12 or card_rank == 13:
  # Jacks, Queens, and Kings are worth 10.
  card2_value = 10
elif card_rank == 1:
  # Aces are worth 11.
  card2_value = 11
else:
  # All other cards are worth the same as
  # their rank.
  card2_value = card_rank

user_hand = card1_value + card2_value

# The user has the option to keep drawing if their hand is below 21.
while user_hand < 21:
  should_hit = input('You have ' + str(user_hand) + ". Hit (y/n)? ")
  if should_hit == 'n':
    break
  elif should_hit == 'y':
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
        print('Drew an ' + card_name)
    else:
        print('Drew a ' + card_name)

    if card_rank == 11 or card_rank == 12 or card_rank == 13:
        # Jacks, Queens, and Kings are worth 10.
        card_value = 10
    elif card_rank == 1:
        # Aces are worth 11.
        card_value = 11
    else:
        # All other cards are worth the same as their rank.
        card_value = card_rank

    user_hand = user_hand + card_value
  else:
    print("Sorry I didn't get that.")

print('Final hand: ' + str(user_hand) + '.')
if user_hand == 21:
  print('BLACKJACK!')
elif user_hand > 21:
  # The user busts - or immediately loses - if
  # their hand total goes above 21.
  print('BUST.')

# The dealer's starting hand has 2 cards.
print('-----------')
print('DEALER TURN')
print('-----------')

card_rank = randint(1, 13)
if card_rank == 1:
  # A 1 stands for an ace.
  card_name = 'Ace'
elif card_rank == 11:
  # An 11 stands for a jack.
  card_name = 'Jack'
elif card_rank == 12:
  # A 12 stands for a queen.
  card_name = 'Queen'
elif card_rank == 13:
  # A 13 stands for a king.
  card_name = 'King'
else:
  # All other cards are named by their
  # number, or rank.
  card_name = card_rank

if card_rank == 1 or card_rank == 8:
  print('Drew an ' + str(card_name))
else:
  print('Drew a ' + str(card_name))

if card_rank == 11 or card_rank == 12 or card_rank == 13:
  # Jacks, Queens, and Kings are worth 10.
  card1_value = 10
elif card_rank == 1:
  # Aces are worth 11.
  card1_value = 11
else:
  # All other cards are worth the same as
  # their rank.
  card1_value = card_rank

card_rank = randint(1, 13)
if card_rank == 1:
  # A 1 stands for an ace.
  card_name = 'Ace'
elif card_rank == 11:
  # An 11 stands for a jack.
  card_name = 'Jack'
elif card_rank == 12:
  # A 12 stands for a queen.
  card_name = 'Queen'
elif card_rank == 13:
  # A 13 stands for a king.
  card_name = 'King'
else:
  # All other cards are named by their
  # number, or rank.
  card_name = card_rank

if card_rank == 1 or card_rank == 8:
  print('Drew an ' + str(card_name))
else:
  print('Drew a ' + str(card_name))

if card_rank == 11 or card_rank == 12 or card_rank == 13:
  # Jacks, Queens, and Kings are worth 10.
  card2_value = 10
elif card_rank == 1:
  # Aces are worth 11.
  card2_value = 11
else:
  # All other cards are worth the same as
  # their rank.
  card2_value = card_rank

dealer_hand = card1_value + card2_value

# The dealer plays through a round of blackjack.
while dealer_hand < 17:
  # Per the rules of blackjack, the dealer must
  # continue drawing cards until their hand
  # total reaches 17.
  print('Dealer has ' + str(dealer_hand) + '.')

  card_rank = randint(1, 13)
  if card_rank == 1:
    # A 1 stands for an ace.
    card_name = 'Ace'
  elif card_rank == 11:
    # An 11 stands for a jack.
    card_name = 'Jack'
  elif card_rank == 12:
    # A 12 stands for a queen.
    card_name = 'Queen'
  elif card_rank == 13:
    # A 13 stands for a king.
    card_name = 'King'
  else:
    # All other cards are named by their
    # number, or rank.
    card_name = card_rank

  if card_rank == 1 or card_rank == 8:
    print('Drew an ' + str(card_name))
  else:
    print('Drew a ' + str(card_name))

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

  dealer_hand = dealer_hand + card_value

print('Final hand: ' + str(dealer_hand) + '.')
if dealer_hand == 21:
  print('BLACKJACK!')
elif dealer_hand > 21:
  # The dealer busts - or immediately loses - if
  # their hand total goes above 21.
  print('BUST.')

# The final game standings.
print('-----------')
print('GAME RESULT')
print('-----------')

if (dealer_hand == 21 and user_hand == 21) or (dealer_hand == user_hand and user_hand < 21):
  print('Push.')
elif (dealer_hand < 21 and dealer_hand > user_hand) or user_hand > 21 or (dealer_hand == 21 and user_hand != 21):
  print('Dealer wins!')
else:
  print('You win!')
