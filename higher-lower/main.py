from art import *
import random
from game_data import *
from replit import clear

print(logo)

score = 0

end_game = False
A = random.choice(data)
while not end_game:
  if score >= 1:
    print(f"You're right! Current score: {score}")
  B = random.choice(data)
  a_fol = A['follower_count']
  b_fol = B['follower_count']
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
  print(vs)
  print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")

  cevap = input("Who has more followers? Type 'A' or 'B'")
  
  if cevap == 'A' and a_fol > b_fol:
    score += 1
    print(score)
    B = A
    clear()
  elif cevap == 'B' and a_fol < b_fol:
    score += 1
    print(score)
    A = B
    clear()
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    end_game = True
    