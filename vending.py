#Author: Sreekar Ravavarapu
#Email: sravavarapu@umass.edu
#Spire ID: 34515445

class VendingMachine:
    def __init__(self):
        self.inventory = {}
        self.balance = 0.0
        self.total_sales = 0.0
        self.sales_history = []

    def add_item(self, name, price, quantity):
        price = round(price, 2)
        if name in self.inventory:
            self.inventory[name]['price'] = price
            self.inventory[name]['quantity'] += quantity
        else:
            self.inventory[name] = {'price': price, 'quantity': quantity}
        print(f"{quantity} {name}(s) added to inventory")

    def get_item_price(self, name):
        if name in self.inventory:
            return self.inventory[name]['price']
        else:
            print("Invalid item")
            return None

    def get_item_quantity(self, name):
        if name in self.inventory:
            return self.inventory[name]['quantity']
        else:
            print("Invalid item")
            return None

    def list_items(self):
        if not self.inventory:
            print("No items in the vending machine")
        else:
            items = sorted(self.inventory.items(), key=lambda self: self[0])
            print("Available items:")
            for name, details in items:
                print(f"{name} (${details['price']}): {details['quantity']} available")

    def insert_money(self, amount):
        if amount in [1.0, 2.0, 5.0]:
            self.balance += amount
            self.balance = round(self.balance, 2)
            print(f"Balance: {self.balance:.2f}")
        else:
            print("Invalid amount")

    def purchase(self, name):
        if name not in self.inventory:
            print("Invalid item")
        elif self.inventory[name]['quantity'] == 0:
            print(f"Sorry {name} is out of stock")
        elif self.inventory[name]['price'] > self.balance:
            print(f"Insufficient balance. Price of {name} is {self.inventory[name]['price']}")
        else:
            self.inventory[name]['quantity'] -= 1
            self.balance -= self.inventory[name]['price']
            self.balance = round(self.balance, 2)
            self.total_sales += self.inventory[name]['price']
            self.total_sales = round(self.total_sales, 2) 
            self.sales_history.append((name, self.inventory[name]['price']))
            print(f"Purchased {name}")
            print(f"Balance: {self.balance:.2f}")

    def output_change(self):
        if self.balance > 0:
            print(f"Change: {self.balance:.2f}")
            self.balance = 0.0
        else:
            print("No change")

    def remove_item(self, name):
        if name in self.inventory:
            del self.inventory[name]
            print(f"{name} removed from inventory")
        else:
            print("Invalid item")

    def empty_inventory(self):
        self.inventory.clear()
        print("Inventory cleared")

    def get_total_sales(self):
        return self.total_sales

    def stats(self, N):
        recent_sales = {}
        for item, price in reversed(self.sales_history[-N:]):
            if item in recent_sales:
                recent_sales[item] = (recent_sales[item][0] + price, recent_sales[item][1] + 1)
            else:
                recent_sales[item] = (price, 1)

        if not recent_sales:
            print("No sale history in the vending machine")
        else:
            print(f"Sale history for the most recent {min(N, len(self.sales_history))} purchase(s):")
            for item, (total_sale, num_purchases) in sorted(recent_sales.items()):
                print(f"{item}: ${total_sale:.2f} for {num_purchases} purchase(s)")
