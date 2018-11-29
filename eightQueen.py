import random
import numpy as np
from bokeh.plotting import figure, output_file, show, save

class Node:
    def __init__(self, index, weight, adjVec = []):
        self.index = index
        self.weight = weight
        self.adjVec = adjVec
        self.adjNum = 1
        for i in adjVec:
            if i == 1:
                self.adjNum += 1
        self.weightPerNumPlusOne = float(weight)/float(self.adjNum)

    def getAdjNode(self):
        temp = []
        for index,value in enumerate(self.adjVec):
            if value == 1:
                temp.append(index)
        return temp
    
    def updateWeight(self, Ans = [], graphList = []):
        countAdj = 1
        for value in Ans:
            if value in graphList[self.index].getAdjNode():
                countAdj -= 1
        self.weightPerNumPlusOne = float(countAdj)/float(self.adjNum)

def is8Queen(Ans = [], graphList = []):
    for value in Ans:
        for adjNode in graphList[value].getAdjNode():
            if adjNode in Ans:
                return False
    return True

def allUpdateWeight(Ans = [], graphList = []):
    for node in graphList:
        node.updateWeight(Ans, graphList)

#####################################################################################

results = {}
looprange = 500

for loop in range(398, 500):
    weightList = []
    graphList = []
    MWIS = []
    INIT = []
    currentState = []
    stopState = []
    totalWeight = 0
    ranInOut = [0, 1]
    infiniteFlag = False

    file = open('eightQueen.txt', 'r')      #you can modify testfile here
    for i,line in enumerate(file):
        if i == 1:
            for plot in line.split():
                weightList.append( int(plot))
        elif i > 1:
            graphList.append( Node( i-2, weightList[i-2], list( map( int, line.split()))))
            stopState.append(-1)
            currentState.append(random.choice(ranInOut))
    file.close()

    allUpdateWeight(currentState, graphList)
    ######################################################################################
    count = 1
    # queen = 0
    while currentState !=  stopState:
        # randomly pick up index to change
        randomIndex = random.randint(0,len(currentState)-1)
        for adjNode in graphList[randomIndex].getAdjNode():
            if currentState[adjNode] == 1 and graphList[randomIndex].weightPerNumPlusOne <= graphList[adjNode].weightPerNumPlusOne:
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            currentState[randomIndex] = 1
        elif flag == 0:
            currentState[randomIndex] = 0     

        allUpdateWeight(currentState, graphList)

        # check length of currentState == 8
        # queen = 0
        # for choose in currentState:
        #     if choose == 1:
        #         queen += 1

        # make sure the one in current list would not change. 
        for node in graphList:
            # node.updateWeight(currentState)
            for adjNode in node.getAdjNode():
                if currentState[adjNode] == 1 and node.weightPerNumPlusOne <= graphList[adjNode].weightPerNumPlusOne:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag == 1:
                stopState[node.index] = 1
            elif flag == 0:
                stopState[node.index] = 0

        # loop threshold
        if count > len(currentState)*100:
            infiniteFlag = True
            break
        count += 1

    #for i in graphList:
    # print(i.index, i.weight , i.adjVec, i.adjNum, i.weightPerNumPlusOne)
    #print(currentState)
    queen = 0
    for i,choose in enumerate(currentState):
        if choose == 1:
            queen += 1
            MWIS.append(i)
            totalWeight += graphList[i].weight

    print(str(loop) + " loop, " + str(count) + " count")
    print(MWIS)   
    if queen == 8 and is8Queen(MWIS, graphList):
        output_file("8queens/8queen_"+ str(loop) + "_loop.html", title="8queen "+ str(loop) + " loop, " + str(count) + " count", mode="cdn")
        # print(str(loop) + " loop, " + str(count) + " count")
        # print(MWIS)
        print("8queen")
    else:
        output_file("others/8queen_"+ str(loop) + "_loop.html", title="8queen "+ str(loop) + " loop, " + str(count) + " count", mode="cdn")
        

    x = []
    y = []
    for node in MWIS:
        x.append(node // 8)
        y.append(node % 8)

    # colors = [
    #     "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
    # ]
    # output to static HTML file (with CDN resources)
    # output_file("8queen.html", title="color_scatter.py example", mode="cdn")

    TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

    # create a new plot with the tools above, and explicit ranges
    # p = figure(tools=TOOLS, x_range=(-1, 8), y_range=(-1, 8))
    p = figure(tools=TOOLS)
    # add a circle renderer with vectorized colors and sizes
    # p.circle(x, y, radius=3, fill_color=colors, fill_alpha=0.6, line_color=None)
    p.circle(x, y, radius=0.3, fill_alpha=0.6)

    # show the results
    # show(p)
    save(p)
        # print(totalWeight)
#     resultState = tuple(MWIS)
#     if infiniteFlag:
#         if results.get('infinite') == None:
#             results['infinite'] = 1
#         else:
#             results['infinite'] += 1
#     else:
#         if results.get(resultState) == None:    
#             results[resultState] = 1
#         else:
#             results[resultState] += 1

# for key,value in results.items():
#     print(str(key) + " : " + str(value/looprange))

