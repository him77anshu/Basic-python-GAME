# Rock paper and scissors game !! 
import random
while True:
    choices=["rock","paper","scissors"]
    computer=random.choice(choices)
    player=None
    while player not in choices:
      player=input("rock , paper, scissors : ").lower()

    if(player==computer):
       print("Player: ",player)
       print("Computer : ",computer)
       print(" Tie !!")
    
    elif(player=="rock"):
       
       if(computer=="paper"):
          print("Player: ",player)
          print("Computer : ",computer)       
          print(" You lose !!")

       elif(computer=="scissors"):
           print("Player: ",player)
           print("Computer : ",computer) 
           print(" You Won !!")
    
    elif(player=="paper"):
       
       if(computer=="scissors"):
          print("Player: ",player)
          print("Computer : ",computer) 
          print(" You lose !!")
          
       elif(computer=="rock"):
           print("Player: ",player)
           print("Computer : ",computer)  
           print(" You Won !!")

    elif(player=="scissors"):
       
       if(computer=="rock"):
          print("Player: ",player)
          print("Computer : ",computer)
          print(" You lose !!")
          
       elif(computer=="paper"):
           
           print("Player: ",player)
           print("Computer : ",computer)
           print(" You Won !!")


    play=input("Play Again ? Yes/No: ").lower()
    if(play !="yes"):
       break
print("Bye !!")