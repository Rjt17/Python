class mobile:		#brand and price in init are parameters which get passed to attributes as values.
	def __init__(self, brand, price):
		self.brand = brand	#this is an attribute
		self.price = price	#this is an attribute

mob1=mobile("Apple",2000)
mob2=mobile("samsung",3000)