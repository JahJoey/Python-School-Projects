# Author @ Joseph Hein
# CS 3060 | Python Functions

def split_char(str, char) :
	count = 0
	new = 0
	words = []

	for i in range(len(str)) :
		if str[i] != char :
			count += 1
			if i == len(str) - 1 :
				words.append(str[new:count])
		else :
			words.append(str[new:count])
			count += 1
			new = i+1

	return words