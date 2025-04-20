# first we ask the customer for what do they want( pizza, burger,sandwich)
# based on the input we create an pizza/burger/sw object
# step1 : we ask the user for the base and mention the price
# step2 : then we ask for the toppings
# step3 : we populate the price along with the tax and add it to the cart along with the item


class Cart:
    def __init__(self,elements):
        self.cartdict=[]
        self.cartdict.append(elements)
        pass


class FoodItem: 
    def __init__(self):
        pass
    def get_price(self):
        pass

class Pizza(FoodItem):
    def __init__(self):
        self.foodtype="Pizza"
        self.base_price=8
    def get_description(self):
        return self.foodtype

    def get_price(self):
        return self.base_price
        
class Burger(FoodItem):
    def __init__(self):
        self.foodtype="Burger"
        self.base_price=6
    
    def get_price(self):
        return self.base_price
    
class Sandwich(FoodItem):
    def __init__(self):
        self.foodtype="Sandwich"
        self.base_price=10
    def get_price(self):
        return self.base_price
    

class Sauce(FoodItem):
    def __init__(self,fooditem:FoodItem):
        self.fooditem=fooditem
    
class Alfredo(Sauce):
    def __init__(self, fooditem:FoodItem):
        self.fooditem=fooditem
    
    def get_price(self):
        return self.fooditem.get_price()+1.25
    
class Marinara(Sauce):
    def __init__(self,fooditem:FoodItem):
        self.fooditem=fooditem
    def get_price(self):
        return self.fooditem.get_price()+1.89
        



class Toppings(FoodItem):
    def __init__(self,fooditem:FoodItem):
        self.fooditem=fooditem
    


class Olives(Toppings):
    def __init__(self,fooditem:FoodItem):
        self.fooditem=fooditem

    def get_price(self):
        return self.fooditem.get_price()+0.25

class Onions(Toppings):
    def __init__(self,fooditem:FoodItem):
        self.fooditem=fooditem

    def get_price(self):
        return self.fooditem.get_price()+0.55
    
class Tomatoes(Toppings):
    def __init__(self,fooditem:FoodItem):
        self.fooditem=fooditem

    def get_price(self):
        return self.fooditem.get_price()+0.15
    
# added a topping and getting the correct price, need to check for more toppings

main_items={
    1:"Pizza",
    2:"Burger",
    3:"Sandwich"
}

sauce_items={
    1:"Alfredo",
    2:"Marinara"
    
}

toppings_items={
    1:"Olives",
    2:"Onions",
    3:"Tomatoes"
}

if __name__=="__main__":
    print(main_items)
    base_choice=int(input("Choose among the following:"))
    if base_choice==1:
        order=Pizza()
        print(order.get_price())
    if base_choice==2:
        order=Burger()
        print(order.get_price())
    if base_choice==3:
        order=Sandwich()  
        print(order.get_price()) 
    
    print(sauce_items)
    sauce_choice=int(input("Choose among the following:"))
    if base_choice==1:
        order=Alfredo(order)
        print(order.get_price())
    if base_choice==2:
        order=Marinara(order)
        print(order.get_price())

    
