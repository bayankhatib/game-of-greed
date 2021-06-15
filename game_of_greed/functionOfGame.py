from game_of_greed.game_logic import GameLogic


class GameFunction():
  def rolling(round,roller,r):

        '''
        function for rolling again in the game
        '''
        if r== True:
            print(f'Starting round {round}')
        print('Rolling 6 dice...')
      #   dice = roller()
        printable_dice = ','.join([str(d) for d in roller])
        print(printable_dice)
        return printable_dice

  def quitting(balance,shelved):
        '''
        function for quit the game
        '''
        if shelved or balance  :
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
        total+=score
        print(f'You have {total} unbanked points and {diceRemaining} dice remaining') 
        banker.shelf(total)

  def banking(banker,total,round):
        '''
        function for banking the user point's that earned in the game
        '''
        totalBanking=banker.bank()
        print(f'You banked {total} points in round {round}')
        print(f'Total score is {totalBanking} points')


  def validation(userAnswer,rollDice):
      counter=0
      for i in range(len(userAnswer)):
            for j in range(len(rollDice)):
                  if userAnswer[i]==rollDice[j]:
                    rollDice[j]=-1
                    counter+=1
                    break
      if counter ==len(userAnswer):
            return True
      return False
     
            