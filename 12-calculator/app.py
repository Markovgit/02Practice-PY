# add 2 numbers 
def add(x,y):
    return x+y

# subtract one number from another 
def subtract(x,y):
    return x-y

# multiply two numbers together
def multyply(x,y):
     return x*y
 
 # divide one number by another
def divide(x,y):
     return x/y
 
 #selection
print("Select the arithmetic operation  you would like to perform:")
print("to ADD press 1 ")
print("to SUBTRACT press 2 ")
print("to MULTIPLY press 3 ")
print("to DIVIDE press 4 ")

while True: 
    choice = input("Enter choice (1/2/3/4):")
    if choice in ('1', '2','3','4'): 
        num1=float(input('Enter first Number :'))
        num2=float(input('Enter second Number :'))
        
        if choice == '1':            
            print(num1, "+", num2,"=",add(num1,num2))
        elif choice =='2':
            print(num1 , "-" , num2 , "=" ,subtract(num1,num2))  
        elif choice =='3':
            print(num1 , "*" , num2 , "=" ,multyply(num1,num2))  
        elif choice =='4':
            print(num1 , "/" , num2 , "=" ,divide(num1,num2))  
            
        break
    
    else:
          print("invalid input")  
            
                