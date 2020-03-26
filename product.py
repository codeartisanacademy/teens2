class Product:
    
    def __init__(self, name, description, price, brand):
        self.name = name
        self.description = description
        self.price = price
        self.brand = brand
    
    def calculate_discount_price(self, discount):
        return self.price - (self.price * (discount / 100))


class Book(Product):

    def __init__(self, name, description, price, brand, author, total_pages):
        # required for class that inherits from another class
        super(Book, self).__init__(name, description, price, brand)
        self.author = author
        self.total_pages = total_pages

    def __str__(self):
        return self.name + " by " + self.author

# create a class for Computer that inherits from product

html_book = Book('Html for Beginner', 'Book for learning HTML', 12.5, 'Gramedia', 'John Doe', 230) 

print(html_book.calculate_discount_price(10))
        