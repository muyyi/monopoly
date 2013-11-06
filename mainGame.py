from gameClasses import *
from console import *
from statusWindow import *
DEFAULT_MONEY = 1500
START='start'
INGAME='ingame'
FINISH='finish'
class monoGame():
    gameState=START
    curr_turn=0
    def __init__(self,board,players=[]):
        self.players=players
        self.board=board
        self.console=console()
        self.statusWindow=statusWindow()
    def do_move(diceSum):
        player=self.players[curr_turn]        
        currBlock=self.board[(player.location+diceSum)%(len(board)-1)]
        currBlock.landOn(player)
        actions=currBlock.getActions()
        if(len(actions)==1):
            actions[0]()
        else:
            self.chooseFromOptions(actions)
        self.curr_turn=(self.curr_turn+1)%(len(players)-1)
        
    def start(self):
        self.console.start()
        name_player = self.console.get_player_name()
        new_player1 = player(name_player,DEFAULT_MONEY)
        self.players.append(new_player1)
        
        name_player = self.console.get_player_name()
        new_player2 = player(name_player,DEFAULT_MONEY)
        self.players.append(new_player2)
        pass
    
    def is_complete(self):  # check if anyone wins, 
        c = 0
        for p in player :
            if not p.is_bankrupt():
                c+=1
        if c == 1:
            for p in player :
                if p.is_bankrupt():
                    gameState=FINISH
                    return True
                     
        elif c == 0:
            gameState=FINISH
            return True
        gameState=INGAME
        return False    