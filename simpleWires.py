from sys import argv

script, wireChoice = argv

def main():
	print "INITIALIZING SCRIPT. . ."
	print "SOURCE: " + script + "\n"

	if wireChoice == "3":
		three()
	elif wireChoice == "4":
		four()
	elif wireChoice == "5":
		five()
	elif wireChoice == "6":
		six()
	else:
		print "That is not a valid input."

def three():
	print "Enter the wire colors below: "
	print "\n"
	
	first = raw_input("First wire: ")
	second = raw_input("Second wire: ")
	third = raw_input("Third wire: ")
	print "\n"

	mainArray = [first, second, third]
	blueCount = mainArray.count("blue")

	if "red" not in mainArray:
		print "Cut the second wire."
	elif mainArray[2] == "white":
		print "Cut the last wire."
	elif blueCount >= 2:
		print "Cut the last blue wire."
	else:
		print "Cut the last wire."

def four():
	serialStat = raw_input("Is the last digit of the serial number 'odd' or 'even'? ")
	print "\n"

	print "Enter the wire colors in order below: "
	first = raw_input("First wire: ")
	second = raw_input("Second wire: ")
	third = raw_input("Third wire: ")
	fourth = raw_input("Fourth wire: ")
	print "\n"

	mainArray = [first, second, third, fourth]
	redCount = mainArray.count("red")
	blueCount = mainArray.count("blue")
	yellowCount = mainArray.count("yellow")

	if redCount >= 1 and serialStat == "odd":
		print "Cut the last red wire."
	elif mainArray[3] == "yellow" and redCount == 0:
		print "Cut the first wire."
	elif blueCount == 1:
		print "Cut the first wire."
	elif yellowCount >= 1:
		print "Cut the last wire."
	else:
		print "Cut the second wire."

def five():
	serialStat = raw_input("Is the last digit of the serial number 'odd' or 'even'? ")
	print "\n"

	print "Enter the wire colors in order below: "
	first = raw_input("First wire: ")
	second = raw_input("Second wire: ")
	third = raw_input("Third wire: ")
	fourth = raw_input("Fourth wire: ")
	fifth = raw_input("Fifth wire: ")
	print "\n" 

	mainArray = [first, second, third, fourth, fifth]
	blackCount = mainArray.count("black")
	redCount = mainArray.count("red")
	yellowCount = mainArray.count("yellow")

	if mainArray[4] == "black" and serialStat == "odd":
		print "Cut the fourth wire."
	elif redCount == 0 and yellowCount > 1:
		print "Cut the first wire."
	elif blackCount == 0:
		print "Cut the second wire."
	else:
		print "Cut the first wire."

def six():
	serialStat = raw_input("Is the last digit of the serial number 'odd' or 'even'? ")
	print "\n"

	print "Enter the wire colors in order below: \n"
	first = raw_input("First wire: ")
	second = raw_input("Second wire: ")
	third = raw_input("Third wire: ")
	fourth = raw_input("Fourth wire: ")
	fifth = raw_input("Fifth wire: ")
	sixth = raw_input("Sixth wire: ")
	print "\n" 

	mainArray = [first, second, third, fourth, fifth, sixth]
	yellowCount = mainArray.count("yellow")
	whiteCount = mainArray.count("white")
	redCount = mainArray.count("red")

	if yellowCount == 0 and serialStat == "odd":
		print "Cut the third wire."
	elif yellowCount == 1 and whiteCount <= 1:
		print "Cut the fourth wire."
	elif redCount == 0:
		print "Cut the last wire."
	else:
		print "Cut the fourth wire."

main()