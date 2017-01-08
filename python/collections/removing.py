
list_words =[
'apple',
'apricot',
'avocado',
'banana',
'bilberry',
'blackberry',
'blackcurrant',
'blueberry',
'boysenberry',
'currant',
'cherry',
'cherimoya',
'cloudberry',
'coconut',
'cranberry'
]

new_list=[]

list_num=len(list_words)

try:
	#new_list.append(list_words.remove(word))	
	for word in list_words:
		list_words.remove(word)
		list_num=len(list_words)-1

except ValueError:
	print("There is an error")

print(list_words)
print('\n')
print(new_list)