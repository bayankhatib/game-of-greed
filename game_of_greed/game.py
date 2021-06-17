from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from game_of_greed.functionOfGame import GameFunction

class Game:
    def __init__(self, roller=None,numOfgame=None):
        self.banker=Banker()
        self.gameLogic=GameLogic
        self.roller = roller or GameLogic.roll_dice
        self.total=0
        self.round=1
        self.dice=6
        self.numOfgame=numOfgame
        self.zelch=0
        self.startRound_TorF=True
        self.checkValidation=True
        self.start_condition=True
        self.randomNumber=''
        self.roller_dice=None


    def play(self):
        """ 
       this function where the user can start the game
       to start round 1 and can roll the dice and choose from dice,
       also known banked and unbanked points and total score 
       for six round and user can quit the game. 
        """
        print("Welcome to Game of Greed")
        try:
            user_input = input("Wanna play? ")
        except:
            raise "You Didn't answer Right "    
        if user_input == 'n':
            print("OK. Maybe another time")
        elif user_input == 'y':   
            while(True):
                '''
                auto get random and 
                '''
                if self.start_condition==True:
                    self.startTheGame()
                try:    
                    do_quit = input("Enter dice to keep (no spaces), or (q)uit: ")
                except:
                    raise "You Didn't answer Right"
                if do_quit == 'q':
                    GameFunction.quitting(self.banker.balance,self.banker.shelved,True)
                    break
               
                elif do_quit.isdigit():
                    turn_to_tuple=list(int(x) for x in list(do_quit)) 
                    self.checkValidation=GameFunction.validation(turn_to_tuple,list(self.roller_dice))  
                    self.checkValidationFun()
                    if self.start_condition is False:
                        continue

                    GameFunction.calc_score(do_quit,self.dice,self.banker,self.total)
                    self.total=self.banker.shelved
                  
                    try:
                        ask_for_roll_again=input('(r)oll again, (b)ank your points or (q)uit ')
                    except:
                        raise "You Didn't answer Right"
                    if ask_for_roll_again=='b':
                        self.bank_Answer()

                    elif ask_for_roll_again=='r':
                        self.rolling_Answer(turn_to_tuple)
                        
                    elif ask_for_roll_again=='q':
                        GameFunction.quitting(self.banker.balance,self.banker.shelved,True)
                        break

                if self.numOfgame and self.round>self.numOfgame :
                    GameFunction.quitting(self.banker.balance,self.banker.shelved,False)
                    break


    def staticValuesForBank(self,total): 
        GameFunction.banking(self.banker,total,self.round)
        self.dice=6
        self.round+=1
        self.total=0               

    def bank_Answer(self):
        self.startRound_TorF=True
        self.banker.bank()
        self.staticValuesForBank(self.total)

    def rolling_Answer(self,userAnswerForDice):  
        self.startRound_TorF=False
        if self.dice ==0 or self.zelch==1500:
            self.dice=6
        else :    
            self.dice-=len(userAnswerForDice)  

    def zelchOutput(self):
        if self.zelch==0:
            self.startRound_TorF=True
            self.dice=6
            self.staticValuesForBank(0)
            self.roller_dice=self.roller(self.dice,self.numOfgame)
            self.randomNumber=GameFunction.rolling(self.round,self.roller_dice,self.dice,self.startRound_TorF)

    def checkValidationFun(self):
        if self.checkValidation == False:
            self.start_condition=False
            print("Cheater!!! Or possibly made a typo...")
            print(self.randomNumber)
        else:
            self.start_condition=True

    def startTheGame(self):
        self.roller_dice=self.roller(self.dice,self.numOfgame)
        self.randomNumber=GameFunction.rolling(self.round,self.roller_dice,self.dice,self.startRound_TorF)
        self.zelch=GameFunction.zelchRoundOver(self.roller_dice)
        self.zelchOutput()        




if __name__ == "__main__":
    roller = GameLogic.roll_dice
    game = Game(roller)
    game.play()