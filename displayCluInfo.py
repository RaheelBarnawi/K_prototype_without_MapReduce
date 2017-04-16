def displaySummary(createdCluster):
    for acluster in createdCluster:
        print(" ----------Clustering Summary-------------- ")
        print("==================================================")
        print("Cluster number:", acluster.getClsuterId())
        print("Number_of_ dataPoint in cluster",acluster.getClsuterSize())
        print("cluster center" ,acluster.getcenter())
