from game_of_greed.game_logic import GameLogic,Banker

class Game:
    def __init__(self, roller=None):
        
        self.roller = roller

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
            int_banker=Banker()



            while(True):
                print(f'Starting round {self.round}')

                print('Rolling 6 dice...')

                dice = self.roller(6)

                printable_dice = ','.join([str(d) for d in dice])

                print(printable_dice)

                do_quit = input("Enter dice to keep (no spaces), or (q)uit: ")

                if do_quit == 'q':

                    if int_banker.balance != 0 :

                        print(f'Total score is {self.total} points')

                    print(f'Thanks for playing. You earned {self.total} points')

                    break


                else :
                    turn_to_list=list(do_quit)

                    turn_to_tuple=tuple(int(x) for x in turn_to_list)

                    score=GameLogic.calculate_score(turn_to_tuple)
                    
                    self.dice-=len(turn_to_tuple)

                    print(f'You have {score} unbanked points and {self.dice} dice remaining') 

                    int_banker.shelf(score)

                    ask_for_roll_again=input('(r)oll again, (b)ank your points or (q)uit ')

                    int_banker.bank()

                    self.total+=int_banker.balance


                    if ask_for_roll_again=='b':

                        self.dice=6

                        print(f'You banked {int_banker.balance} points in round {self.round}')

                        print(f'Total score is {self.total} points')

                        self.round+=1




if __name__ == "__main__":

    roller = GameLogic.roll_dice

    game = Game(roller)

    game.play()