import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

W1 = np.random.rand(2, 3)
W2 = np.random.rand(3, 1)

hidden = sigmoid(np.dot(X, W1))
output = sigmoid(np.dot(hidden, W2))

print("Network Output:")
print(output)
