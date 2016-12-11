import sys

def remember(thing):
	#open a file
	#file = open("database.txt","w") : truncate or delate the file
	with open("database.txt","a") as file:
		#write to a file
		file.write(thing+'\n')

def showdb():
	#open a file
	with open("database.txt" ,"r") as file:
		#print out each line
		for line in file:
			print(line)
		#close the file

if __name__=="__main__":
	if sys.argv[1].lower()=='--list':
		showdb()
	else:
		remember(' '.join(sys.argv[1:]))

			#input("What do you wanna remember? : "))

