import numpy as np
from scipy.spatial import distance
from collections import Counter
import datapointInfo

def compute_dime(datapoint):
    num_dimn = 0
    cat_dimn = 0
    for item in datapoint:
        if (item.replace('.', '').isdigit()):
            num_dimn += 1
        else:
            cat_dimn += 1

    return cat_dimn, num_dimn


def update_centers(centeroids, kdata, cate_dimn, num_dimn):
    new_center_num = []
    new_center_cate = []
    num_list_list = []
    cat_list_list = []
    for obj in centeroids:
        # print(" onject Id =", obj.getcluster_dataPonits_id())
        cluster_id_list = obj.getcluster_dataPonits_id()
        for item in cluster_id_list:
            current_point = kdata[item]
            # print("current point ",current_point)
            cate_part = current_point[0:cate_dimn]
            num_part = current_point[cate_dimn:]
            num_list_list.append(num_part)
            cat_list_list.append(cate_part)
        # print("numeric part mean  ",num_list_list)
        # compute mean and frequency
        new_center_num, new_center_cate = compute_mean_frequency(num_list_list, cat_list_list, cate_dimn, num_dimn)
        # print(" computeed mean=",new_center_num, "computed mode=" ,new_center_cate)
        obj.setcenter_numerica(new_center_num)
        obj.setcenter_categorical(new_center_cate)
        new_center_num = []
        num_list_list = []
        new_center_cate = []
        cat_list_list = []


def compute_mean_frequency(num_list, cate_list, cate_dimn, num_dimn):
    mean_center = []
    mode_center = []
    dim_list = []
    # -----------------compute the mean  for numeric attributes ----------------
    for i in range(0, num_dimn):
        dim_mean = np.mean([pair[i] for pair in num_list])
        mean_center.append(dim_mean)
    # --------------------compute the mode for categorical attributes ---------------------
    # print("cate_list:",cate_list)
    for dim in range(0, cate_dimn):
        for item in cate_list:
            dim_list.append(item[dim])
        # print(" list of dim",dim,dim_list)
        count_dim = Counter(dim_list)
        # print("counter",count_dim)
        dim_mode = max(count_dim.iterkeys(), key=lambda k: count_dim[k])
        # print("dim_mode",dim," ",dim_mode)
        dim_list = []
        mode_center.append(dim_mode)
        # print ("categorical center =" , mode_center)
    return mean_center, mode_center


def formdatapoints(line, cat_dim, num_dim):
    tempDataPoint = [x.strip() for x in line.split(',')]
    cate_part = tempDataPoint[0:cat_dim]
    inputdata = cate_part
    for item in range(cat_dim, num_dim + cat_dim):
        inputdata.append(float(tempDataPoint[item]))
    return inputdata


# ----------------------------------------------------------------------
def compute_distance(center_cat, center_num, datapoint_cat, datapoint_num):
    # --------- Euclidean distance for numeric attributes--------------------

    dis_num = distance.euclidean(center_num, datapoint_num)
    # --------- Mismatch Distance for categorical attributes-----------------
    mis_match = [int(val not in center_cat) for val in datapoint_cat] # data in this
    dis_cate = sum(mis_match)
    # ----------K-prototype cost function-------------------------
    unified_distance = dis_num + dis_cate
    return unified_distance


# ---------------------------------------------------------------
def performClustering(centriods, kdata, cate_dimn, num_dimn,data_size):
    #  slices the data point to categorical and numerical
    print ("perform clustering ")
    DataPoint = datapointInfo.datapointInfo()
    centerSize = len(centriods)
    # print("kdata",len(kdata))
    print("center size", centerSize)
    iter = 1
    while (iter < 10):
        i = 1
        print (iter)
        while (i < data_size +1):
            datapoint = kdata[i]

            cate_part = datapoint[0:cate_dimn]
            num_part = datapoint[cate_dimn:]
            # print("current data point is:",datapoint)
            min = 1000000
            j = 0
            while (j < centerSize):
                # print("Itertion over centers=" , j)
                centriod = centriods[j]
                cluster_num = centriod.getcluster_nmuber()
                center_num = centriod.getcenter_numerica()
                # print("center_num",center_num)
                center_cat = centriod.getcenter_categorical() # clustroid
                #print("test centr number",j," for tuple",i)
                dis = compute_distance(center_cat, center_num, cate_part, num_part)
                #print(" dis",dis, "min=",min)
                if (dis < min):
                    #print ("dis < than min for opject", i)
                    min = dis
                    pointid = i
                    clu_idex = j
                    bestK = cluster_num
                    #print(" dis",dis, "min=",min)

                j += 1
            best_cluster = centriods[clu_idex]
            #print("data will be added to cluster ",best_cluster.getcluster_nmuber())
            best_cluster.setcluster_dataPonits_id(pointid)

            # check if the data change cluster
            if (iter == 1):
                DataPoint.steclusterNumber(bestK, pointid)

            else:
                # check if per is not equal new
                pre = DataPoint.getclusterId(pointid)
                if (pre != bestK):
                    # remove id from pervious
                    obj = centriods[pre - 1]
                    obj.removeId(pointid)
                DataPoint.steclusterNumber(bestK, pointid)

            i += 1
        iter += 1
        # update centers
        update_centers(centriods, kdata, cate_dimn, num_dimn)

    # print (DataPoint.getdataInfo() )
    return DataPoint