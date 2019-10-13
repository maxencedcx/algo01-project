import numpy
import math



####### PART 1
def parcours(llist):
    parcoursLlist = []
    copyllist = list(llist).copy()
    copyllist.sort()

    M = sum(copyllist) / len(copyllist)
    xxx = 0
    for x in copyllist:
        xxx += (x - M)**2
    sigma = math.sqrt(xxx/len(copyllist))
    positiveMajorllist = [x for x in copyllist if 0 <= x < M + 0.96 * sigma]
    negativeMajorllist = [x for x in copyllist if M - 0.96 * sigma < x < 0]
    negativeMajorllist.sort(reverse=True)
    positiveRemainingllist = [x for x in copyllist if x not in positiveMajorllist and 0 < x]
    negativeRemainingllist = [x for x in copyllist if x not in negativeMajorllist and x < 0]
    negativeRemainingllist.sort(reverse = True)

    if len(positiveMajorllist) > len(negativeMajorllist) or positiveMajorllist[-1] < abs(negativeMajorllist[-1]):
        parcoursLlist = positiveMajorllist + negativeMajorllist + negativeRemainingllist + positiveRemainingllist
    else:
        parcoursLlist = negativeMajorllist + positiveMajorllist + positiveRemainingllist + negativeRemainingllist

    return parcoursLlist


def calculateTimeTakenByList(llist, position = 0, baseTime = 0):
    timeTaken = baseTime
    previousWaitingTime = 0
    for i in range(0, len(llist)):
        tmpPos = position if i == 0 else llist[i - 1]
        previousWaitingTime += abs(tmpPos - llist[i])
        timeTaken += previousWaitingTime
    return timeTaken


def gloutonAlgo(llist, position = 0):
    gloutonLlist = []
    copyllist = llist
    while len(copyllist) > 0:
        position = min(copyllist, key=lambda x:abs(x-position))
        gloutonLlist.append(position)
        copyllist.remove(position)

    return gloutonLlist


llistSize = 1000
llist = numpy.random.normal(0, llistSize, llistSize)

gloutonllist = gloutonAlgo(list(llist).copy())
totalGloutonTime = calculateTimeTakenByList(gloutonllist)
averageGloutonTime = totalGloutonTime / llistSize
#print(gloutonllist)
print(f"total Glouton time :\t{totalGloutonTime},\taverage Glouton time:\t{averageGloutonTime},\ttime to be under: {0.9*averageGloutonTime}")

parcoursllist = parcours(llist)
#print(parcoursllist)
totalparcoursTime = calculateTimeTakenByList(parcoursllist)
averageparcoursTime = totalparcoursTime / llistSize
print(f"total parcours time :\t{totalparcoursTime},\taverage parcours time:\t{averageparcoursTime}")
