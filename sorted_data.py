def main():
	ratings = open("scores.txt", "r")
	
	# Create a list of restaurant and rating pairs from the lines in the file
	contentsList = [line.split(":") for line in ratings]

	# Change 'contentsList' into a dictionary and convert the values to integers,
	# if a ValueError is raised remove '\n' and add the value as a str
	contentsDict = {}
	for line in contentsList:
		try:
			contentsDict[line[0]] = int(line[1])
		except ValueError:
			contentsDict[line[0]] = line[1][:-1]
			
	for key in sorted(contentsDict):
		print "Resturant '" + key + "' is rated at " + str(contentsDict[key]) + "."

if __name__ == "__main__":
	main()
