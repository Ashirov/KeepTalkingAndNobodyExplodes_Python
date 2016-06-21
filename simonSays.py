colorArray = []

def main(running):
	while running == True:
		serialVowel = raw_input("Does the serial number contain a vowel? ").lower()
		strikeAmount = raw_input("How many strikes have you taken? ").lower()
		print "\n"

		if strikeAmount == "0" or "none" or "zero":
			strikeAmount = 0
		elif strikeAmount == "1" or "one":
			strikeAmount = 1
		elif strikeAmount == "2" or "two":
			strikeAmount == 2
		else:
			running = False

		if serialVowel == "yes":
			if strikeAmount == 0:
				red = "blue"
				blue = "red"
				green = "yellow"
				yellow = "green"
			elif strikeAmount == 1:
				red = "yellow"
				blue = "green"
				green = "blue"
				yellow = "red"
			elif strikeAmount == 2:
				red = "green"
				blue = "red"
				green = "yellow"
				yellow = "blue"
			else:
				running = False
		elif serialVowel == "no":
			if strikeAmount == 0:
				red = "blue"
				blue = "yellow"
				green = "green"
				yellow = "red"
			elif strikeAmount == 1:
				red = "red"
				blue = "blue"
				green = "yellow"
				yellow = "green"
			elif strikeAmount == 2:
				red = "yellow"
				blue = "green"
				green = "blue"
				red = "red"
		else:
			running = False

		firstColor = raw_input("What is the first color? ").lower()

		if firstColor == "red":
			colorArray.append(red)
			print "Click: " + colorArray[0] + "\n"
		elif firstColor == "blue":
			colorArray.append(blue)
			print "Click: " + colorArray[0] + "\n"
		elif firstColor == "green":
			colorArray.append(green)
			print "Click: " + colorArray[0] + "\n"
		elif firstColor == "yellow":
			colorArray.append(yellow)
			print "Click: " + colorArray[0] + "\n"
		else:
			running = False	
				
		secondColor = raw_input("What is the second color? ").lower()

		if secondColor == "red":
			colorArray.append(red)
			print "Click: " + colorArray[0] + " " + colorArray[1] + "\n"
		elif secondColor == "blue":
			colorArray.append(blue)
			print "Click: " + colorArray[0] + " " + colorArray[1] + "\n"
		elif secondColor == "green":
			colorArray.append(green)
			print "Click: " + colorArray[0] + " " + colorArray[1] + "\n"
		elif secondColor == "yellow":
			colorArray.append(yellow)
			print "Click: " + colorArray[0] + " " + colorArray[1] + "\n"
		else:
			running = False

		thirdColor = raw_input("What is the third color? ").lower()

		if thirdColor == "red":
			colorArray.append(red)
			print "Click: " + colorArray[0] + " " + colorArray[1] + " " + colorArray[2] + "\n"
		elif thirdColor == "blue":
			colorArray.append(blue)
			print "Click: " + colorArray[0] + " " + colorArray[1] + " " + colorArray[2] + "\n"
		elif thirdColor == "green":
			colorArray.append(green)
			print "Click: " + colorArray[0] + " " + colorArray[1] + " " + colorArray[2] + "\n"
		elif thirdColor == "yellow":
			colorArray.append(yellow)
			print "Click: " + colorArray[0] + " " + colorArray[1] + " " + colorArray[2] + "\n"
		else:
			running = False	

		fourthColor = raw_input("What is the fourth color? ").lower()

		if fourthColor == "red":
			colorArray.append(red)
			print "Click: " + colorArray[0] + " " + colorArray[1] + " " + colorArray[2] + " " + colorArray[3] + "\n"
		elif fourthColor == "blue":
			colorArray.append(blue)
			print "Click: " + colorArray[0] + " " + colorArray[1] + " " + colorArray[2] + " " + colorArray[3] + "\n"
		elif fourthColor == "green":
			colorArray.append(green)
			print "Click: " + colorArray[0] + " " + colorArray[1] + " " + colorArray[2] + " " + colorArray[3] + "\n"
		elif fourthColor == "yellow":
			colorArray.append(yellow)
			print "Click: " + colorArray[0] + " " + colorArray[1] + " " + colorArray[2] + " " + colorArray[3] + "\n"
		else:
			running = False	

		running = False				

main(True)