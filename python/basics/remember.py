def remember(thing):
	#open a file
	#file = open("database.txt","w") : truncate or delate the file
	file = open("database.txt","a")
	#write to a file
	file.write(thing+'\n')
	#close the file
	file.close()
	#pass


if __name__=="__main__":
	remember(input("What do you wanna remember? : "))

#with open("database.text","a") as file:
#	file.write(thing+'\n')