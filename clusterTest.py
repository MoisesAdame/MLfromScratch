import math as mt
import numpy as np
X_train = []
y_train = []

for i in range(500):
    scale_radius = np.random.randint(-100, 101) / 100
    scale_angle = np.random.randint(0, 101) / 100
    X_train.append([(1 + ((0.2)**0.5)*scale_radius*mt.cos(2*mt.pi*scale_angle)) , (2 + ((0.2)**0.5)*scale_radius*mt.sin(2*mt.pi*scale_angle))])
    X_train.append([(2 + ((0.2)**0.5)*scale_radius*mt.cos(2*mt.pi*scale_angle)) , (1 + ((0.2)**0.5)*scale_radius*mt.sin(2*mt.pi*scale_angle))])
    y_train.append(0)
    y_train.append(1)

X_train = np.array(X_train)
y_train = np.array(y_train)

X_predict = np.array([[1.5,2], [1,1.5]])
