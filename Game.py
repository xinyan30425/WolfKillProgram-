import random
from random import randint,choice
import card
from time import sleep 
import statistics
from statistics import mode
from Character import Villager,Seer,Witch,Werewolf


def seercheck(checkid):
    for i in player_list:
        if i.playerid == checkid:
            identity(i)
                
def identity(role):
    if role.type=="human" or role.type=="god":
        print(f"you have checked player {role.playerid} identity is GOOD")
    elif role.type=="wolf":
        print(f"you have checked player {role.playerid} identity is WOLF")

def wolfattack():
    print(f"The alive players are: {alive_list}")
    print("werewolf please choose one player to attack from the alivelist:")
    victim = int(input())
    if not isinstance(victim, int):
        raise TypeError("playerid must be integer")

    for i in alive_list:
        if i == victim:
            alive_list.remove(i)
            victim_list.extend([i]) 
    print(f"Wolf team choose to kill player {victim}")
    print(f"Victim list: {victim_list}")
    return victim   

def witch_magic(victimid):
    witch_select=int(input())
    if not isinstance(witch_select, int):
        raise TypeError("selection must be integer")

    if witch_select == 1:
        print("witch choose to cure")
        alive_list.append(victimid) #append() fucntion to push item into stack
        victim_list.remove(victimid)
        witch.cure=0

    elif witch_select == 2:
        print(f"The alive players are: {alive_list}")
        print("please choose a player to poison:")
        choose_poison=int(input())
        if not isinstance(choose_poison, int):
            raise TypeError("playerid must be integer")

        alive_list.remove(choose_poison)
        victim_list.extend([choose_poison])
        witch.poison=0

    else:
        print("witch choose to skip")
        print("witch please close your eyes")
        

def vote():
    vote_list=[]
    for i in alive_list:
        print(f"player {i} please vote")
        voteid = int(input())
        if not isinstance(voteid, int):
            raise TypeError("playerid must be integer")
        
        print("player",i, "vote for",voteid)
        vote_list.append(voteid) #append() fucntion to push item into stack

    #find the most frequent element in the list, to get who gets the most vote
    vote_out = mode(vote_list) #get the most common value from a list 
    print(f"player {vote_out}  is voted out")
    print("vote ends")
    alive_list.remove(vote_out)
    victim_list.append(vote_out)
    print(f"player {alive_list} are alive")


#wait for player join the game
import queue 
print("waiting for players join the game...")
q=queue.Queue()
for i in range(1,7):
    q.put(i) #add item in the queue
while not q.empty():
    for i in range(1,7):
        sleep(randint(0,3))
        print(q.get(),end=" ")
        print("player",i,"joined the game")
print("game starts")
timer=3
for i in range(3):
    print(timer,end=" ")
    timer-=1
    sleep(1)

 
#create six players 
villager1=Villager()
villager2=Villager()
seer=Seer()
witch=Witch()
werewolf1=Werewolf()
werewolf2=Werewolf()

def show_symbol(player):
    if player.name=="villager1" or player.name=="villager2":
        villager1.card()
    elif player.name=="seer":
        seer.card()
    elif player.name=="witch":
        witch.card()
    elif player.name=="werewolf1" or player.name=="werewolf2":
        werewolf1.card()


role_list=[] #create an empty list 
role_list.extend([villager1,villager2,seer,witch,werewolf1,werewolf2]) #insert objects into the empty list

#randomly generat six play's roles and assign ID to each role
x=random.randint(0,5)
p1=role_list[x]
p1.playerid=1
role_list.pop(x) #pop() function to pop element from stack 

x=random.randint(0,4)
p2=role_list[x]
role_list.pop(x) #pop() function to pop element from stack 
p2.playerid=2

x=random.randint(0,3)
p3=role_list[x]
role_list.pop(x) #pop() function to pop element from stack 
p3.playerid=3

x=random.randint(0,2)
p4=role_list[x]
role_list.pop(x) #pop() function to pop element from stack 
p4.playerid=4

x=random.randint(0,1)
p5=role_list[x]
role_list.pop(x) #pop() function to pop element from stack 
p5.playerid=5

p6=role_list[0]
p6.playerid=6

#print each player's ID and his roles for judge to review:

print(f"player1 is: {p1.name} id is: {p1.playerid}") 
print(f"player2 is: {p2.name} id is: {p2.playerid}") 
print(f"player3 is: {p3.name} id is: {p3.playerid}") 
print(f"player4 is: {p4.name} id is: {p4.playerid}") 
print(f"player5 is: {p5.name} id is: {p5.playerid}")
print(f"player6 is: {p6.name} id is: {p6.playerid}")

alive_list=[p1.playerid,p2.playerid,p3.playerid,p4.playerid,p5.playerid,p6.playerid]
print(alive_list)
player_list=[p1,p2,p3,p4,p5,p6]
print(player_list)
player_type_list=[p1.type,p2.type,p3.type,p4.type,p5.type,p6.type]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#practice create a dictionary by the key list and the value list: 
#key list is the list of player id:alive_list
#value list is the list of player type:player_type_list

player_dict=dict(zip(alive_list,player_type_list))
print(player_dict)

#set that stores multiple role names in a set
playerset={"villager","villager","werewolf","werewolf","witch","seer"}


#players check their roles:
input("please verify your role, player1 check role, please press the enter bottum")
print(f"your role is: {p1.name}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

input("please verify your role, player2 check role, please press the enter bottum")
print(f"your role is: {p2.name}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

input("please verify your role, player3 check role, please press the enter bottum")
print(f"your role is: {p3.name}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

input("please verify your role, player4 check role, please press the enter bottum")
print(f"your role is: {p4.name}")

input("please verify your role, player5 check role, please press the enter bottum")
print(f"your role is: {p5.name}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

input("please verify your role, player6 check role, please press the enter bottum")
print(f"your role is: {p6.name}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


days=0
nights=0
victim_list=[]

human_count=0
god_count=0
wolf_count=0

for i in player_list: #here i is players class object in player_list
    if i.type=="human":
        human_count+=1
    elif i.type=="god":
        god_count+=1
    elif i.type=="wolf":
        wolf_count+=1
print(f"human:{human_count},god:{god_count},wolf:{wolf_count}")

#game begin, night starts everyone please close your eyes
while human_count>=1 and god_count>=1 and wolf_count>=1: 
#if the number of one alignemnt is zero, game ends and system will calculate the winner
    days+=1
    print("day"+str(days)+"~~~~~~~~~~~~~~~~~~~~~")

    nights+=1
    print(f"{nights} night begins")
    
    #Seer check one player's identity from the alive list
    if seer.playerid in alive_list:
        print("Seer please check one player's identity")
        print(f"player {alive_list} are alive")
        print("please enter a player ID from the alive list:")
        id = int(input())
        if not isinstance(id, int):
            raise TypeError("playerid must be integer")
        seercheck(id)
        print("Seer please close your eyes")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #Wolf choose one player to kill from the alive list
    print("wolf team wake up")
    print(f"player {alive_list} are alive")
    wolfattack() #call wolf attack function
    print("wolf team please close your eyes")
    print(f"player {alive_list} are alive")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #Witch
    #if witch.playerid in alive_list:
    print("witch wakes up")
    print("witch please choose to use cure or poison, you can only use one item at one night")
    victim = victim_list[-1] #the last id in the victim list is the person who is killed by the wolf team during the same night
    print(f"The victim is player{victim}")
    witch.save() #call witch make selection fucntion from the witch class
    witch_magic(victim) #call witch magic function to use cure or poison
    print(f"The alive players are: {alive_list}")
    print(f"The victims are: {victim_list}")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    
    #initialize the number of human,wolf,and god types in the alive list after every night 
    human_count=0
    god_count=0
    wolf_count=0

    for i in player_list: #here i is players class object in player_list
        if i.playerid in alive_list:
            if i.type=="human":
                human_count+=1
            elif i.type=="god":
                god_count+=1
            elif i.type=="wolf":
                wolf_count+=1
    print(f"human:{human_count},god:{god_count},wolf:{wolf_count}")

    #day starts
    sleep(2)
    print(f"{days} day begins")
    if len(victim_list)==0:
        print("no one died last night")
    else:
        print(f"player {victim_list} out")

    print(f"player {alive_list} are still alive")
    print("The remaining player please speak in turn")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("please vote one player to exile")
    vote()

    #initialize the number of human,wolf,and god types in the alive list after vote in the day
    human_count=0
    god_count=0
    wolf_count=0

    for i in player_list: #here i is players class object in player_list
        if i.playerid in alive_list:
            if i.type=="human":
                human_count+=1
            elif i.type=="god":
                god_count+=1
            elif i.type=="wolf":
                wolf_count+=1
    print(f"human:{human_count},god:{god_count},wolf:{wolf_count}")

#final winner condition check
if human_count==0 or god_count==0 and wolf_count>=1:
    print("wolf team wins")
elif wolf_count==0 and human_count>=1 or god_count>=1:
    print("human team wins")
else:
    print("game ends,draw")

