import builtins
import re
from abc import abstractmethod,ABC
from game_of_greed.game_logic import GameLogic
from game_of_greed.game import Game

totalListCheck=[]

class BasePlayer(ABC):
    def __init__(self):
        self.old_print = print
        self.old_input = input 
        builtins.print = self._mock_print # Methods overriding
        builtins.input = self._mock_input # Methods overriding
        self.total_score = 0
        self.counterOfPlay=1
        self.dice_remaining = 0
        self.unbanked_points = 0
        
    def reset(self):
        builtins.print = self.old_print
        builtins.input = self.old_input

    # The default behaviour
    @abstractmethod
    def _mock_print(self, *args):
       return self.old_print(*args)

    @abstractmethod
    def _mock_input(self, *args):
        return self.old_input(*args)

    @classmethod
    def play(cls, num_games=1,numberOfRounds=20):

        mega_total = 0

        for i in range(num_games):
            player = cls()
            game = Game(None,numberOfRounds) # doesn't pass a mock roller
            # game=Game()
            try:
                game.play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass

            mega_total += player.total_score
            totalListCheck.append(player.total_score)
        
            player.reset()
                
        print(
            f"{num_games} games (maybe) played with average score of {mega_total//num_games }"
        )
        # print(f'all game score  ',totalListCheck)


class NervousNellie(BasePlayer):
    def __init__(self):
        super().__init__()
        self.roll = None
     

    def _mock_print(self, *args):
        first_arg = args[0]
        first_char = first_arg[0]
        if first_char.isdigit():
            self.roll = tuple(int(char) for char in first_arg.split(","))
        elif first_arg.startswith("Thanks for playing."):
            self.total_score = int(re.findall(r"\d+", first_arg)[0])
        self.old_print(first_arg)

    def _mock_input(self, *args):
        prompt = args[0]
        if prompt.startswith("Wanna play?"):
            return "y"
        elif prompt.startswith("Enter dice to keep (no spaces), or (q)uit:"):
            scorers = GameLogic.get_scorers(self.roll)
            keepers = "".join([str(ch) for ch in scorers])
            return keepers
        elif prompt.startswith("(r)oll again, (b)ank your points or (q)uit "):
            return "b"
        else:
            raise ValueError(f"Unrecognized prompt {prompt}")
   


         

class BasicBot(BasePlayer):
    def __init__(self):
        super().__init__()
    def _mock_input(self, *args):
        x = args[0]
        if x.startswith('Wanna play?'):
            return 'n'
    def _mock_print(self, *args):
        self.old_print(*args)
    
    
    

if __name__ == "__main__":
    # BasicBot.play(20)
    NervousNellie.play(10,20)