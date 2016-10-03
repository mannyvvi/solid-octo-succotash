import math

def normal_distro(x,mean,deviation):
     u = mean
     g = deviation
 #standard deviation g
     y = (1/(math.sqrt(2*(g*g)*3.142))) * math.exp(-((x-u)*(x-u))/(g*(math.sqrt(2))))
     return y