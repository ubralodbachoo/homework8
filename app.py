#1
class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} lari damatebulia")
        else:
            print("arasworia tanxaa")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount < self.__balance:
                self.__balance -= amount
                print(f"angarishidan chamogewrat {amount} lari")
            else:
                print("arasakmarisi tanxaa")
        else:
            print("araswori tanxa sheiyvanet")

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

acc = BankAccount("bacho", 1000)
print(f"owner: {acc.get_owner()}")
print(f"balance: {acc.get_balance()}₾")

acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)  # ეს არ გამოვა
print(f"balance now: {acc.get_balance()}₾")

#2
class ShoppingCart:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        if isinstance(other, ShoppingCart):
            return len(self) == len(other)
        return False


cart1 = ShoppingCart(["ვაშლი", "მსხალი"])
cart2 = ShoppingCart(["ბანანი", "ატამი"])
print("Cart1 == Cart2:", cart1 == cart2) 

cart3 = ShoppingCart(["კარაქი", "ხილი", "ნაყინი"])
print("Cart1 == Cart3:", cart1 == cart3)
print("Cart2 == Cart3:", cart2 == cart3)

cart4 = ShoppingCart(["მაწონი", "ბოსტნეული"])
print("Cart1 == Cart4:", cart1 == cart4)
print("Cart3 == Cart4:", cart3 == cart4)

#3
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int

    def is_clasic(self):
        return self.year < 1970

book1 = Book("vefxisttyaosani", "shota rustaveli", 1200)
print(book1.is_clasic())

#4
class Person:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print(f"Person removed: {self.name}")

human = Person("bacho")

del human
import gc
gc.collect()

#6
class CustomList:
    def __init__(self, items=None):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __iter__(self):
        return iter(self.items)


lst = CustomList([10, 20, 30, 40])

print("pirveli elementi", lst[0])
lst[1] = 25
print("მეორე ელემენტის შეცვლის შემდეგ:", lst[1])

#7
class Refrigerator:
    def __init__(self):
        self.items = []

    def __contains__(self, item):
        return item in self.items
    def __str__(self):
        return f"Fridge with {len(self.items)} items"

    def __del__(self):
        print("Fridge deleted da igi")

fridge = Refrigerator()

fridge.items.extend(["milk", "eggs", "cheese"])
print("Milk in fridge?", "milk" in fridge)
print(fridge)
del fridge



