import numpy
import math

def parcours(llist):
    position = 0
    timeSpent = 0
    llist.sort()
    sortedList = []
    #for house in llist:
        #print(house)
    #print(llist)
    return sortedList

def norm(x, u, sigma):
    return math.exp(-((x - u)**2)/(2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))


llist = numpy.random.normal(0,1000,1000)
parcours(llist)

u = 0
sigma = 1
for x in range(0, 11):
    result = norm(x, u, sigma)
    print(f"f({x}, {u}, {sigma}) is {result}")
    print(math.erf(x/2) - 0.5)
