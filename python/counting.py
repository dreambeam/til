some_string = "I am that I am"

swords= some_string.split()

list_word =[]

for word in swords:
	list_word.append(word.lower())


print(list_word)

count =0
my_dict={}

for word in list_word:
	if word not in my_dict:
		count=1
		my_dict.update({word:count})
	else:
		count = my_dict[word]+1
		my_dict.update({word:count})

print(my_dict)