import random

def even_odd(num):
    # If % 2 is 0, the number is even.
    # Since 0 is falsey, we have to invert it with not.
    return not num % 2



def test_num():
	start = 5
	while start:
		numb = random.randint(1,99)
		if even_odd(numb) is True:
			print("{} is even".format(numb))
		elif even_odd(numb) is False:
			print("{} is odd".format(numb))
		start -= 1

test_num()