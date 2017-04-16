from sklearn.metrics import accuracy_score
import time
import Kprototype
import kprototype_method

if __name__ == "__main__":

    file = open('adult_48.csv', 'rU')
    lines = file.readlines()  # return all the lines in the file in one list - each index represents a line
    data_size = (len(lines))
    index = 0  # we start with the first line
    templine = lines[index]
    centroids=[]
    tempDataPoint = [x.strip() for x in templine.split(',')]
    cate_dim, num_dim = kprototype_method .compute_dime(tempDataPoint)

    # ------------------initialize clusters-------------
    num_of_clusters = 2
    iter = 1
    start_time = time.time()
    while (iter <= num_of_clusters):
        obj = Kprototype.Kprototypes()
        obj.setclsuter_number(iter)
        centroids.append(obj)
        datapoints = lines[iter + 10]
        currentDataPoint = kprototype_method.formdatapoints(datapoints, cate_dim, num_dim)
        iter += 1

        # form center
        # print("current",currentDataPoint)
        obj.formcenter(currentDataPoint, cate_dim, num_dim)

    # --------------------process data in text ---------------------
    # --------------------------------------------------------------
    kdata = {}
    counter_value = 1
    for line in lines:
        # print("line number",counter_value )
        # print(line)
        newpoint = kprototype_method.formdatapoints(line, cate_dim, num_dim)
        kdata[counter_value] = newpoint
        counter_value += 1
    filesize = len(kdata)
    print ("Number of records in dataset:", filesize)
    # --------------------------------------------------------------

    predected_labels = kprototype_method.performClustering(centroids, kdata, cate_dim, num_dim, data_size)
    # read truth values from text file
    print(predected_labels.getdataInfo())
    for obj in centroids:
        obj.getcluster_dataPonits_id()
        print("cluster size", obj.getclustersize())
        print("--------------------------------------")

    end_time = (time.time() - start_time)
    print ("exuction time =", end_time)
    class_pred = []
    for k in range(1, data_size + 1):
        val = predected_labels.getclusterId(k)
        class_pred.append(val)

    label_line = file.readlines()
    class_true = [int(x.strip()) for x in label_line]
    clustering_accuracy = accuracy_score(class_true, class_pred)
    print("predicate_class",class_pred)
    print("actual_class",class_true)
    print("clsutering accuracy:", clustering_accuracy * 100)
    print ("clustring error:", 1 - clustering_accuracy)