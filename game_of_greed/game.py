from game_of_greed.game_logic import GameLogic,Banker

class Game:
    def __init__(self, roller=None,score=0):
        self.roller = roller
        self.calculate_score=score

    def play(self):
        print("Welcome to Game of Greed")
        user_input = input("Wanna play? ")
        if user_input == 'n':
            print("OK. Maybe another time")
        else:
            int_banker=Banker()
            counter_remaining=6
            counter_looping=1
            while(True):
                print(f'Starting round {counter_looping}')
                print('Rolling 6 dice...')
                dice = self.roller(6)
                printable_dice = ','.join([str(d) for d in dice])
                print(printable_dice)
                do_quit = input("Enter dice to keep (no spaces), or (q)uit: ")
                if do_quit == 'q':
                    if int_banker.balance != 0 :
                        print(f'Total score is {int_banker.balance} points')
                    print(f'Thanks for playing. You earned {int_banker.balance} points')
                    break
                else :
                    turn_to_list=list(do_quit)
                    turn_to_tuple=tuple(int(x) for x in turn_to_list)
                    # print(turn_to_tuple)
                    score=GameLogic.calculate_score(turn_to_tuple)
                    
                    counter_remaining-=len(turn_to_tuple)
                    print(f'You have {score} unbanked points and {counter_remaining} dice remaining') 
                    int_banker.shelf(score)
                    ask_for_roll_again=input('(r)oll again, (b)ank your points or (q)uit ')
                    int_banker.bank()
                    if ask_for_roll_again=='b':
                        print(f'You banked {int_banker.balance} points in round 1')
                        print(f'Total score is {int_banker.balance} points')
                        counter_looping+=1

    




if __name__ == "__main__":
    roller = GameLogic.roll_dice
    calc_score=GameLogic.calculate_score
    int_banker=Banker()
    # shelf=int_banker.shelf()
    # bank=int_banker.bank()
    # int_banker.shelf(100)
    # print(int_banker.shelved)
    game = Game(roller,calc_score)
    game.play()