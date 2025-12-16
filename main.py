#Create your team's csv file with 4 columns: 2 columns of item names and 2 columns of item prices
#Upload your team's csv file to the files section of this zylab (click on the icon to the left of the run button)

#Edit your team's store to use the csv file for your store's inventory data

from appJar import gui 

import pandas
grocerystoredf = pandas.read_csv("groceriesandprices.csv")
fruititems = list(grocerystoredf.Fruits)
fruitprices = list(grocerystoredf.FruitPrices)
vegetableitems = list(grocerystoredf.Vegetables)
vegetableprices = list(grocerystoredf.VegetablePrices)



#Function to greet the user and ask for a category
cart = " "
total = 0
def greet_user(greeting,sentinel,categoryq,readyq):
   canswer = ' '
   ranswer = sentinel
   print(greeting)
   while ranswer == sentinel:
       canswer = input(categoryq)
       ranswer = input(readyq)
   if canswer == "Fruits":
       fruit("Welcome to our Fruits section! Here are your choices:",fruititems,fruitprices,"Which fruit would you like or enter None? ")
   elif canswer == "Vegetables":
       vegetable("Welcome to our Vegetables section!  Here are your choices:",vegetableitems,vegetableprices,"Which vegetable would you like or enter None? ")
   else:
       print('Sorry, we do not carry that category.  See you next time! ')



#Function ask user to pick Fruits
def fruit(greeting, selection, prices, pickq):
   print(greeting)
   for item, price in zip(selection, prices):
      print(f"{item}: ${price:.2f}")
   fruitpick= input(pickq).strip()
   if fruitpick=="None":
      print("No fruit selected. Returning to main menu.")
      greet_user("Great!", "n", "What category would you like to browse (Fruits, Vegetables)? ", "Ready to browse (y/n)? ")
      return
   if fruitpick not in selection:
      print("Sorry, that fruit is not available.")
      return
   selectedfruitindex = selection.index(fruitpick)
   closing(selection[selectedfruitindex],prices[selectedfruitindex], "Enjoy your ")

#Function ask user to pick a Vegetable
def vegetable(greeting, selection, prices, pickq):
   print(greeting)
   for item, price in zip(selection, prices):
      print(f"{item}: ${price:.2f}")
   vegetablepick=input(pickq).strip()
   if vegetablepick=="None":
      print("No vegetable selected. Returning to main menu.")
      greet_user("Great!","n", "What category would you like to browse (Fruits, Vegetables)? ", "Ready to browse (y/n)? ")
      return
   if vegetablepick not in selection:
      print("Sorry, that vegetable is not available.")
      return
   selectedvegetableindex = selection.index(vegetablepick)
   closing(selection[selectedvegetableindex],prices[selectedvegetableindex], "Enjoy your ")

        
#Function to give user total price of purchase
def closing(pickeditem,price,goodbye):
   global cart
   global total
   cart = cart + " " + pickeditem
   total = total + price
   ttotal = total*1.09
   print("Your items so far:",cart)
   print("Your cost for the",pickeditem,"is $%.2f."%price)
   print("Your total cost is $%.2f."%total)
   print("Your total cost plus tax is $%.2f."%ttotal)
   print(goodbye+pickeditem+"!")
   more = input("Would you like to pick another item (y/n)? ")
   if more == "y":
       greet_user("Great!", "n", "What category would you like to browse (Fruits, Vegetables)? ", "Ready to browse (y/n)? ")
   else:
       print("Please pay $%.2f!"%ttotal)
       print("Your groceries:")
       for l in cart:
           print(l,end="")
       print()
       print("Enjoy your groceries!")
      
  
  
      
#greet_user("Welcome to our Grocery Store", "n", "What category would you like to browse (Fruits, Vegetables)? ", "Ready to browse (y/n)? ")


#Edit the elif sections below with appropriate button names for your team’s store and the corresponding function calls, first elif should be a call to the #greet_user function (move your initial greet_user function call to this spot), second elif should be a call to the function for your first product category #and third elif should be a call to your second product category (copy the function calls from your greet_user function definition if-elif-else function)

def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Hello":
        greet_user("Welcome to our Grocery store", "n", "What category would you like to browse (Fruits, Vegetables)? ", "Ready to browse (y/n)? ") 
    elif btn == "Fruits":
        fruit("Welcome to our Fruits section! Here are your choices:",fruititems,fruitprices,"Which fruit would you like or enter None? ")
    elif btn == "Vegetables":
         vegetable("Welcome to our Vegetables section!  Here are your choices:",vegetableitems,vegetableprices,"Which vegetable would you like or enter None? ")
    elif btn == "Close":
        app.infoBox("b1","Thank you for shopping!")   
    else:
        print('Pick a valid option')


app=gui("Main Menu","500x500")

#Replace “Welcome to Demo’s Main Menu” with a heading for your team’s gui

app.addLabel("title", "Welcome to Grocery's Main Menu")
app.setLabelBg("title", "orange")

#Find your team gif image, save to your project code folder, and replace k.gif
#with the image file name in the line below

app.addImage("decor","Grocery.gif")
app.setFont(18)

#change the first parameter of the addButton method in lines the following lines with names aligning with your team functions
#make sure they match the Button names in the press function above

app.addButton("Hello", press)
app.addButton("Fruits", press)
app.addButton("Vegetables", press)
app.addButton("Close", press)
app.addButton("Exit",press)
app.go() #displays the gui

