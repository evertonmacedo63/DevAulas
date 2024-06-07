def new_func():
    x = new_func1()
    if x > 8 :
        print("True")
        Sinal = True
    else :
        print("False")
        Sinal = False
    print ("Sinal= ", Sinal)

def new_func1():
    x = int(input(f"Digite um numero entre 7 e 10:"))
    return x

new_func() 
