"""
##  make a random number generator using 
## make a todo list 
## make a basic chatbot using NTLK
""" 

# Random number generator
import random as rn

def respons_e():
    print("Would you lie to try again?\n")
    response=int(input("Enter either 1 for continuing 2 to quit the game\n"))

    if response==1:
        attempt=0
        game_play()
    else:           
        print("Tnanks for playing")
        return
    
           
def repons_e1():
    print("All attempts are used up, sorry!!,Would you like to try again??")
    print("\n")
    response= int(input("Enter either 1 for playing again or 2 for terminating the game\n" ))
    print("\n")
    if response==1:
        attempt=1
        game_play()
    else:
        print("Thanks for playing")
        return
        
    


#amin exec method

def game_play():
    print("You get 3 chacnes to play")
    x=rn.randint(1,3)
    max_attempt=3
    attempt=0
    while attempt<max_attempt:
        attempt=attempt+1
        if attempt>3:
            break
        print("Enter the magic number")
        num=int(input())

        if x>num:
            print("number is Too low")
    
        elif x<num:
            print("Number is Too high")
    
        elif x==num:
            print("Yay!!, You Won\n")
            respons_e()
            
           
    else :
        repons_e1()
        
       
          
game_play()

        
    


