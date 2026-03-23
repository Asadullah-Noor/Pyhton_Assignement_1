class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Order:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def get_total(self):
        return sum(item.price for item in self.items)
# 🔥 Polymorphism starts here
class Customer:
    def calculate_bill(self, order):
        return order.get_total()
class RegularCustomer(Customer):
    def calculate_bill(self, order):
        return order.get_total()
class PremiumCustomer(Customer):
    def calculate_bill(self, order):
        total = order.get_total()
        return total * 0.9   # 10% discount
class VIPCustomer(Customer):
    def calculate_bill(self, order):
        total = order.get_total()
        return total * 0.8   # 20% discount


class Restaurant:
    def __init__(self):
        self.menu = []

    def add_menu_item(self, item):
        self.menu.append(item)
    def display(self):
        result = "Menu:\n"
        for item in self.menu:
          result += f"{item.name} - Rs.{item.price}\n"
        return result
# Create menu items
burger = MenuItem("Burger", 500)
pizza = MenuItem("Pizza", 1000)

# Create order
order = Order()
order.add_item(burger)
order.add_item(pizza)

# Customers
regular = RegularCustomer()
premium = PremiumCustomer()
vip = VIPCustomer()
print("Regular Bill:", regular.calculate_bill(order))
print("Premium Bill:", premium.calculate_bill(order))
print("VIP Bill:", vip.calculate_bill(order))
print("-------Restaurant Menu-------")
menu=Restaurant()
menu.add_menu_item(burger)
menu.add_menu_item(pizza)
print(menu.display())