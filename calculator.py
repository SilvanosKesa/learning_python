print('Welcome user')
#welcoming message and first on screen
while True:
    name = input("What is your name? ").strip().title()
    if name =='':
        print('Invalid input!')
        continue
    else:
        print(f'Welcome, {name}')
        break

while True:
    #looping point
    point= input('Do you wish to use the calculator? (yes/no)').lower().strip()
    if point =='no':
        break

    #Resquesting operation
    print('Which operation would you like to perfom? \n 1: multiplication \n 2: power \n 3: division \n 4: addition \n 5: subtraction ')
    ask_operation = input()
    #multiplication
    if ask_operation == '1' or ask_operation =='multiplication' :
         x = (input("Enter number to multiply: "))
         y = (input('Enter the number to multiply by: '))
         try:
            x1 = float(x)
            y1 = float(y)
            print(f'{name},{x1} multiplied by {y1} is: ',x1 * y1)
         except: print("invalid input")

    #power
    elif ask_operation == '2' or ask_operation == 'power':
         x2 = input('Enter the the number you want to find the power of: ')
         y2 = input('Enter the power you want to raise the number to: ')
         try:
          x2_1 = float(x2)
          y2_1 = float(y2)
          print(f'{x2_1} raised to the power of {y2_1} is: ',pow(x2_1,y2_1))
         except: print('Please enter numerical values')

    #division
    elif ask_operation == '3' or ask_operation == 'division' :
         x3 = input('Enter the number to be divided: ')
         y3 = input('Enter the number you want to divide by: ')
         try:
             x3_1 = float(x3)
             y3_1 = float(y3)
             print(f'{x3_1} divided by {y3_1} is: ',x3_1/y3_1)
         except:print('Please enter numerical values')

    #addition
    elif ask_operation == '4' or ask_operation == 'addition':
         x4 = input('Enter the number you want to add: ')
         y4 = input('Enter the other number to add: ')
         try:
             x4_1 = float(x4)
             y4_1 = float(y4)
             print(f'{x4_1} plus{y4_1} is:',x4_1 + y4_1)
         except: print("Please enter numerical values")

    #subrtaction
    elif ask_operation =='5' or ask_operation == 'subtraction':
         x5 = input('Enter the number you want to subract from: ')
         y5 = input('Enter the value you want to subtract from the number above: ')
         try:
             x5_1 =float(x5)
             y5_1 =float(y5)
             print(f'{x5_1} minus {y5_1} is: ', x5_1 - y5_1)
         except: print('Please enter a numerical values')
    else : print('Please enter a valid option.')
print('Thank you for using the calculator, we hope you were satisfied')