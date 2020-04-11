from sklearn.cluster import KMeans
import numpy as np
import pickle
import pandas as pd

class InfosetAbstraction:

    def __init__(self):
        return

    def run_k_means(self,data,cluster):
        self.kmeans = KMeans(n_clusters=cluster, random_state=0).fit(data)
        a=1

    def save_model(self,filename):
        pickle.dump(self.kmeans,open(filename,'wb'))

    def load_model(self,filename):
        self.kmeans = pickle.load(open(filename,'rb'))

    def cluster_class(self,data_point):
        return self.kmeans.predict(data_point)

    def prepare_data(self,filename):
        data = pd.read_csv(filename)
        data = data.drop(['CLASS'],axis=1)
        return data.to_numpy()

    def predict(self,data_point):
        return self.kmeans.predict(data_point)

    def prepare_data_two_card(self,filename):
        data = pd.read_csv(filename)
        data_1 = data.drop(['S3','C3','S4','C4','S5','C5','CLASS'], axis=1) # 1,2
        data_2 = data.drop(['S1', 'C1', 'S4', 'C4', 'S5', 'C5', 'CLASS'], axis=1) # 2,3
        data_3 = data.drop(['S1', 'C1', 'S2', 'C2', 'S5', 'C5', 'CLASS'], axis=1) # 3,4
        data_4 = data.drop(['S3', 'C3', 'S1', 'C1', 'S2', 'C2', 'CLASS'], axis=1) # 4,5
        data_5 = data.drop(['S2', 'C2', 'S4', 'C4', 'S5', 'C5', 'CLASS'], axis=1) # 1,3
        data_6 = data.drop(['S2', 'C2', 'S3', 'C3', 'S5', 'C5', 'CLASS'], axis=1) # 1,4
        data_7 = data.drop(['S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'CLASS'], axis=1) # 1,5
        data_8 = data.drop(['S1', 'C1', 'S3', 'C3', 'S5', 'C5', 'CLASS'], axis=1) # 2,4
        data_9 = data.drop(['S1', 'C1', 'S3', 'C3', 'S4', 'C4', 'CLASS'], axis=1) # 2,5
        data_10 = data.drop(['S1', 'C1', 'S2', 'C2', 'S4', 'C4', 'CLASS'], axis=1) # 3,5

        data = data_1.to_numpy()
        data = np.concatenate((data, data_2.to_numpy()), axis=0)
        data = np.concatenate((data, data_3.to_numpy()), axis=0)
        data = np.concatenate((data, data_4.to_numpy()), axis=0)
        data = np.concatenate((data, data_5.to_numpy()), axis=0)
        data = np.concatenate((data, data_6.to_numpy()), axis=0)
        data = np.concatenate((data, data_7.to_numpy()), axis=0)
        data = np.concatenate((data, data_8.to_numpy()), axis=0)
        data = np.concatenate((data, data_9.to_numpy()), axis=0)
        data = np.concatenate((data, data_10.to_numpy()), axis=0)


        return data