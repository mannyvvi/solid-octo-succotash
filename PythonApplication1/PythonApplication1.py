#from Actions import Increase,Decrease,Double
from Prob_Distros import Normal_Distro
from Decision import Decider
import math,random

#random .seed("Agent")

def desire(goal, value):
    difference = goal - value
    Mood = goal - (math.sqrt(difference * difference))
    return Mood, difference


def motivation(Mood,goal):
	if (goal - 0.1) <= Mood <= (goal + 0.1) :
		action = 0
	else:
		action = 1
	return action

def run(value,goal,action):
	counter = 0
	print "Goal:",goal
	print "I started at" ,value
	print "-----"
	while action != 0:
		status,difference = desire(goal,value)
		action = motivation(status,goal)
		value = Decider(value,action,difference,goal)
		print "Value:",value
		print "Mood:",status
		print "Difference:",difference
		print "-----"
		counter = counter +1

	print "That took me" , counter , "steps"


value = round(random.random(),1)
if value == 0:
	value = value + 1
goal = round(random.random(),1)
Mood = 0.1

run(value,goal,Mood)

#next step is to add planning stage
#this should check that the chosen action will result in increasing the Mood (or decreasing the difference)
#after that, look at chaining together actions into a plan, then run them all in one go

#also, look at VHigh bug that occurs (if utility decreases, do not do action - should solve issue) (adding negative mean to normal distro seems to have solved it)

