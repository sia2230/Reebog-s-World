def turn_right():
    for i in range (2):
        turn_left()
    
while(True):
    if at_goal():
        break
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
        if wall_in_front():
            turn_right()
            
    

        
    


