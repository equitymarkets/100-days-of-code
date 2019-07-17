#Day 3 - Fibonacci in the while loop


def Fib_Func():
    
    
    number = input("Please enter a number ")
    		
    A = 0										
    B = 1
    C = 1
    D = B + C 
    E_array = []

    print(B)									#1
    E_array.append(B)
    print(C)									#1
    E_array.append(C)
    print(D)									#2
    E_array.append(D)




    while D < int(number):
        A = B
        B = C
        C = D
        D = C + B
        print(D)
        E_array.append(D)

    return(E_array)

	

