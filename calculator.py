>>> class GroceryList(dict):

>>>def __init__(self):
    	self = {}

>>>def addToList(self, item, price):
            self.update({item:price})

>>>def Total(self):
		total = 0
		for items in self:
			total += (self[items])*.07 + (self[items])
		return total


>>>def Subtotal(self):
		subtotal = 0
		for items in self:
			subtotal += self[items]
		return subtotal

>>>def returnList(self):
		return self


>>>List1 = GroceryList()

>>>List1.addToList("milk",4)
>>>List1.addToList("eggs", 3)
>>>List1.addToList("spinach", 3)


print List1.Total()
print List1.Subtotal()
print List1.returnList()


print

>>>List2 = GroceryList()

>>>List2.addToList('cheese', 10.50)
>>>List2.addToList('carrots', 25.30)
>>>List2.addToList('tomatoes', 20.60)

print List2.Total()
print List2.Subtotal()
print List2.returnList()

