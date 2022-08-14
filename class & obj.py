from datetime import date
class Customer:
	def __init__( self, name , age , food, street, city, state , zipcode) :
		self.name = name
		self.age = age
		self.food = food
		self.street = street
		self.city = city
		self.state = state
		self.zipcode = zipcode
P1 = Customer("Jance", 18 , "cheeseburger", "ranganadhan street", "chennai","TamilNadu",565276)

P2 = Customer("Joel", 19, "friedchicken","Vinayaga street","chennai","TamilNadu",896516)

P3 = Customer("Jenilie", 18, "pizza", "valluvar street","chennai","TamilNadu", 765389)

print(P1.name, ",", P1.age)
print(P1.food)
print(P1.street, ",",P1.city, ",",P1.state,",",P1.zipcode)

