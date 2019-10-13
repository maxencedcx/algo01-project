




####### PART 2
def part2ColoringProblemHeuristic(nodesAndNeighbors, colors):
    # The heuristic works this way:
    # We sort each node by its degree
    # We go through this list, attributes a color for each node that is not a neighbour with the previous colored node
    # Repeat this process with new colors once we finished going through the list

    colorsAndNodes = dict()
    copyllist = sorted(nodesAndNeighbors, key=lambda x: len(x[1]), reverse=True)
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
