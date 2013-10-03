import random
import os
from datetime import datetime

#----------------------------------------------------
# generates array of random int numbers from 0 to 100 

def generate_data(count):
	result = []
	for i in range(count): #What kind of array should we teach? All of them?
		result.append(random.randint(0, 100))
	return result

#----------------------------------------------------
# Saves int data to file 

def save_to_file(filename, data):
	file = open(filename, 'w')

	for number in data:
		file.write(str(number) + "\n") #is it ok that this is not effective
	
	file.close()

#----------------------------------------------------
# Reads int data from file

def read_from_file(filename):
	file = open(filename, 'r')
	data = []
	
	for line in file:
		line = line.strip()
		if line != '':
			data.append(int(line))

	file.close()
	return data

#-----------------------------------------------------
# Finds max number

def find_max_straight(data):
	max = 0
	for number in data:
		if number > max:
			max = number
	return max

#-----------------------------------------------------
# Bubble sort
def sort_bubble(data):
	start = datetime.now()

	for i in range(0, len(data)):
		for j in range(i, len(data)):
			if (data[i] < data[j]):
				tmp = data[j]
				data[j] = data[i]
				data[i] = tmp

	end = datetime.now()
	spent = end - start
	print("Bubble sort spent time is %s" % spent.microseconds)


#-----------------------------------------------------
# main program

if __name__ == '__main__':
	print ("Starting first lesson now...")

	print ("Generating sample data")
	data = generate_data(100)
	save_to_file('data.txt', data)

	data = read_from_file('sample.txt')
	print("Read data, %s items" % len(data))

	max = find_max_straight(data)
	print ("Maximum item is %s " % max)

	data = read_from_file('data.txt')
	sort_bubble(data)
	print("Sorted data is %s" % [int(i) for i in data]) #Complicated


