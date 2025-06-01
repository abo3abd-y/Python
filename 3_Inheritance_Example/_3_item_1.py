import csv

class Item:
    pay_rate = 0.8 
    all = [] 
    def __init__(self, name : str, price : float, quantity = 0):
        
        print(f"An instance created: {name}")
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        
        
        self.__name = name # this is an attribute that should not be changed 
        self.__price = price
        self.quantity = quantity

    
        Item.all.append(self) 


    @property
    def price(self):
        return self.__price
    
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value


    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        Regards, JimShapedCoding
        """
    

    def __send(self): # we can also do this for methods where users cannot use this directly
        pass

    def send_email(self):
        self.__connect('hello there')
        self.__prepare_body()
        self.__send()


    @property
    def name(self): 
        return self.__name
    
    @name.setter # im basically telling python that i want to set new values for name
    def name(self, new_val): # the point of this is to control the logic and control what to put in those attributes and controling and restricting what you put in that variable
        if len(new_val) > 10:
            raise Exception("The name is too long") 
        else:
            self.__name = new_val

    def calculate_total_price(self): 
        return self.__price * self.quantity
    
    

    @classmethod
    def instantiate_from_csv(cls):
        with open('3_data_example_1.csv', 'r') as f:
            reader = csv.DictReader(f) 
            items = list(reader) 
        
        for item in items:
            print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
    @staticmethod
    def is_integer(num):
       
        if isinstance(num, float): 
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    @property # this basically allows the following to be read like an attribute instead of a method
    def read_only_name(self):
        return "Hey, you called the read_only_name function"


