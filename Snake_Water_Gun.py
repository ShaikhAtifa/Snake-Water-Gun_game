'''
Snake Water Gun Game
RULES:
USER HAVE 3 CHOICES:
Snake,Water and Gun...
in snake Vs gun battel->gun kill snake hence GUN wins
in snake Vs water battel->snake drink water hence SNAKE wins
in water Vs gun battel->gun drown in water hence WATER wins
'''
#To generate computer choice automaticaly we have use random module 
import random

computer_ji=random.choice([1,-1,0])#Computers input
Users_choice=int(input("Enter One choice from  1 for \'Snake\'  -1 for \'Water\'  0 for \'Gun\'"))
Dict={1:'Snake',-1:'Water', 0:'Gun'}
print(f"\nYour choice:{Dict[Users_choice]}\ncomputers choice:{Dict[computer_ji]}")

#Now we have both choices
#lets decide the winner on given rules

if(computer_ji==Users_choice):
    print("Round Draw")
elif(Users_choice==1 and computer_ji==-1):
    print("You win!!")
elif(Users_choice==1 and computer_ji==0):
    print("You Lose:(")
elif(Users_choice==-1 and computer_ji==1):
    print("You Lose:(")
elif(Users_choice==-1 and computer_ji==0):
    print("You win!!")
elif(Users_choice==0 and computer_ji==-1):
    print("You lose:(")
elif(Users_choice==0 and computer_ji==1):
    print("You win!!")

else:
    print("Something went wrong\n choose valid input")