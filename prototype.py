#THIS IS NOT THE FINAL MODEL
import numpy as np

X_train = np.array([
    [2104,5,1,45],
    [1416, 3, 2, 40],
    [852,2,1,35]
    ])
y_train = np.array([460,232,178])

b_init = 785.1811367994083
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618])

def compute_cost(X,y,w,b):
    cost = 0.0
    m = X.shape[0]
    for i in range(m):
        cost += (np.dot(X[i], w)+b - y[i])**2
    cost = cost/(2*m)
    return cost

cost = compute_cost(X_train, y_train, w_init, b_init)

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

iterations = 1000
alpha = 5.0e-7

w_final, b_final = gradient_descent(X_train, y_train, initial_w, initial_b, alpha, iterations)

print(f"b, w found by gradient descent: {b_final}, {w_final}")
m, n = X_train.shape
for i in range(m):
    print(f"prediction: {np.dot(X_train[i], w_final)+ b_final:.2f}, target value = {y_train[i]}")

print(w_final)
print(b_final)


x = np.zeros(n)
for i in range(n):
    x[i] = int(input("enter the values of size, no of bedrooms, no of floors and age of the house "))

print(f"the predicted price of house is {(np.dot(w_final, x) + b_final)*1000} dollars")
