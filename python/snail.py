# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(snail_map):
    len_x = len(snail_map[0])
    len_y = len(snail_map)
    
    res = []
    x = 0
    y = 0
    circle = 0
    
    direction = 'right'
    
    for i in range(0,len_x*len_y):
        res.append(snail_map[y][x])
        
        if x == circle-1 and y == circle:
            direction = 'right'
        elif x == len_x-1-circle and y < len_y-1-circle:
            direction = 'down'
        elif y == len_y-1-circle and x == len_x-1-circle:
            direction = 'left'
        elif y == len_y-1-circle and x == 0+circle:
            direction = 'up'
            circle += 1
        
        if direction == 'right' and x != len_x-1:
            x+=1
        elif direction == 'down' and y != len_y-1:
            y+=1
        elif direction == 'left' and x != 0:
            x-=1
        elif direction == 'up' and y != 0:
            y-=1
        
    return res
