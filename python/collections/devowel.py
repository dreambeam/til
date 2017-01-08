
fruits_names =[ 'Apple', 'Apricot','Avocado', 'Ammanda']


vowels =list('aeoui')

output =[]

def devowler():

	for fruit in fruits_names:
		list_fruits = list (fruit.lower())
		#print(fruit.lower())
		for vowel in vowels:
			while True:
				try:
					list_fruits.remove(vowel)

				except:
					break
		output.append(''.join(list_fruits).capitalize())
	#print(list_fruits)
	print(output)


devowler()