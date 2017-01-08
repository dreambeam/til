import os

list_item=[]

def clear():
	if os.name=='nt':
		os.system('cls')
	else:
		os.system('clear')

#show help function
def show_help():
	print('\n' + "Input the list of item you want to remember, comma separated, ")
	print("""

Input DONE to quit
Input HELP to display this message again
Input SHOW to display the list of items
		""")


#show list function
def show_list():
	count = 1
	for item in list_item:
		print("{} {} \n".format(count,item))
		count+=1

print("Input shopping items here \n")
show_help()

while True:
	item = input("> ")

	if item=='DONE':
		clear()
		print("Here is your shopping list: ")
		show_list()
		break

	elif item=='HELP':
		clear()
		show_help()
		continue

	elif item=='SHOW':
		clear()
		show_list()
		continue

	else:
		list_item.extend((item.split(',')))
		show_list()

