import random
from collections import Counter

all_rules = {
    '(1, 1)': 100,
    '(1, 2)': 200,
    '(1, 3)': 1000,
    '(1, 4)': 2000,
    '(1, 5)': 3000,
    '(1, 6)': 4000,
    '(2, 3)': 200,
    '(2, 4)': 400,
    '(2, 5)': 600,
    '(2, 6)': 800,
    '(3, 3)': 300,
    '(3, 4)': 600,
    '(3, 5)': 900,
    '(3, 6)': 1200,
    '(4, 3)': 400,
    '(4, 4)': 800,
    '(4, 5)': 1200,
    '(4, 6)': 1600,
    '(5, 1)': 50,
    '(5, 2)': 100,
    '(5, 3)': 500,
    '(5, 4)': 1000,
    '(5, 5)': 1500,
    '(5, 6)': 2000,
    '(6, 3)': 600,
    '(6, 4)': 1200,
    '(6, 5)': 1800,
    '(6, 6)': 2400,
}

class GameLogic:
   def __init__(self):
     pass
  
   @staticmethod
   def calculate_score(a):
    score = 0
    roll_dice_Input=Counter(a)
    if len(roll_dice_Input.most_common()) == 3 and roll_dice_Input.most_common()[0][1]==2 and roll_dice_Input.most_common()[1][1]==2 and roll_dice_Input.most_common()[2][1]==2 :
        return 1500
        
    if a ==():
      return 0
    elif roll_dice_Input.most_common(1)[0]== (1,1) and len( roll_dice_Input.most_common())==6:
      score=1500
      return score
    else :
      dic_counter= Counter(all_rules)
      case01=roll_dice_Input.most_common()
      for case in  case01:
        score+=dic_counter[str(case)]
      return score 
  
   @staticmethod 
   def roll_dice(value=6):
      values = []
      for i in range(value):
        values.append(random.randint(1,6))
      return tuple(values)
        










     
