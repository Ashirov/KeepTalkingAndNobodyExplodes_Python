def main():
	print "Gathering necessary data: \n"
	buttonColor = raw_input("What color is the button? ")
	buttonText = raw_input("What does the button read? ")
	buttonBatterys = raw_input("How many batteries are present on the bomb? ")
	print "\n"

	if buttonBatterys >= "1" and buttonText == "detonate":
		print "[Press and release immediatly.]"
	elif buttonBatterys >= "2":
		statusFRK = raw_input("Is there a lit FRK indicator present on the bomb? ")

		if statusFRK == "yes":
			print "[Press and release immediatly.]"
		else:
			if buttonColor == "white":
				statusCAR = raw_input("Is there a lit CAR indicator present on the bomb? ")
				if statusCAR == "yes":
					print "[Press and hold...]\n"
					hold()
				else:
					if buttonColor == "blue" and buttonText == "abort":
						print "[Press and hold...]\n"
						hold()
					elif buttonColor == "yellow":
						print "[Press and hold...]\n"
						hold()
					elif buttonColor == "red":
						print "[Press and release immediatly.]"
					else:
						print "[Press and hold...]\n"
						hold()
			elif buttonColor == "blue" and buttonText == "abort":
				print "[Press and hold...]\n"
				hold()
			elif buttonColor == "yellow":
				print "[Press and hold...]\n"
				hold()
			elif buttonColor == "red":
				print "[Press and release immediatly.]"
			else:
				print "[Press and hold...]\n"
				hold()
	else:
		if buttonColor == "white":
			statusCAR = raw_input("Is there a lit CAR indicator present on the bomb? ")
			
			if statusCAR == "yes":
				print "[Press and hold...]\n"
				hold()
		elif buttonColor == "blue" and buttonText == "abort":
			print "[Press and hold...]\n"
			hold()
		elif buttonColor == "yellow":
			print "[Press and hold...]\n"
			hold()
		elif buttonColor == "red":
			print "[Press and release immediatly.]"
		else:
			print "[Press and hold...]\n"
			hold()

def hold():
	stripColor = raw_input("What color is the strip? ")

	if stripColor == "blue":
		print "\n"
		print "[Release when the countdown timer has a 4 in any position.]"
	elif stripColor == "white":
		print "\n"
		print "[Release when the countdown timer has a 1 in any position.]"
	elif stripColor == "yellow":
		print "\n"
		print "[Release when the countdown timer has a 5 in any position.]"
	else:
		print "\n"
		print "[Release when the countdown timer has a 1 in any position.]"

main()