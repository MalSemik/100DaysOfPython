MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

COINS = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickle": 0.05,
    "penny": 0.01
}

resources = {"water": 300, "milk": 200, "coffee": 100}


class CoffeeMachine:
    def __init__(self, resources):
        self.resources = resources
        self.profit = 0

    def _print_report(self):
        print(
            f"""
        Water: {self.resources["water"]}ml
        Milk: {self.resources["milk"]}ml
        Coffee: {self.resources["coffee"]}g
        Money: ${self.profit}
        """
        )

    def _turn_off(self):
        print("The coffee machine will now turn off.")

    def _check_resources(self, order):
        for ingredient in MENU[order]["ingredients"].keys():
            if self.resources[ingredient] < MENU[order]["ingredients"][ingredient]:
                return False
        return True

    def _make_payment(self):
        inserted_amount = 0
        for coin, value in COINS.items():
            inserted_amount += int(input(f"How many {coin}s? ")) * value # TODO: it should print pennies not pennys but I don't know how to do it
        print(inserted_amount)
        return inserted_amount

    def _make_transaction(self, order):
        value = self._make_payment()
        if value >= MENU[order]["cost"]:
            self.profit += MENU[order]["cost"]
            return True
        else:
            print("Not enough money.")
            return False

    def _new_order(self):
        new_order = input("Would you like to make another order? Type 'y' or 'n': ")
        if new_order == "y":
            self.get_order()
        else:
            self._turn_off()

    def _make_coffee(self, order):
        print(f"Making {order} in progress...")
        for ingredient in MENU[order]["ingredients"].keys():
            self.resources[ingredient] -= MENU[order]["ingredients"][ingredient]
        print("Your coffee is done. Please collect your order.")
        self._new_order()

    def get_order(self):
        order = input(f"What would you like? {tuple(MENU.keys())}: ")
        if order == "report":
            self._print_report()
            self._new_order()
        elif order == "off":
            self._turn_off()
        elif order in MENU:
            if self._check_resources(order):
                if self._make_transaction(order):
                    self._make_coffee(order)
                else:
                    self._new_order()
            else:
                print("Not enough resources.")
                self._turn_off()
        else:
            print("Incorrect choice")
            self.get_order()


cm = CoffeeMachine(resources)
cm.get_order()
