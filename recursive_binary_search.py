# Author @ Joseph Hein
# CS 3060 | Python Functions

def binary_search(data, item, offset) :
	last = len(data)
	first = 0
	middle = len(data) // 2

	if len(data) > 1 :
		if data[0] == item :
			position = 0
			return (position + offset)

		if data[middle] == item :
			return middle + offset

		elif item < data[middle] :
			data = data[:middle]
			return binary_search(data, item, offset)

		elif item > data[middle] :
			data = data[middle:last]
			offset += middle
			return binary_search(data, item, offset)