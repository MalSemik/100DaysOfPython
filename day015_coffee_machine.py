MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
}


class CoffeeMachine:
    def __init__(self):
        self.resources = resources
        self.profit = 0

    def _print_report(self):
        print(f"""
        Water: {self.resources["water"]}ml
        Milk: {self.resources["milk"]}ml
        Coffee: {self.resources["coffee"]}g
        Money: ${self.profit}
        """)

    def _turn_off(self):
        print("The coffee machine will now switch off.")

    def _check_resources(self, order):
        if self.resources["water"] >= MENU[order]["ingredients"]["water"] and self.resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
            if "milk" in MENU[order]["ingredients"].keys():
                if self.resources["milk"] >= MENU[order]["ingredients"]["milk"]:
                    return True
            else:
                return True
        return False

    def _accept_coins(self):
        "quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01"
        num_quarters = int(input("How many quarters? "))
        num_dimes = int(input("How many dimes? "))
        num_nickles = int(input("How many nickles? "))
        num_pennies = int(input("How many pennies? "))
        return [num_quarters, num_dimes, num_nickles, num_pennies]

    def _calculate_value(self):
        coins = self._accept_coins()
        value = coins[0] * 0.25 + coins[1] * 0.1 + coins[2] * 0.05 + coins[3] * 0.01
        return value

    def _check_transaction_successful(self, order):
        if self._calculate_value() >= MENU[order]["cost"]:
            self.profit += MENU[order]["cost"]
            return True

    def _make_coffee(self, order):
        print(f"Making {order} in progress...")
        self.resources["water"] -= MENU[order]["ingredients"]["water"]
        self.resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
        if "milk" in MENU[order]["ingredients"].keys():
            self.resources["milk"] -= MENU[order]["ingredients"]["milk"]

        print("Your coffee is done. Please collect your order.")
        new_order = input("Would you like to make another order? Type 'y' or 'n': ")
        if new_order == "y":
            self.get_order()
        else:
            self._turn_off()

    def get_order(self):
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "report":
            self._print_report()
        elif order == "off":
            self._turn_off()
        elif order in ["espresso", "latte", "cappuccino"]:
            if self._check_resources(order):
                if self._check_transaction_successful(order):
                    self._make_coffee(order)
                else:
                    print("Not enough money.")
            else:
                print("Not enough resources.")
        else:
            print("Incorrect choice")
            self.get_order()


cm = CoffeeMachine()
cm.get_order()
