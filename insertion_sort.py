# Author @ Joseph Hein
# CS 3060 | Python Functions

def insertion_sort(data) :

	for k in range(1, len(data)):

		pos = k
		curvalue = data[k]

		while curvalue < data[pos-1] and pos > 0 : 
			data[pos] = data[pos - 1] 
			pos -= 1

		data[pos] = curvalue