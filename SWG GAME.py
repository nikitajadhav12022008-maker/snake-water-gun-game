#snake water and gun game:
import random as rd
print("enter 1 for snake/2 for water/3 for gun:")
print("lets start the game!!!")
print("====================")

while True:
    a = int(input("enter your choice:"))
    b = rd.randint(1,3)
    if(a == b):
        print("DRAW!!")
    elif(a == 1 and b == 2):
        print("you win!!!")
    elif(a == 2 and b == 1):
        print("you loss!!")
    elif(a == 3 and b == 1):
        print("you won!!")
    elif(a == 1 and b == 3):
        print("you loss!!")
    elif(a == 2 and b == 3):
        print("you won!!")
    else:
        print("sorry for inconvinience please try again!!!!!")