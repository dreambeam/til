#def shopping_list():

def show_help():
	print("""
	Type 'DONE' when you are done
	Type 'SHOW' to view list of item
	Type 'HELP' to get some help """)

def show_list():
	print("Here is your list:")
	for item in list_items:
		print(item)

def add_item(item):
	list_items.append(item)
	print("New item added {}. number{}".format(item,len(list_items)))

list_items =[]

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




