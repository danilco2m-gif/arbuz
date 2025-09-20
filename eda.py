class Product:
    def__init__ (self, name, price available=true):
       self.name = name
       self.price = price
       self.avaible =available 
    
    def__str_(self):
    status = "est)"if self.available else "netuu("
    return f"{self.name} - {self.price} грн ({status})"

class Cart:
    def__init__(self):
       self.items = []
    
    def add(self, product):
        if product.avaible
          self.items.append(Product)
          
        else:
           print(f"{product.name} not avaible ")
    def remove(self, index):
       if 0 <= index < len(self.items):
          self.items.pop(index)
          

    
    def show(self):
        if not self.items:
            print("oreooo")
        else:
            for i, p in enumerate(self.items, 1):
                print(f"{i}. {p}")
            print(f"suma: {self.total()} грн")
        
        products  = [
           product (Iphone s, 30)
           product ( nokia 3310, 10)
           product ( earpods 1, 5)
           product ( samsung note 7, 22)
           product ( nechego , 0, available=false) 
        ]

cart = Cart()

while True:
    cmd = input("\n[a]dobavuty [r]ydalit [s]pokasat: ").strip().lower()


    elif cmd == "r":
        print("\n=tovary:")
        cart.show()
        num = int(input("chislo tovarov" \
        ": ")) - 1


