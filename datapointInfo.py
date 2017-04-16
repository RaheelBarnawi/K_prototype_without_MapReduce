class datapointInfo:
    def __init__(self):
        self.data_cluster = {}

    def steclusterNumber(self, clusterId, datapointId):
        # print("coming data", datapointId)
        self.data_cluster[datapointId] = clusterId
        # print(self.data_cluster)

    def getclusterId(self, datapointId):
        # print("current keys",self.data_cluster)
        # print("dataPointInfo",datapointId)
        return self.data_cluster[datapointId]

    def getdataInfo(self):
        return self.data_cluster