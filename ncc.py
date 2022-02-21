import numpy as np
class ncc:
    def __init__(self, clusters = 2):
        self.clusters = clusters

    def model(self, X_train, y_train, X_predict):
        pass

    def _model(self, X_train, y_train, x_predict):
        pass

    def _boundary(self, centroid1, centroid2):
        # The middle point between each centroid is obtained
        if centroid1.shape[0] >= centroid1.shape[0]:
            dimensions_centroid = centroid1.shape[0]
        else:
            dimensions_centroid = centroid2.shape[0]
        
        middle_point = []
        for i in range(dimensions_centroid):
            middle_point.append((centroid1[i] + centroid2[i]) /2)
        middle_point = tuple(middle_point)
    
        # The slope of the boundary is obtained
        boundary_slopes = []
        for j in range(dimensions_centroid - 1):
            boundary_slopes.append(- (centroid1[j] - centroid2[j])/(centroid1[-1] - centroid2[-1]))
        boundary_slopes = tuple(boundary_slopes)

        # The model coefficients are returned (slope1, slope2,...,slopen, indep)
        # All the slopes are returned
        coeficcients = []
        for k in range(len(boundary_slopes)):
            coeficcients.append(boundary_slopes[k])
        
        # The independent value is obtained and appended to the coefficient list
        independent_coeficcient = middle_point[-1]
        for dim in range(dimensions_centroid - 1):
            independent_coeficcient += (-coeficcients[dim] * middle_point[dim])
        coeficcients.append(independent_coeficcient)

        return tuple(coeficcients)

    def centroid(self, X_train, y_train):
        # We obtain all the centroids of the different clusters
        clusters = np.unique(y_train)
        centroids = [self._centroid(X_train, y_train, cluster) for cluster in clusters]
        centroids = np.array(centroids)

        return centroids

    def _centroid(self, X_train, y_train, cluster):
        # The cooirdinates of all the samples of a certain 
        # cluster are stored in an array.
        cluster_indices = np.argwhere(y_train == cluster)
        cluster_data = [X_train[x, :][0] for x in cluster_indices[:]]
        cluster_data = np.array(cluster_data)

        # We use the centroid formulas to obtain a tuple 
        # that represents the centroid of the given cluster
        centroid = []
        for i in range(cluster_data.shape[1]):
            some_coordinate_centroid = 2 * np.sum(cluster_data[:, i]) / cluster_data.size
            centroid.append(some_coordinate_centroid)
        
        return tuple(centroid)