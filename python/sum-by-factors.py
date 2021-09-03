# https://www.codewars.com/kata/54d496788776e49e6b00052f

def prime_factors(n):
    i = 2
    n = abs(n)
    factors = {}
    
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] = 0
            
    if n > 1:
        factors[n] = 0
        
    return factors

def sum_for_list(lst):
    p_dict = {}
    res = []
    
    #Getting prime factors of every number and adding them to p_dict 
    for numbers in lst:
        for key in prime_factors(numbers): #Since the function returns a dictionary we can use the keys as iterator
            p_dict[key] = 0 #Just adding keys (prime factors) to the dictionary
    
    #Adding the values to the dict
    for number in lst:
        for prime in p_dict.keys():
            if number%prime == 0:
                p_dict[prime] += number
    
    #Adding dict key/value to a list to return desired type
    for key in p_dict:
        val = p_dict[key]
        res.append([key,val])
    
    res.sort() #Sorting the list
    return res
