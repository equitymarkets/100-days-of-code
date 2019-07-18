#Day 3 - Fibonacci in the while loop


def Fib_Func():
    
    
    numb = int(input("How many times would you like to run the cycle?"))
    
    
    
    while numb > 0:
        
        number = input("Please enter a number ")
        
        A = 0										
        B = 1
        C = 1
        D = B + C 
        E_array = []
    
        print(B)									#1
        
        print(C)									#1
        
        print(D)									#2
        
    



        while D < int(number):
            A = B
            B = C
            C = D
            D = C + B
            print(D)
            E_array.append(float(D/C))
            
        numb -= 1
        
    return(E_array)
    
        
    
    
