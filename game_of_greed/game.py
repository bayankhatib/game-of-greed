from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from game_of_greed.functionOfGame import GameFunction
from collections import Counter



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
        elif user_input == 'y':
            r=True
            while(True):
                roller_dice=self.roller(6)
                GameFunction.rolling(self.round,roller_dice,r)
                do_quit = input("Enter dice to keep (no spaces), or (q)uit: ")
                
                
                if do_quit == 'q':
                    GameFunction.quitting(self.banker.balance)
                    break

               
                else :
                      

                    turn_to_list =list(do_quit)
                    turn_to_tuple=tuple(int(x) for x in turn_to_list)
                            
                    l1=Counter(turn_to_tuple).most_common() 
                    # print(l1 ,'***',self.roller)
                    l2=Counter(roller_dice).most_common() 
                    # print(l2,l1)
                    check =  all(item in l1 for item in l2)
                    
                    if check == False:
                        print("Cheater!!! Or possibly made a typo...")
                        # print(self.roller)
                               
                    

                    GameFunction.calc_score(do_quit,self.dice,self.banker,self.total)

                    ask_for_roll_again=input('(r)oll again, (b)ank your points or (q)uit ')

                    self.banker.bank
                    self.total+=self.banker.shelved
                    if ask_for_roll_again=='b':
                        r=True
                        GameFunction.banking(self.banker,self.round)
                        self.dice=6
                        self.round+=1
                    elif ask_for_roll_again=='r':
                        r=False
                

     


#             >>> l = ["a","b","b"]
# >>> l.count("a")
# 1
# >>> l.count("b")
# 2

                        



                      




if __name__ == "__main__":
    roller = GameLogic.roll_dice
    game = Game(roller)
    game.play()