class Clsuters:
    def __init__(self):
        self.classuterNumber = 0
        self.clusterSize = 0
        self.clsuterDict = {}
        self.clusterListId = []

    def setClusterId(self, clusterId):
        self.classuterNumber = clusterId

    def addDataPoint(self, datapointId):
        self.clusterListId.append(datapointId)

    def setNewValue(self, value):
        if (self.clsuterDict.has_key(value)):
            # add one to the current value
            print("Value there ")

    def formCenter(self, valueList):

        # this method is called only when a new cluster formed
        for item in valueList:  # go through the list one item at a time
            self.clsuterDict[item] = 1  # add that item and set it value(support) to 1

    def getcenter(self):
        return self.clsuterDict

    def increaseClsuterSzie(self):
        self.clusterSize += 1

    def getClsuterSize(self):
        return len(self.clusterListId)

    def getClsuterId(self):
        return self.classuterNumber

    def updateCenter(self, tuple1):

        for item in tuple1:
            if (self.clsuterDict.has_key(item)):
                self.clsuterDict[item] += 1
                #print("key is there" , item, "and the new suport is ", self.clsuterDict[item] )
            else:
                self.clsuterDict[item] = 1
        #print("updated center",self.clsuterDict)
    def getdatapointInCluster(self):
        return self.clusterListId