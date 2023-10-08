import card
from card import Witch_symbol,Seer_symbol,Villager_symbol,Werewolf_symbol
import turtle

class Villager:
    def __init__(self,name="villager",type="human",playerid=1):
        self.name = name
        self.type = type
        self.playerid=playerid

    def card(self):
        villager_symbol = Villager_symbol()
        villager_symbol.print_card()


class Seer:
    def __init__(self,name="seer",type="god",playerid=1):
        self.name = name
        self.type = type
        self.playerid = playerid

    def card(self):
        seer_symbol = Seer_symbol()
        seer_symbol.print_card()
        
class Witch:
    def __init__(self,name="witch",type="god",cure=1,poison=1,playerid=1):
        self.name = name
        self.type = type
        self.cure=cure
        self.poison=poison
        self.playerid=playerid

    def card(self):
        witch_symbol = Witch_symbol()
        witch_symbol.print_card(witch_symbol)
    
    def save(self):
        if self.cure==1:
            print("1.cure")
        if self.poison==1:
            print("2.poison")
        if self.cure==0 and self.poison==0:
            print("3.you do not have a cure or a poison,skip")
        

class Werewolf: 
    def __init__(self,name="werewolf",type="wolf",playerid=1):
        self.name = name
        self.type = type
        self.playerid=playerid

    def card(self):
        werewolf_symbol = Werewolf_symbol()
        werewolf_symbol.print_card()

# villager1=Villager()
# seer=Seer()
# witch=Witch()
# werewolf1=Werewolf()

#test
#seer.card()
#villager1.card()
#werewolf1.card()
#witch.card()