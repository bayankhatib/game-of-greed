from game_of_greed.game_logic import GameLogic
from collections import Counter


class GameFunction():
  def rolling(round,roller,diceNumber,startRound_TorF):
        '''
        function for rolling again in the game
        '''
        if startRound_TorF== True:
            print(f'Starting round {round}')

        print(f'Rolling {diceNumber} dice...')
        printable_dice = ','.join([str(d) for d in roller])
        print(printable_dice)
        return printable_dice

  def quitting(balance,shelved,q):
        '''
        function for quit the game
        '''
        if shelved or balance and q :
            print(f'Total score is {balance} points')
        print(f'Thanks for playing. You earned {balance} points')
        

  def calc_score(useAnswer,diceRemaining,banker,total):
        '''
        function for calculating the user score
        '''
        turn_to_list=list(useAnswer)
        turn_to_tuple=tuple(int(x) for x in turn_to_list)
        score=GameLogic.calculate_score(turn_to_tuple)
        diceRemaining-=len(turn_to_tuple)
        print(f'You have {total+score} unbanked points and {diceRemaining} dice remaining') 
        banker.shelf(score)


  def banking(banker,total,round):
        '''
        function for banking the user point's that earned in the game
        '''
        print(f'You banked {total} points in round {round}')
        print(f'Total score is {banker.balance} points')
        


  def validation(userAnswer,rollDice):
      return not (Counter(userAnswer)-Counter(rollDice))
     

  def zelchRoundOver(turn_to_tuple):
        score=GameLogic.calculate_score(turn_to_tuple)
        if score==0:
              print('Zilch!!! Round over')
              return score    
        else:
              return score       
             
