import numpy as np
import math


class Helpers:
    def minkowski_helper(point1, point2, p, w):
        distance = 0.0
        for i in range(0, len(point1)):
            diff = abs(point1[i]-point2[i])
            distance += math.pow(diff, p)
        distance = math.pow(distance, 1/p)
        return distance


class KNN:
    """
    K Nearest Neighbours model
    Args:
        k_neigh: Number of neighbours to take for prediction
        weighted: Boolean flag to indicate if the nieghbours contribution
                  is weighted as an inverse of the distance measure
        p: Parameter of Minkowski distance
    """

    def __init__(self, k_neigh, weighted=False, p=2):

        self.weighted = weighted
        self.k_neigh = k_neigh
        self.p = p

    def fit(self, data, target):
        """
        Fit the model to the training dataset.
        Args:
            data: M x D Matrix( M data points with D attributes each)(float)
            target: Vector of length M (Target class for all the data points as int)
        Returns:
            The object itself
        """

        self.data = data
        self.target = target.astype(np.int64)

        return self

    
    def find_distance(self, x):
        """
        Find the Minkowski distance to all the points in the train dataset x
        Args:
            x: N x D Matrix (N inputs with D attributes each)(float)
        Returns:
            Distance between each input to every data point in the train dataset
            (N x M) Matrix (N Number of inputs, M number of samples in the train dataset)(float)
        """
        # TODO
        number_of_trainings = len(x)
        number_of_instances = len(self.data)
        output_array = np.zeros(shape = (number_of_trainings,number_of_instances), dtype=float)
        for i in range(0, number_of_instances):
            for j in range(0,number_of_trainings):

                # Need to find distance from this point to all training data
                temp_dist = Helpers.minkowski_helper(self.data[i], x[j], self.p, self.weighted)
                output_array[j,i] = temp_dist
        return output_array

    def k_neighbours(self, x):
        """
        Find K nearest neighbours of each point in train dataset x
        Note that the point itself is not to be included in the set of k Nearest Neighbours
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            k nearest neighbours as a list of (neigh_dists, idx_of_neigh)
            neigh_dists -> N x k Matrix(float) - Dist of all input points to its k closest neighbours.
            idx_of_neigh -> N x k Matrix(int) - The (row index in the dataset) of the k closest neighbours of each input

            Note that each row of both neigh_dists and idx_of_neigh must be SORTED in increasing order of distance
        """
        # TODO
        number_of_trainings = len(x)
        output_array_weights = np.zeros(shape = (number_of_trainings,self.k_neigh), dtype=float)
        output_array_idx = np.zeros(shape = (number_of_trainings,self.k_neigh), dtype=int)

        distances = self.find_distance(x)
        for i in range(0,number_of_trainings):
            sorted_distances = sorted(distances[i])
            for j in range(0,self.k_neigh):
                output_array_weights[i,j] = sorted_distances[j]
                output_array_idx[i,j] = list(distances[i]).index(sorted_distances[j])
        return np.array([output_array_weights, output_array_idx])

        pass

    def predict(self, x):
        """
        Predict the target value of the inputs.
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            pred: Vector of length N (Predicted target value for each input)(int)
        """
        # TODO
        # As it is calssfication problem, we only need to send mode of the outputs for the k nearest neighbours
        k_nearest_neighbours = self.k_neighbours(x)
        predictions = np.zeros(shape = (len(x)), dtype=int)
        k_nearest_neighbours_idx = k_nearest_neighbours[1]
        for i in range(0,len(x)):
            neighbours_target = np.zeros(shape = (self.k_neigh), dtype=int)
            for j in range(0,len(k_nearest_neighbours_idx[i])):
                neighbours_target[j]=int(self.target[int(k_nearest_neighbours_idx[i][j])])          
            vals, counts = np.unique(neighbours_target, return_counts=True)
            mode = np.argwhere(counts == np.max(counts))
            predictions[i] = mode[0][0]
        return predictions

    def evaluate(self, x, y):
        """
        Evaluate Model on test data using 
            classification: accuracy metric
        Args:
            x: Test data (N x D) matrix(float)
            y: True target of test data(int)
        Returns:
            accuracy : (float.)
        """
        # TODO
        predictions = self.predict(x)
        right = 0
        total = len(y)
        for i in range(0,total) : 
            if predictions[i] == y[i]:
                right +=1
        percentage = (right/total)*100
        return percentage
