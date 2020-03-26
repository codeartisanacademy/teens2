class SmartPhone:
    
    def __init__(self, brand, os, price, description):
        self.brand = brand
        self.os = os
        self.price = price
        self.description = description

    def __str__(self):
        return self.brand

    def get_discount_price(self, discount):
        final_price = self.price - (self.price * (discount/100))
        return final_price
    


iphone_x = SmartPhone('Apple iPhone X', 'iOS', 600, 'Maybe the best phone')

print(iphone_x)
print(iphone_x.get_discount_price(50))

