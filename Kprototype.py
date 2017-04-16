class Kprototypes:
    def __init__(self):
        self.clsuter_number = 0
        self.center_categorical = []
        self.center_numerica = []
        self.cluster_dataPonits_id = []
        # -------------Setters and getters methods-----------------------

    def setclsuter_number(self, cluster_id):
        self.clsuter_number = cluster_id

    def setcenter_categorical(self, cate_center):
        self.center_categorical = cate_center

    def setcenter_numerica(self, numeric_center):
        self.center_numerica = numeric_center

    def setcluster_dataPonits_id(self, datapoint_id):
        #print( "current id in class", self.cluster_dataPonits_id)
        #print ("coming data id", datapoint_id)
        if (datapoint_id not in self.cluster_dataPonits_id):
            self.cluster_dataPonits_id.append(datapoint_id)
            #print(" data point is add")

    def getcluster_nmuber(self):
        return self.clsuter_number

    def getcenter_categorical(self):
        return self.center_categorical

    def getcenter_numerica(self):
        return self.center_numerica

    def getcluster_dataPonits_id(self):
        return self.cluster_dataPonits_id

    def getclustersize(self):
        return (len(self.cluster_dataPonits_id))

    # -----------------------------------------------------------------
    def removeId(self, idValue):
        self.cluster_dataPonits_id.remove(idValue)

    def formcenter(self, datapoint, cat_dimn, num_dimn):
        cate_part = datapoint[0:cat_dimn]
        num_part = datapoint[cat_dimn:]
        self.center_categorical = cate_part
        self.center_numerica = num_part