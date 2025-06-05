from _3_item_1 import Item

class Phone(Item):

    def __init__(self,name:str, price:float, quantity=0,  broken_phones = 0): 
        super().__init__( 
        )
        assert broken_phones >= 0, f"Quantity {broken_phones} is not greater than or equal to zero"
        
        self.broken_phones = broken_phones