#Functions, Code Blocks and While Loops
#Hurdle One
def right_turn():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    right_turn()
    move()
    right_turn()
    move() 
    turn_left()


for i in range(1, 7):
    jump()


#While Loop

