#Black Jack

import random
import time

cards = ["Ace of Spades", "Ace of Clubs", "Ace of Hearts", "Ace of Diamonds", " 2 of Spades", "2 of Clubs", "2 of Hearts", "2 of Diamonds", "3 of Spades", "3 of Clubs", "3 of Hearts", "3 of Diamonds", "4 of Spades", "4 of Clubs", "4 of Hearts", "4 of Diamonds", "5 of Spades", "5 of Clubs", "5 of Hearts", "5 of Diamonds", "6 of Spades", "6 of Clubs", "6 of Hearts", "6 of Diamonds", "7 of Spades", "7 of Clubs", "7 of Hearts", "7 of Diamonds", "8 of Spades", "8 of Clubs", "8 of Hearts", "8 of Diamonds", "9 of Spades", "9 of Clubs", "9 of Hearts", "9 of Diamonds", "10 of Spades", "10 of Clubs", "10 of Hearts", "10 of Diamonds", "Jack of Spades", "Jack of Clubs", "Jack of Hearts", "Jack of Diamonds", "Queen of Spades", "Queen of Clubs", "Queen of Hearts", "Queen of Diamonds", "King of Spades", "King of Clubs", "King of Hearts", "King of Diamonds"]
random.shuffle(cards)

computer_hand = []
player_hand = []
player_points = 0


def play():

  computer_hand = []
  player_hand = []

  time.sleep(2)
  player_hand.append(cards.pop(0))
  time.sleep(1)

  computer_hand.append(cards.pop(0))
  time.sleep(1)

  player_hand.append(cards.pop(0))
  print("Here is your starting hand:", player_hand)
  time.sleep(1)

  computer_hand.append(cards.pop(0))
  print("The computer's face-up card is " + computer_hand[0])


  def player_point_count():

    global player_points
    player_points = 0

    if "Ace of Spades" in player_hand or "Ace of Clubs" in player_hand or "Ace of Hearts" in player_hand or "Ace of Diamonds" in player_hand:
      player_points += 11

      if player_points > 10:
        player_points += 1


    if "2 of Spades" in player_hand or "2 of Clubs" in player_hand or "2 of Hearts" in player_hand or "2 of Diamonds" in player_hand:
      player_points += 2


    if "3 of Spades" in player_hand or "3 of Clubs" in player_hand or "3 of Hearts" in player_hand or "3 of Diamonds" in player_hand:
      player_points += 3


    if "4 of Spades" in player_hand or "4 of Clubs" in player_hand or "4 of Hearts" in player_hand or "4 of Diamonds" in player_hand:
      player_points += 4


    if "5 of Spades" in player_hand or "5 of Clubs" in player_hand or "5 of Hearts" in player_hand or "5 of Diamonds" in player_hand:
      player_points += 5


    if "6 of Spades" in player_hand or "6 of Clubs" in player_hand or "6 of Hearts" in player_hand or "6 of Diamonds" in player_hand:
      player_points += 6


    if "7 of Spades" in player_hand or "7 of Clubs" in player_hand or "7 of Hearts" in player_hand or "7 of Diamonds" in player_hand:
      player_points += 7


    if "8 of Spades" in player_hand or "8 of Clubs" in player_hand or "8 of Hearts" in player_hand or "8 of Diamonds" in player_hand:
      player_points += 8


    if "9 of Spades" in player_hand or "9 of Clubs" in player_hand or "9 of Hearts" in player_hand or "9 of Diamonds" in player_hand:
      player_points += 9


    if "10 of Spades" in player_hand or "10 of Clubs" in player_hand or "10 of Hearts" in player_hand or "10 of Diamonds" in player_hand or "Jack of Spades" in player_hand or "Jack of Clubs" in player_hand or "Jack of Hearts" in player_hand or "Jack of Diamonds" in player_hand or "Queen of Spades" in player_hand or "Queen of Clubs" in player_hand or "Queen of Hearts" in player_hand or "Queen of Diamonds" in player_hand or "King of Spades" in player_hand or "King of Clubs" in player_hand or "King of Hearts" in player_hand or "King of Diamonds" in player_hand:
      player_points += 10

    return player_points


  def computer_point_count():


    global computer_points
    computer_points = 0

    if "Ace of Spades" in computer_hand or "Ace of Clubs" in computer_hand or "Ace of Hearts" in computer_hand or "Ace of Diamonds" in computer_hand:
      computer_points += 11

    while computer_points > 10:
      if "Ace of Spades" in computer_hand or "Ace of Clubs" in computer_hand or "Ace of Hearts" in computer_hand or "Ace of Diamonds" in computer_hand:
        computer_points += 1


    if "2 of Spades" in computer_hand or "2 of Clubs" in computer_hand or "2 of Hearts" in computer_hand or "2 of Diamonds" in computer_hand:
      computer_points += 2


    if "3 of Spades" in computer_hand or "3 of Clubs" in computer_hand or "3 of Hearts" in computer_hand or "3 of Diamonds" in computer_hand:
      computer_points += 3


    if "4 of Spades" in computer_hand or "4 of Clubs" in computer_hand or "4 of Hearts" in computer_hand or "4 of Diamonds" in computer_hand:
      computer_points += 4


    if "5 of Spades" in computer_hand or "5 of Clubs" in computer_hand or "5 of Hearts" in computer_hand or "5 of Diamonds" in computer_hand:
      computer_points += 5


    if "6 of Spades" in computer_hand or "6 of Clubs" in computer_hand or "6 of Hearts" in computer_hand or "6 of Diamonds" in computer_hand:
      computer_points += 6


    if "7 of Spades" in computer_hand or "7 of Clubs" in computer_hand or "7 of Hearts" in computer_hand or "7 of Diamonds" in computer_hand:
      computer_points += 7


    if "8 of Spades" in computer_hand or "8 of Clubs" in computer_hand or "8 of Hearts" in computer_hand or "8 of Diamonds" in computer_hand:
      computer_points += 8


    if "9 of Spades" in computer_hand or "9 of Clubs" in computer_hand or "9 of Hearts" in computer_hand or "9 of Diamonds" in computer_hand:
      computer_points += 9


    if "10 of Spades" in computer_hand or "10 of Clubs" in computer_hand or "10 of Hearts" in computer_hand or "10 of Diamonds" in computer_hand or "Jack of Spades" in computer_hand or "Jack of Clubs" in computer_hand or "Jack of Hearts" in computer_hand or "Jack of Diamonds" in computer_hand or "Queen of Spades" in computer_hand or "Queen of Clubs" in computer_hand or "Queen of Hearts" in computer_hand or "Queen of Diamonds" in computer_hand or "King of Spades" in computer_hand or "King of Clubs" in computer_hand or "King of Hearts" in computer_hand or "King of Diamonds" in computer_hand:
      computer_points += 10

    return computer_points




  def main():
    hit_stand = input("Press 'H' for hit me. 'S' for stand")
    if hit_stand == ("H"):
      player_hand.append(cards.pop(0))
      print("Here is your updated hand:", player_hand)
      print(player_point_count())

    if hit_stand == ("S"):
      return

  global computer_points
  global player_points

  while player_points <= 20:
    print(main())

  if player_points > 20:
    return

  time.sleep(0)
  print("Your current hand value is " + str(player_point_count()))


  print("Player points:", player_point_count())
  print("Computer points:", computer_point_count())

  if player_points <= 21 and computer_points <= 21:
    print("a")#letters are just testing what's printing

    if abs(player_points - 21) == abs(computer_points - 21):
      print("a1")

      print("Player points:", player_points)
      print("Computer points:", computer_points)
      print("Tie.")

    if abs(player_points - 21) < abs(computer_points - 21):
      print("a2")

      print("Player points:", player_points)
      print("Computer points:", computer_points)
      print("Player wins.")

    if abs(player_points - 21) > abs(computer_points - 21):
      print("a3")

      print("Player points:", player_points)
      print("Computer points:", computer_points)
      print("Computer wins")

  else:
    if player_points > 21 and computer_points > 21:
      print("b1")

      print("player points:", player_points)
      print("computer points:", computer_points)
      print("Both bust.")

    if player_points <= 21 and computer_points > 21:
      print("b2")

      print("Player points:", player_points)
      print("Computer points:", computer_points)
      print("Computer busts. Player wins")

    if player_points > 21 and computer_points <= 21:
      print("b3")

      print("Player points:", player_points)
      print("computer points:", computer_points)
      print("Player busts Computer wins")


while True:
  start = input("Press Y to begin")
  if start == ("Y"):
    if len(cards) >= 4:
      print(play())
    else:
      print("Game Over")
  else:
    print("Okay then.")















