number_of_birds = 5
arr = [1,1,2,2,3]

def migrate(arr, number_of_birds):
	max_type_sight = 0
	birds_count = {}
	for x in range(0, number_of_birds):
		