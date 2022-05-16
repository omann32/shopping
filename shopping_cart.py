import time



def add_cart(mycart):
  selection = input("What item would you like to purchase? ").title()
  price = input(f"What is the price of your {selection}? ")
  items = input(f"How many of the {selection} do you want? ")
  total = float(price) * float(items)
  mycart[selection]= [items, price]
  print(f"You have added:Item {items} {selection}(s), totaling ${total:.2f} ")
 

def remove_cart(mycart):
    selection = input('What would you like to remove? ').title()
    if len(mycart) < 1:
        print('Wait, you have nothing is in the cart')
    
    
    elif selection not in mycart:
        print(f"{selection} is not in your cart. We can try adding it if you want.") 
        selection2 = input(f"do you want to add {selection}? yes or no?")
        if selection2 == 'yes':
            price = input(f"What is the price of your {selection}? ")
            items = input(f"How many of the {selection} do you want? ")
            total = float(price) * float(items)
            mycart[selection]= [items, price]
            print(f"You have added:Item {items} {selection}(s), totaling ${total:.2f} ")
            

        
    else:
        del mycart[selection]
        print(f"{selection} has been put back on the shelf.")
    

def check_total(mycart):
    print ("{:<10} {:<10} {:<10} {:<10}".format('Quantity', 'Item', 'Price per', 'Total'))
    
    for key, value in mycart.items(): 
        total = float(value[0]) * float(value[1])
        print ("{:<10} {:<10} {:<10} {:<10}".format(int(value[0]), key, float(value[1]), "{:.2f}".format(total)))
        
    
  
def clear_cart(mycart):
    selection = input('Are you sure you want to empty the whole cart? yes or no')
    while selection not in {'yes' or 'no'}:
        print('yes or no')
    if selection == 'yes':
        mycart.clear()

        
        


    




def game():
    time.sleep(0)
    print('Hello, Welcome to John\'s Fresh Produce.')
    time.sleep(2)
    print('--------Let\'s Start Shopping--------')
    time.sleep(2)
    shopping_cart = {}
    choices = {'add', 'remove', 'check total', 'clear cart', 'quit'}
    while True:
        selection = input('What would you like to do?: Add, Remove, Check Total, Clear Cart, or Quit ').lower()
        while selection not in choices:
            selection = input('Let\'s try again...... Add, Remove, Check Total, Clear Cart, or Quit ').lower()
        
        if selection == 'add':
            add_cart(shopping_cart)
        elif selection == 'remove':
            remove_cart(shopping_cart)
        elif selection == 'check total':
            check_total(shopping_cart)
        elif selection == 'clear cart':
            clear_cart(shopping_cart)
        else: 
          selection == 'quit'
          break     
       
    print('I hope it\'s been a pleasure shopping here, thank you for your business')
    print ("{:<10} {:<10} {:<10} {:<10}".format('Quantity', 'Item', 'Price per', 'Total'))
    
    for key, value in shopping_cart.items(): 
        total = float(value[0]) * float(value[1])
        print ("{:<10} {:<10} {:<10} {:<10}".format(int(value[0]), key, float(value[1]), "{:.2f}".format(total)))
        





game()



