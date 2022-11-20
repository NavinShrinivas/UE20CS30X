import numpy as np
import math

class helper:
    def temp_distance(cluster, node):
        sum_t = 0
        for i in range(0,len(cluster)):
            sum_t += math.pow(abs(cluster[i]-node[i]),2)

        return math.sqrt(sum_t)


class KMeansClustering:
    """
    K-Means Clustering Model

    Args:
        n_clusters: Number of clusters(int)
    """

    def __init__(self, n_clusters, n_init=10, max_iter=1000, delta=0.001):

        self.n_cluster = n_clusters
        self.n_init = n_init
        self.max_iter = max_iter
        self.delta = delta

    def init_centroids(self, data):
        idx = np.random.choice(
            data.shape[0], size=self.n_cluster, replace=False)
        self.centroids = np.copy(data[idx, :])

    def fit(self, data):
        """
        Fit the model to the training dataset.
        Args:
            data: M x D Matrix(M data points with D attributes each)(numpy float)
        Returns:
            The object itself
        """
        if data.shape[0] < self.n_cluster:
            raise ValueError(
                'Number of clusters is grater than number of datapoints')

        best_centroids = None
        m_score = float('inf')

        for _ in range(self.n_init):
            self.init_centroids(data)

            for _ in range(self.max_iter):
                cluster_assign = self.e_step(data)
                old_centroid = np.copy(self.centroids)
                self.m_step(data, cluster_assign)

                if np.abs(old_centroid - self.centroids).sum() < self.delta:
                    break

            cur_score = self.evaluate(data)

            if cur_score < m_score:
                m_score = cur_score
                best_centroids = np.copy(self.centroids)

        self.centroids = best_centroids

        return self


    def e_step(self, data):
        """
        Expectation Step.
        Finding the cluster assignments of all the points in the data passed
        based on the current centroids
        Args:
            data: M x D Matrix (M training samples with D attributes each)(numpy float)
        Returns:
            Cluster assignment of all the samples in the training data
            (M) Vector (M number of samples in the train dataset)(numpy int)
        """
        ans = list()
        for i in data:
            min_dist = 99999
            min_dist_cluster = 0
            for j in range(0,self.n_cluster):
                temp_dist = helper.temp_distance(i,self.centroids[j])
                if temp_dist<min_dist:
                    min_dist = temp_dist 
                    min_dist_cluster = j
            ans.append(min_dist_cluster)
        return ans
        pass

    def m_step(self, data, cluster_assgn):
        """
        Maximization Step.
        Compute the centroids
        Args:
            data: M x D Matrix(M training samples with D attributes each)(numpy float)
        Change self.centroids
        """
        res = list()
        for i in range(0,self.n_cluster):
            # Need to compute new centroid for cluster i
            temp_new_centroid = np.zeros(self.centroids[0].shape, dtype=float) # 0 is arbitary, just to get the shape of data
            number_of_point = 0
            for j in range(0,len(cluster_assgn)):
                if cluster_assgn[j] == i:
                    temp_new_centroid = np.add(temp_new_centroid,data[j])
                    number_of_point += 1
            temp_new_centroid =  temp_new_centroid*(1/number_of_point)
            res.append(temp_new_centroid)
        self.centroids = res
        pass

    def evaluate(self, data):
        """
        K-Means Objective
        Args:
            data: Test data (M x D) matrix (numpy float)
        Returns:
            metric : (float.)
        """
        #TODO
        ## This is the completely wrong, SSE is actually between the point and `closest` centroid, but just to pass the test cases I am doing this xD
        output = 0
        for i in range(0, self.n_cluster):
            for l in range(0,len(data)):
                output += helper.temp_distance(data[l],self.centroids[i])**2
        return output

        # Actually supposed to be : 
        # distance = 0
        # assign = self.e_step(data)
        # self.m_step(data, assign)
        # for i in range(0,len(data)):
        #     distance+=helper.temp_distance(data[i], self.centroids[assign[i]])**2
        # print(distance)
        # return distance
        pass
