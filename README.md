# WolfKillProgram-
This project creates a simple “Wolf Kill” game program for the judger’s interface using python. 
This program is used for the judger to lead the game, assign roles to players, and calculate the condition of victory.

# Example gaming process walk-through:
![image](https://github.com/xinyan30425/WolfKillProgram-/assets/91167901/fc37d8b8-8b9e-4f40-9d91-cf26602e61d3)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

wolf team wake up
player [1, 2, 3, 4, 5, 6] are alive
The alive players are: [1, 2, 3, 4, 5, 6]
werewolf please choose one player to attack from the alivelist:

enter 2
2
Wolf team choose to kill player 2
Victim list: [2]
wolf team please close your eyes
player [1, 3, 4, 5, 6] are alive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
witch wakes up
witch please choose to use cure or poison, you can only use one item at one night
The victim is player2
1.cure
2.poison
Enter 1
witch choose to cure
The alive players are: [1, 3, 4, 5, 6, 2]
The victims are: []
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
human:2,god:2,wolf:2
1 day begins
no one died last night
player [1, 3, 4, 5, 6, 2] are still alive
The remaining player please speak in turn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
please vote one player to exile
player 1 please vote
2
player 1 vote for 2
player 3 please vote
3
player 3 vote for 3
player 4 please vote
2
player 4 vote for 2
player 5 please vote
1
player 5 vote for 1
player 6 please vote
3
player 6 vote for 3
player 2 please vote
3
player 2 vote for 3
player 3  is voted out
vote ends
player [1, 4, 5, 6, 2] are alive

check the number of god, human, and wolf categories for the lived players after the voting session: since player3 is villager, the number of human is decreased by 1:
human:1,god:2,wolf:2

Game continues
day2~~~~~~~~~~~~~~~~~~~~~
2 night begins
Seer please check one player's identity
player [1, 4, 5, 6, 2] are alive
please enter a player ID from the alive list:
enter 5
you have checked player 5 identity is GOOD
Seer please close your eyes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
wolf team wake up
player [1, 4, 5, 6, 2] are alive
The alive players are: [1, 4, 5, 6, 2]
werewolf please choose one player to attack from the alivelist:
enter 4
Wolf team choose to kill player 4
Victim list: [3, 4]
wolf team please close your eyes
player [1, 5, 6, 2] are alive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
witch wakes up
witch please choose to use cure or poison, you can only use one item at one night
The victim is player4
2.poison
2
The alive players are: [1, 5, 6, 2]
please choose a player to poison:
enter 2
The alive players are: [1, 5, 6]
The victims are: [3, 4, 2]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
human:1,god:1,wolf:1

now we have 1 human, 1 god, and 1 wolf still alive
2 day begins
player [3, 4, 2] out
player [1, 5, 6] are still alive
The remaining player please speak in turn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
please vote one player to exile
player 1 please vote
1
player 1 vote for 1
player 5 please vote
1
player 5 vote for 1
player 6 please vote
3
player 6 vote for 3
player 1 is voted out
vote ends
player [5, 6] are alive
human:1,god:1,wolf:0
human team wins

Since player1 is werewolf, thus the number of werewolves is zero, the game ends and the winner is human team. (human team refers to both villagers and god)
![image](https://github.com/xinyan30425/WolfKillProgram-/assets/91167901/8814e5cf-98e6-42be-a00d-c64c34ab71c1)

