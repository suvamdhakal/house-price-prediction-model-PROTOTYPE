#THIS IS NOT THE FINAL MODEL
import numpy as np

X_train = np.array([
    [2104, 5, 1, 45],
    [1416, 3, 2, 40],
    [1534, 3, 2, 30],
    [852,  2, 1, 36],
    [1940, 4, 2, 25],
    [1800, 4, 2, 20],
    [1200, 3, 1, 15],
    [1600, 3, 2, 10],
    [2200, 5, 2, 15],
    [950,  2, 1, 50],
    [1350, 3, 1, 35],
    [1750, 4, 2, 30],
    [2000, 4, 2, 10],
    [1100, 2, 1, 25],
    [1450, 3, 2, 20],
    [2300, 5, 2, 5],
    [1250, 3, 1, 40],
    [1850, 4, 2, 35],
    [1000, 2, 1, 45],
    [1550, 3, 2, 15]
])

y_train = np.array([
    460,
    232,
    315,
    178,
    410,
    380,
    220,
    350,
    500,
    190,
    270,
    395,
    450,
    210,
    330,
    540,
    240,
    360,
    195,
    340
])

b_init = 0
w_init = np.zeros(X_train.shape[1])

def zscore_normalize_features(X):

    mean = np.mean(X, axis = 0)
    sd = np.std(X,axis = 0)

    X_normalized = (X - mean)/sd

    return X_normalized, mean, sd

X_norm, mean, sd = zscore_normalize_features(X_train)


def compute_cost(X,y,w,b):
    cost = 0.0
    m = X.shape[0]

    for i in range(m):
        cost += (np.dot(X[i], w)+b - y[i])**2

    cost = cost/(2*m)
    return cost

cost = compute_cost(X_norm, y_train, w_init, b_init)

def compute_gradient(X,y,w,b):
    m,n = X.shape
    dj_dw = np.zeros(n)
    dj_db = 0
    err = 0

    for i in range(m):
        err = (np.dot(X[i], w)+b) - y[i]

        for j in range(n):
            dj_dw[j] += err * X[i,j]

        dj_db += err

    dj_db = dj_db/m
    dj_dw = dj_dw/m

    return dj_dw, dj_db

def gradient_descent(X,y,w,b,alpha,num_iters):

    for i in range(num_iters):
        dj_dw, dj_db = compute_gradient(X, y, w, b)
        w = w - alpha * dj_dw
        b = b - alpha * dj_db

    return w, b


initial_w = np.zeros_like(w_init)
initial_b = 0

iterations = 10000
alpha = 0.1

w_final, b_final = gradient_descent(X_norm, y_train, initial_w, initial_b, alpha, iterations)

print(f"b, w found by gradient descent: {b_final}, {w_final}")
m, n = X_norm.shape

for i in range(m):
    print(f"prediction: {np.dot(X_norm[i], w_final)+ b_final:.2f}, target value = {y_train[i]}")

print(w_final)
print(b_final)


x = np.zeros(n)

for i in range(n):
    x[i] = float(input("enter the values of size, no of bedrooms, no of floors and age of the house "))

x_input_norm = (x - mean) / sd
print(f"the predicted price of house is ${((np.dot(w_final, x_input_norm) + b_final)*1000):.2f}")

