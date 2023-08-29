MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "kasa_money": 0,
}

def report():
    kasa_money = resources['kasa_money']
    print(f"Water : {resources['water']}\nMilk : {resources['milk']}\nCoffee : {resources['coffee']}\nMoney : ${kasa_money}")

def stoc(kahve):
    su = MENU[kahve]['ingredients']['water']
    kahv = MENU[kahve]['ingredients']['coffee']
    sut = MENU[kahve]['ingredients']['milk']
    if int(su) < resources['water'] and int(kahv) < resources['coffee'] and int(sut) < resources['milk']:
        resources['water'] -= su
        resources['coffee'] -= kahv
        resources['milk'] -= sut
        return True
    else:
        print("Sorry not enough stock")
        return False

def money(kahve):
    quarters = input("How many quarters?")
    dimes = input("How many dimes?")
    nickless = input("How many nickless")
    pennies = input("How many pennies?")

    ceyrek = int(quarters) / 4
    on = int(dimes) / 10
    bes = int(nickless) / 20
    bir = int(pennies) / 100
    toplam = ceyrek + on + bir + bes
    hesap = MENU[kahve]['cost']
    if toplam - hesap > 0:
        print(f"Here is ${toplam - hesap} in change.")
        print(f"Here is your {kahve} ☕️ Enjoy!")
        resources['kasa_money'] += toplam - hesap
    else:
        print("Sorry that's not enought money. Money refunded.")

off = False



while not off:
    inp = input("What would you like? (espresso/latte/cappuccino): ")

    if inp == "report":
        report()
    elif inp == "off":
        off = True
    elif inp == "espresso":
        if stoc('espresso'):
            money('espresso')
    elif inp == "latte":
        if stoc('latte'):
            money('latte')
    elif inp == "cappuccino":
        if stoc('cappuccino'):
            money('cappuccino')
