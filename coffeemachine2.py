class Coffee():
    cups = 1
    def __init__(self, r_water, r_milk, r_beans, r_cash):
        self.r_water = r_water
        self.r_milk = r_milk
        self.r_beans = r_beans
        self.r_cash = r_cash

class CoffeeMachine():
    def __init__(self, water_s, milk_s, beans_s, cups_s,  cash_s):
        self.water_s = water_s
        self.milk_s = milk_s
        self.beans_s = beans_s
        self.cups_s = cups_s
        self.cash_s = cash_s

    def __str__(self):
        return f'The coffee machine has:\n{self.water_s} of water\n{self.milk_s} of milk\n{self.beans_s} of beans\n{self.cups_s} of cups\n{self.cash_s} of money'
        
    def add_supplies(self):
        print('Write how many ml of water do you want to add:')
        add_water = int(input())
        self.water_s += add_water
        print('Write how many ml of milk do you want to add:')
        add_milk = int(input())
        self.milk_s += add_milk
        print('Write how many grams of coffee beans do you want to add:')
        add_beans = int(input())
        self.beans_s += add_beans
        print('Write how many disposable cups of coffee do you want to add:')
        add_cups = int(input())
        self.cups_s += add_cups
    
    def take_cash(self):
        print('I gave you ${self.cash_s}')
        self.cash_s = 0
    
    def make_coffee(self, name):
        able = True
        if name == 'espresso':
            if self.water_s > espresso.r_water and self.milk_s > espresso.r_milk and self.beans_s > espresso.r_beans:
                print('I have enough resources, making you a coffee!')
                self.water_s -= espresso.r_water
                self.milk_s -= espresso.r_milk
                self.beans_s -= espresso.r_beans
                self.cups_s -= 1
                self.cash_s += espresso.r_cash
        elif name == 'latte':
            if self.water_s > latte.r_water and self.milk_s > latte.r_milk and self.beans_s > latte.r_beans:
                print('I have enough resources, making you a coffee!')
                self.water_s -= latte.r_water
                self.milk_s -= latte.r_milk
                self.beans_s -= latte.r_beans
                self.cups_s -= 1
                self.cash_s += latte.r_cash
        elif name == 'cappuccino':
            if self.water_s > cappuccino.r_water and self.milk_s > cappuccino.r_milk and self.beans_s > cappuccino.r_beans:
                print('I have enough resources, making you a coffee!')
                self.water_s -= cappuccino.r_water
                self.milk_s -= cappuccino.r_milk
                self.beans_s -= cappuccino.r_beans
                self.cups_s -= 1
                self.cash_s += cappuccino.r_cash
        else:
            return

def buy():
    options = ['espresso', 'latte', 'cappuccino']
    choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
    if choice == 'back':
        return
    CoffeeMachine.make_coffee(options[int(choice) - 1])

espresso = Coffee(250, 0, 16, 4)
latte = Coffee(350, 75, 20, 7)
cappuccino = Coffee(200, 100, 12 , 6)
vendor = CoffeeMachine(400, 540, 120, 9, 550)

while True:        
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action == 'buy':
        buy()
    elif action == 'fill':
        CoffeeMachine.add_supplies()
    elif action == 'take':
        CoffeeMachine.take_cash()
    elif action == 'remaining':
        print(vendor)
    elif action == 'exit':
        break