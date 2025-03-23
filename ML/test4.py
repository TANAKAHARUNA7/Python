import numpy as np
import matplotlib.pyplot as plt

# Data set
# input 
# # input Data, features
# H(x) -> input data : x1 -> xn
x_train = [ np.random .rand() * 10 for _ in range(50)]
# y = lable
y_train = [val + np.random.rand() * 5 for val in x_train]

# BGC(Batch Gradient Descent) 배지경사하강법을
# 이용하여 Linear Rergeresion 적용
w = 0.0
learning_rate = 0.001
gradient_sum = 0.0
epoch = 50
# GD 遂行後最適のW値を導出
for x, y in zip(x_train, y_train):
    gradient_sum += x * (w * x - y)
# w値アップデート
# w = w - learning_rate * gradient_sum      
    w = w - learning_rate * (gradient_sum / len(x_train))

x_train = [val for val in  range(10)]
y_train = [val for ]


print(x_train)
print("-" * 100)
print(y_train)

plt.scatter(x_train, y_train, color = "blue")
plt.show()

# output
# label
# f(x) -> f(x2)  


