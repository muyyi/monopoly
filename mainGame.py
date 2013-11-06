from gameClasses import player
import console as _console
from statusWindow import *
from random import *

START='start'
INGAME='ingame'
FINISH='finish'
generel_commands = ["roll","build","mortage","unmortage","trade","end"]

class monoGame():
    gameState=START
    curr_turn=0
    def __init__(self,board,players=[]):
        self.players=players
        self.board=board
        self.console=_console.console()
        self.statusWindow=statusWindow()
        self.default_money = 1500
        self.current_player = 0 # index of the current player
        self.winner = -1;
        
#     def do_move(diceSum):
#         player=self.players[curr_turn]        
#         currBlock=self.board[(player.location+diceSum)%(len(board)-1)]
#         currBlock.landOn(player)
#         actions=currBlock.getActions()
#         if(len(actions)==1):
#             actions[0]()
#         else:
#             self.chooseFromOptions(actions)
#         self.curr_turn=(self.curr_turn+1)%(len(players)-1)
        
    def start(self):
        self.console.start()
        
        name_player = self.console.get_player_name()
        new_player1 = player(name_player,self.default_money)
        self.players.append(new_player1)
        
        name_player = self.console.get_player_name()
        new_player2 = player(name_player,self.default_money)
        self.players.append(new_player2)
        
        self.current_player = randrange(len(self.players))
        self.console.display("{} takes the first turn".format(self.players[self.current_player].name))
        
        while not self.is_complete():
            self.next_turn()
            
        if not winner == -1:
            self.console.show_winner(winner)
    
    def next_turn(self):
        # main game logic
        rolled_already = False
        end_turn = False
        name = self.players[self.current_player].name
        self.console.display(name)
        while not end_turn:
            cmd = self.console.prompt_commands(generel_commands)
            if cmd == "roll":
                if not rolled_already:
                    dice = self.board.roll_dice()
                    self.console.display("Dice rolled {}".format(dice))
                    rolled_already = True
                    # movement around the board and actions on landing
                else:
                    self.console.display("You have already rolled the dice")
            elif cmd == "end":
                if not rolled_already:
                    self.console.display("You first have to roll the dice")
                else:
                    end_turn = True
                    self.console.display("{} ends his turn".format(name))
            elif cmd == "build":    
                pass
            elif cmd == "mortage":    
                pass
            elif cmd == "unmortage":    
                pass
            elif cmd == "trade":    
                pass
            else:
                self.console.display("Invalid command input!")     
        #complete the turn than change to next player
        self.current_player = self.next_player(self.current_player)
        pass
    
    def next_player(self, index):
        if index < len(self.players)-1:
            index += 1
        elif index ==  len(self.players)-1:
            index = 0
        return index
    
    def is_complete(self):  # check if anyone wins, 
        c = 0
        w = 0
        for p in self.players :
            if not p.is_bankrupt():
                c+=1
                w = p
        if c == 1:
            winner = w
            gameState=FINISH
            return True
        elif c == 0:
            gameState=FINISH
            return True
        gameState=INGAME
        return False    