from _3_item_1 import Item

item1 = Item("MyItem", 750)
# item1.name = "OtherItem"


print(item1.name) # calls the property "attribute". read-only attribute
#print(item1.__name) # this will produce an error because two underscores mean you cannot edit this
print(item1.read_only_name)



item1.name = "OtherItem" # this calls the new setter function that we created
print(item1.name)


# this idea of private and public attributes in programming is called encapsulation
print(item1.price)
item1.apply_increment(0.2)
print(item1.price)


