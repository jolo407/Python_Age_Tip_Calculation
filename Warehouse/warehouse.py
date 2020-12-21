#imports
from menu import print_menu, print_header, clear 
from homework import calculate_age, calculate_tip

#global vars

#functions





def register_product():
    # title, category, stock, price
    print_header(" Register a new Product")
    title = input("Please provide the Title ")
    category = input("Please provide the Category: ")
    stock = input("Please provide the Stock: ")
    price = input("Please provide the Price: ")

    







#instructions

opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input("PLease choose an option: ")

    if(opc == '1'):
        register_product()

    elif(opc =='a'):
        calculate_age()
    elif(opc =='b'):
        calculate_tip()



print("Good bye!!")
