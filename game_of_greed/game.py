from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from game_of_greed.functionOfGame import GameFunction



class Game:
 
    def __init__(self, roller=None,numOfgame=5):
        self.banker=Banker()
        self.gameLogic=GameLogic
        self.roller = roller or GameLogic.roll_dice
        self.total=0
        self.round=1
        self.dice=6
        self.numOfgame=numOfgame


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
        elif user_input == 'y':
            r=True
            start_condition=True
    
            while(self.round<=self.numOfgame):
                '''
                auto get random and 
                '''
                if start_condition==True:
                    roller_dice=self.roller(self.dice)
                    randomNumber=GameFunction.rolling(self.round,roller_dice,self.dice,r)
                    zelch=GameFunction.zelchRoundOver(roller_dice)
                    if zelch:
                        r=True
                        self.dice=6
                        self.staticValuesForBank(0)
                        roller_dice=self.roller(self.dice)
                        randomNumber=GameFunction.rolling(self.round,roller_dice,self.dice,r)

                do_quit = input("Enter dice to keep (no spaces), or (q)uit: ")
                if do_quit == 'q':
                    GameFunction.quitting(self.banker.balance,self.banker.shelved)
                    break

               
                else :
                    turn_to_tuple=list(int(x) for x in list(do_quit)) 
                    check=GameFunction.validation(turn_to_tuple,list(roller_dice))  
   
                    if check == False:
                        start_condition=False
                        print("Cheater!!! Or possibly made a typo...")
                        print(randomNumber)
                        continue
                    else:
                        start_condition=True
                       
                    checkFromThe3of2=GameFunction.calc_score(do_quit,self.dice,self.banker,self.total)
                    self.total=self.banker.shelved
                  
                    
                    ask_for_roll_again=input('(r)oll again, (b)ank your points or (q)uit ')
                    
                    if ask_for_roll_again=='b':
                    #    totalBanking=banker.bank()
                        r=True
                        self.banker.bank()

                        self.staticValuesForBank(self.total)
                    
                    elif ask_for_roll_again=='r':
                        r=False
                        if self.dice ==0:
                            self.dice=6
                        if checkFromThe3of2:
                            self.dice=6
                        else :    
                            self.dice-=len(turn_to_tuple)

                    elif ask_for_roll_again=='q':
                        GameFunction.quitting(self.banker.balance,self.banker.shelved)
                        break

    def staticValuesForBank(self,total): 
        GameFunction.banking(self.banker,total,self.round)
        self.dice=6
        self.round+=1
        self.total=0           





if __name__ == "__main__":
    roller = GameLogic.roll_dice
    game = Game(roller)
    game.play()