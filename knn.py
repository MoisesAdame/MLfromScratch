import numpy as np

def euclidean_dist(x, y):
    return np.sum((x -  y)**2)

class knn:
    def __init__(self, k = 3):
        knn.k = k

    def model(self, X_train, y_train, X_predict):
        y_predict = [self._model(X_train, y_train, x_predictors) for x_predictors in X_predict]
        y_predict = np.array(y_predict)
        return y_predict

    def _model(self, X_train, y_train, x_predict):
        # List with all the distances from x to y
        dist_x = [euclidean_dist(x_predict, i) for i in X_train]
        dist_x = np.array(dist_x)

        # Array with indeces of closest points
        closest_to_x_indices = np.argsort(dist_x)
        closest_to_x_indices = closest_to_x_indices[:knn.k]

        # The most common is chosen
        closest_to_x_names = [y_train[indices] for indices in closest_to_x_indices]
        return np.bincount(closest_to_x_names).argmax()