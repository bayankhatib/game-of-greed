from game_of_greed.game_logic import GameLogic


class GameFunction():
  def rolling(round,roller):
        '''
        function for rolling again in the game
        '''
        print(f'Starting round {round}')
        print('Rolling 6 dice...')
        dice = roller(6)
        printable_dice = ','.join([str(d) for d in dice])
        print(printable_dice)

  def quitting(balance,total):
        '''
        function for quit the game
        '''
        if balance != 0 :
            print(f'Total score is {total} points')
            print(f'Thanks for playing. You earned {total} points')

  def calc_score(useAnswer,diceRemaining,bank):
        '''
        function for calculating the user score
        '''
        turn_to_list=list(useAnswer)
        turn_to_tuple=tuple(int(x) for x in turn_to_list)
        score=GameLogic.calculate_score(turn_to_tuple)
        diceRemaining-=len(turn_to_tuple)
        print(f'You have {score} unbanked points and {diceRemaining} dice remaining') 
        bank.shelf(score)

  def banking(banker,round,total):
        '''
        function for banking the user point's that earned in the game
        '''
        banker.bank()
        print(f'You banked {banker.balance} points in round {round}')
        print(f'Total score is {total} points')
