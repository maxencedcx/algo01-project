import numpy
import math



####### PART 1
def parcours(llist):
    return mixAlgo(list(llist).copy())

def calculateTimeTakenByList(llist, position = 0, baseTime = 0):
    timeTaken = baseTime
    previousWaitingTime = 0
    for i in range(0, len(llist)):
        tmpPos = position if i == 0 else llist[i - 1]
        previousWaitingTime += abs(tmpPos - llist[i])
        timeTaken += previousWaitingTime
        #print(f"from {tmpPos} to {llist[i]} takes {abs(tmpPos - llist[i])} + {previousWaitingTime - abs(tmpPos - llist[i])} = {previousWaitingTime}, total is {timeTaken}")
    return timeTaken

def gloutonAlgo(llist, position = 0):
    gloutonLlist = []
    copyllist = llist
    while len(copyllist) > 0:
        position = min(copyllist, key=lambda x:abs(x-position))
        gloutonLlist.append(position)
        copyllist.remove(position)

    return gloutonLlist

def mixAlgo(llist):
    mixLlist = []
    copyllist = llist
    copyllist.sort()

    M = sum(llist) / len(llist)
    xxx = 0
    for x in llist:
        xxx += (x - M)**2
    sigma = math.sqrt(xxx/len(llist))

    majorllist = [x for x in copyllist if M - 0.96 * sigma < x < M + 0.96 * sigma]
    positiveMajorllist = [x for x in majorllist if x > 0]
    negativeMajorllist = [x for x in majorllist if x < 0]
    negativeMajorllist.sort(reverse=True)
    positiveRemainingllist = [x for x in copyllist if x not in majorllist and x > 0]
    negativeRemainingllist = [x for x in copyllist if x not in majorllist and x < 0]
    negativeRemainingllist.sort(reverse = True)

    if len(positiveMajorllist) > len(negativeMajorllist):
        mixLlist = positiveMajorllist + negativeMajorllist
    elif positiveMajorllist[-1] < abs(negativeMajorllist[-1]):
        mixLlist = positiveMajorllist + negativeMajorllist
    else:
        mixLlist = negativeMajorllist + positiveMajorllist

    position = mixLlist[-1]
    if position > 0:
        mixLlist += positiveRemainingllist + negativeRemainingllist
    else:
        mixLlist += negativeRemainingllist + positiveRemainingllist

    return mixLlist


llistSize = 1000
llist = numpy.random.normal(0, llistSize, llistSize)

gloutonllist = gloutonAlgo(list(llist).copy())
totalGloutonTime = calculateTimeTakenByList(gloutonllist)
averageGloutonTime = totalGloutonTime / llistSize
#print(gloutonllist)
print(f"total Glouton time :\t{totalGloutonTime},\taverage Glouton time:\t{averageGloutonTime},\ttime to be under: {0.9*averageGloutonTime}")

mixllist = parcours(llist)
#mixllist = mixAlgo(list(llist).copy())
#print(mixllist)
totalmixTime = calculateTimeTakenByList(mixllist)
averagemixTime = totalmixTime / llistSize
print(f"total mix time :\t{totalmixTime},\taverage mix time:\t{averagemixTime}")





###### PART2
def part2ColoringProblemHeuristic(nodesAndNeighbors, colors):
    # The heuristic works this way:
    # We sort each node by its degree
    # We go through this list, attributes a color for each node that is not a neighbour with the previous colored node
    # Repeat this process with new colors once we finished going through the list

    colorsAndNodes = dict()
    copyllist = sorted(nodesAndNeighbors, key=lambda x: len(x[1]), reverse=True)
    print(copyllist)
    colorIndex = 0

    while len(copyllist) > 0:
        colorsAndNodes[colors[colorIndex]] = []
        for aNodeAndNeighbors in copyllist:
            if any(x in colorsAndNodes[colors[colorIndex]] for x in aNodeAndNeighbors[1]):
                continue
            else:
                colorsAndNodes[colors[colorIndex]].append(aNodeAndNeighbors[0])
        copyllist = [x for x in copyllist if x[0] not in colorsAndNodes[colors[colorIndex]]]
        colorIndex += 1

    return colorsAndNodes

nodesAndNeighbors = [
                    [1, [2,3,4]],
                    [2, [1]],
                    [3, [1, 9, 10]],
                    [4, [1, 5, 10]],
                    [5, [4, 6, 7]],
                    [6, [5, 7, 10]],
                    [7, [5, 6, 10]],
                    [8, [9, 10]],
                    [9, [3, 8]],
                    [10, [3, 6, 7, 8]]
]

colors = [
            "red",
            "yellow",
            "blue",
            "green",
            "cyan",
            "purple",
            "orange",
            "magenta",
            "turquoise",
            "grey",
            "pink"
]

print(part2ColoringProblemHeuristic(nodesAndNeighbors, colors))
