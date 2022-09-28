import art
import random
from game_data import data

print(art.logo)

randomA = random.sample(data,1)
randomB = random.sample(data,1)

def printDetail(randA,randB):
  print(f"Compare A: {randA[0]['name']}, a {randA[0]['description']}, from {randA[0]['country']} \n")
  print(art.vs)
  print(f"Against B: {randB[0]['name']}, a {randB[0]['description']}, from {randB[0]['country']} \n")

printDetail(randomA, randomB)

player_answer = input("Who has more followers? Type 'A or 'B'.").lower()

score = 0

#check which side has larger follower score
def decideWinner(answer):
  if randomA[0]['follower_count'] > randomB[0]['follower_count']:
    result = 'a'
    return result
  elif randomA[0]['follower_count'] < randomB[0]['follower_count']:
    result = 'b'
    return result

def aORb(winn):
  if winn == 'a':
    return randomA
  else:
    return randomB

#Need to check whether the answer given by the player is actually correct. 
while player_answer == decideWinner(player_answer):
  print('Correct!')
  score += 1
  print(f'Your score {score} \n') 
  randomA = aORb(player_answer)
  randomB = random.sample(data,1)
  printDetail(randomA,randomB)
  player_answer = input("Who has more followers? Type 'A or 'B'.").lower()
  decideWinner(player_answer)
  
else:
  print("Sorry that's wrong.")
  print(f'Your final score is {score}.')
  
