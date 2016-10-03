import random
import math

def Increase(value):
	number = round(random.random(),1)
	print "Increasing value by",number
	value = value + number
	return value

def Decrease(value):
	number = round(random.random(),1)
	print "Decreasing value by",number
	value = value - number
	return value

def Increase_Large(value):
	number = round(random.random(),1)
	print "Increasing value by",(number*2)
	value = value + (number*2)
	return value

def Decrease_Large(value):
	number = round(random.random(),1)
	print "Decreasing value by",(number*2)
	value = value - (number*2)
	return value