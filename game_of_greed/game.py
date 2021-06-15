from game_of_greed.game_logic import GameLogic,Banker
from game_of_greed.functionOfGame import GameFunction


class Game:
    def __init__(self, roller=None):
        self.banker=Banker()
        self.gameLogic=GameLogic
        self.roller = roller or GameLogic.roll_dice()
        self.total=0
        self.round=1
        self.dice=6

    def play(self):
        """ 
       this function where the user can start the game
       to start round 1 and can roll the dice and choose from dice,
       also known banked and unbanked points and total score 
       for six round and user can quit the game. 

        """
        print("Welcome to Game of Greed")
        user_input = input("Wanna play? ")
        if user_input == 'n':
            print("OK. Maybe another time")
        else:
            while(True):
                GameFunction.rolling(self.round,self.roller)
                do_quit = input("Enter dice to keep (no spaces), or (q)uit: ")
                if do_quit == 'q':
                    GameFunction.quitting(self.banker.balance,self.total)
                    break
                elif do_quit=='b' :
                    GameFunction.calc_score(do_quit,self.dice,self.banker)
                    ask_for_roll_again=input('(r)oll again, (b)ank your points or (q)uit ')
                    self.total+=self.banker.shelved
                    if ask_for_roll_again=='b':
                        GameFunction.banking(self.banker,self.round,self.total)
                        self.dice=6
                        self.round+=1




if __name__ == "__main__":
    roller = GameLogic.roll_dice
    game = Game(roller)
    game.play()