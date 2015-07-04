ratings = open("scores.txt", "r")
contents = [line.split(":") for line in ratings]
contents = {line[0]:line[1] for line in contents}

items = contents.items()
items.sort()

for item in items:
	item = list(item)

	print "Resturant '" + item[0] + "' is rated at " + item[1][:-1] + "."
