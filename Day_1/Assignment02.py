import math
a= input("Please enter velocity (percentage of speed of light): ")
vel=float(a)
print ("Ship is travelling at " + str(vel) + " % speed of light.")
print ('At this speed : ')
vel=vel/100
factor=1/math.sqrt(1-math.pow(vel,2))
mass=factor*70000
print ("Weight of the shuttle is "+ str(mass))
print ("Perceived time to travel to Alpha Centauri " + str(4.3/factor) + "years.")
print ("Perceived time to travel to Barnard\'s Star is " + str(6.0/factor) + " years.")
print ("Perceived time to travel to Betelguese is " + str(309.0/factor) + " years.")
print ("Perceived time to travel to Andromeda Galaxy " + str(2000000.0/factor) + " years.")

