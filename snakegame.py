from turtle import*
from random import randrange
from freegames import square,vector     

food = vector(0,0)
snake = [vector(10,0)]
aim = vector(0,-10)
turtle.bgcolor('turquoise')

def change(x,y):  # x and y axis
    "change snake direction"
    aim.x = x
    aim.y = y

def inside(head):    # boundary values
    "return true if head inside boundaries"
    return -200 < head.x<190 and -200 < head.y < 190  

def move():            #for movement of the snake 
    "Move snake forward one segment"   
    head = snake[-1].copy()        #forward movement value 
    head.move(aim)
    if not inside(head) or head in snake:
        square(head.x,head.y,9,'red')
        update()
        return

    snake.append(head)

    if head==food:       # conditions
        print('snake:',len(snake))    
        food.x = randrange(-15,15)*10
        food.y = randrange(-15,15)*10
    else:
        snake.pop(0)    

    clear()

    for body in snake:     #snake is combination of squares
        square(body.x,body.y,9,'black')

    square(food.x,food.y,9,'orange') 
    update()
    ontimer(move, 100)


hideturtle()
tracer(False)   
listen()      
onkey(lambda: change(10,0),'Right')    
onkey(lambda: change(-10,0),'Left')
onkey(lambda: change(0,10),'Up')
onkey(lambda: change(0,-10),'Down')
move()
done()
