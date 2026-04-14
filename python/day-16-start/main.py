#import turtle
#timmy = turtle.Turtle()
#OR:
import turtle
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral3")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
#table.align = "l"
#print(table)

#PROJECT DAY 16: BUILDING COFFEE MACHINE IN OOP
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

#TODO-2: Check Resources Sufficient?
coffee_order = True
while coffee_order:
  options = menu.get_items()
  order = input(f"What would you like to drink? ({options}) ").lower()
  if order == "off":
    coffee_order = False
    break
  elif order == "report":
#TODO-1: Print Report
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(order)
    if coffee_maker.is_resource_sufficient(drink):
#TODO-3: Process Coins
#TODO-4: Check Transaction Successful?
    if money_machine.make_payment(drink.cost):
#TODO-5: Make Coffee
      coffee_maker.make_coffee(drink)
