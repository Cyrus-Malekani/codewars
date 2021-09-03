# https://www.codewars.com/kata/5a1a76c8a7ad6aa26a0007a0

def reducer(buffer):
    while len(buffer) > 1:
        reduce = 0
        
        for i in range(0,len(buffer)):
            reduce += int(buffer[i])
        
        buffer = str(reduce)

    return int(buffer)

def life_path_number(birthdate):
    lst = birthdate.split('-')
    
    year = lst[0]
    month = lst[1]
    day = lst[2]
        
    year = reducer(year)
    month = reducer(month)
    day = reducer(day)
    
    life_path_number = reducer(str(year+month+day))
    
    return life_path_number
