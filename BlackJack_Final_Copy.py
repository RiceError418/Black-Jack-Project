#Black Jack

import random
import time

cards = ["Ace of Spades", "Ace of Clubs", "Ace of Hearts", "Ace of Diamonds", " 2 of Spades", "2 of Clubs", "2 of Hearts", "2 of Diamonds", "3 of Spades", "3 of Clubs", "3 of Hearts", "3 of Diamonds", "4 of Spades", "4 of Clubs", "4 of Hearts", "4 of Diamonds", "5 of Spades", "5 of Clubs", "5 of Hearts", "5 of Diamonds", "6 of Spades", "6 of Clubs", "6 of Hearts", "6 of Diamonds", "7 of Spades", "7 of Clubs", "7 of Hearts", "7 of Diamonds", "8 of Spades", "8 of Clubs", "8 of Hearts", "8 of Diamonds", "9 of Spades", "9 of Clubs", "9 of Hearts", "9 of Diamonds", "10 of Spades", "10 of Clubs", "10 of Hearts", "10 of Diamonds", "Jack of Spades", "Jack of Clubs", "Jack of Hearts", "Jack of Diamonds", "Queen of Spades", "Queen of Clubs", "Queen of Hearts", "Queen of Diamonds", "King of Spades", "King of Clubs", "King of Hearts", "King of Diamonds"]
random.shuffle(cards)

computer_hand = []
player_hand = []
player_points = 0
computer_points = 0


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
  print("GLaDOS' face-up card is " + computer_hand[0])


  def player_point_count():
    # To count the player's points, it will check the player's hand for each card and add the corresponding value to the player's total points.
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
    # To count GLaDOS' points, it will check GLaDOS' hand for each card and add the corresponding value to the computer's total points.
      
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


  global computer_points
  global player_points

  time.sleep(0)
  print("Your current hand value is " + str(player_point_count()))

  # The main function will ask the player if they want to hit or stand. If the player chooses to hit, it will add a card to the player's hand and print the updated hand and the current hand value. If the player chooses to stand, it will return False and end the loop.
  def main():
    hit_stand = input("Press 'H' for hit me. 'S' for stand")
    if hit_stand == ("H"):
      player_hand.append(cards.pop(0))
      time.sleep(2)
      print("Here is your updated hand:", player_hand)
      player_point_count()
      time.sleep(2)
      print("Your current hand value is " + str(player_point_count()))
      return True
      
    if hit_stand == ("S"):
      return False


  while player_points <= 20:
    keep_going = main()
    if keep_going == False:
      break
  
  print("Player's final hand value is " + str(player_point_count()))
  time.sleep(2)
  print("GLaDOS' points:", computer_point_count())

  # For calculating the winner, it will check if the player and GLaDOS have points less than or equal to 21. If they do, it will check who is closer to 21 and declare them the winner. If both players have points greater than 21, it will declare a bust. If one player has points less than or equal to 21 and the other has points greater than 21, it will declare the player with points less than or equal to 21 the winner.
  if player_points <= 21 and computer_points <= 21:

    if abs(player_points - 21) == abs(computer_points - 21):
      time.sleep(2)
      print("Both you AND GLaDOS have the same points. It's a tie :000")
      time.sleep(1)
      print("GLaDOS: ))))))):")
      time.sleep(2)
      print("But that still means GLaDOS doesn't win. GLaDOS is sad. You are a mean person.")

      
    if abs(player_points - 21) < abs(computer_points - 21):
      time.sleep(2)
      print("You win. Congratulations. Say good game to GLaDOS, you made her cry.")
      time.sleep(1)
      print("GLaDOS: ))))))):")
      time.sleep(2)
      print("GLaDOS is CRYING. She is sad. You are a mean person.")

    if abs(player_points - 21) > abs(computer_points - 21):
      time.sleep(2)
      print("GLaDOS wins, you lose. She is happy. You are a mean person.")
      print("GLaDOS: :DDDDDD")


  else:
    if player_points > 21 and computer_points > 21:
      time.sleep(2)
      print("Both you AND GLaDOS bust.")
      time.sleep(1)
      print("GLaDOS: :(((((((")
      time.sleep(2)
      print("Now you both are sad. You are a mean person.")

    if player_points <= 21 and computer_points > 21:
      time.sleep(2)
      print("GLaDOS busts. You win. Congratulations. Say good game to GLaDOS. You made her cry.")
      time.sleep(1)
      print("GLaDOS: ))))))):")
      time.sleep(2)
      print("GLaDOS is CRYING. She is sad. You are a mean person.")

    if player_points > 21 and computer_points <= 21:
      time.sleep(2)
      print("You bust. GLaDOS wins. She is happy. You are a mean person.")
      time.sleep(1)
      print("GLaDOS: :DDDDDD")
      time.sleep(2)
      print("GLaDOS is happy. You are a mean person.")

# Loop to start the game and check if there are enough cards to play. If there are not enough cards, it will print "Game Over" and end the game. If the player does not want to play, it will print "Okay then." and end the game.  
while True:
  start = input("Press Y to begin a round of Black Jack with everyone's favourite robot, GLaDOS.")
  if start == ("Y"):
    if len(cards) >= 4:      
      play()
    else:
      print("Game Over")
  else:
    print("Okay then.")















