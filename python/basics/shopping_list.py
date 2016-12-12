#def shopping_list():
#modified to write and read from file
def show_help():
	print("""
	Type 'DONE' when you are done
	Type 'SHOW' to view list of item
	Type 'HELP' to get some help """)

def show_list():
	print("Here is your list:")
	with open("sdata.txt") as file:
		#for item in list_items:
		for item in file:
			print(item)

#def add_item(item):
#	list_items.append(item)

def add_item(item):
	with open("sdata.txt","a") as file:
		file.write(item+'\n')

#list_items =[]

print("Enter the Shopping List: ")
print("Enter DONE if no more item")

show_help()

while True:
	item = raw_input("> ")

	if item == 'DONE':
		show_list()
		break

	elif item == "HELP":
		show_help()
		continue

	elif item == 'SHOW':
		show_list()
		continue

	add_item(item)

	#list_items.append(item)



