class searchNode(object):
    def __init__(self, gameState, previousNode=None,heuristic=0):
        if(previousNode is None):
            self.previousStates=list()
            self.currentCost=0
            self.currentDepth=0
            self.currentState=gameState
            self.currentHeuristicValue=heuristic
        else:
            self.previousStates=list(previousNode.previousStates)
            self.previousStates.append(previousNode)
            self.currentCost=previousNode.currentCost+gameState[2]
            self.currentDepth=previousNode.currentDepth+1
            self.currentState=gameState
            self.currentHeuristicValue=heuristic

    def ToDirection(self, directionString):
        n = Directions.NORTH
        e = Directions.EAST
        s = Directions.SOUTH
        w = Directions.WEST

        if (directionString=='North'):
            return n
        elif(directionString=='East'):
            return e
        elif(directionString=='South'):
            return s
        elif(directionString=='West'):
            return w

    def GetDirections(self):
        directions=list()

        for x in self.previousStates:
            if x.currentState[1] != "START":
                directions.append(x.currentState[1])
        directions.append(self.currentState[1])

        return directions
    def AStarCost(self):
        return self.currentCost+self.currentHeuristicValue

