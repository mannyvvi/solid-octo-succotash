from Prob_Distros import Normal_Distro
from Actions import *
import operator

def Decider(value,action,difference, goal):
	if action == 1:
		probs = []
		prob_vhigh = Normal_Distro(difference,goal*0.90 ,0.8)
		probs.append(prob_vhigh)

		prob_high = Normal_Distro(difference,goal*0.50 ,0.8)
		probs.append(prob_high)

		prob_low = Normal_Distro(difference,goal*-0.50 ,0.8)
		probs.append(prob_low)

		prob_vlow = Normal_Distro(difference,goal*-0.90 ,0.8)
		probs.append(prob_vlow)

		choice, number = max(enumerate(probs), key=operator.itemgetter(1))
		if choice == 0:
			print "Very High"
			value = Increase_Large(value)
		elif choice == 1:
			print "High"
			value = Increase(value)
		elif choice == 2:
			print "Low"
			value = Decrease(value)
		elif choice == 3:
			print "Very Low"
			value = Decrease_Large(value)
		elif choice == 4:
			print "BAAAAAA!!"
	return value
	


