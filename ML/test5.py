import numpy as np
import random
import matplotlib.pyplot as plt

# data set
#fregehgthtrhrthrt
#fewfwgregehrh
# input : input data, feature
# H(x) -> input data : x1 -> xn
x_train = [ np.random.rand()  * 10 for _ in range(50)]
# 50
# output : label
# f(x) -> f(x2)
# y = label 
y_train = [val + np.random.rand() * 5 for val in x_train]

# BGC(Batch Gradient Descent) : 배치 경사 하강법
# 이용하여 선형 회귀 모델(Linear Rergeresion)을 구현 = Mean Squared Error

w = 0.0 # 초기 가중치
b = 0.0
learning_rate = 0.001 # 학습률 
epoch = 50  # 반복 횟수(학습률)
loss_history = []


# H(x) -> w * x + b
for num_of in range(epoch):
    gradient_w_sum = 0.0 # 기울기 합
    gradient_b_sum = 0.0
    loss = 0.0
    
    # GD 수행 후 최적의 w를 찾아야 함
    # zip(list1, list2) : list1, list2를 묶어줌
    for x, y in zip(x_train, y_train):
        gradient_w_sum += x * (w * x - y) # 기울기 합
        gradient_b_sum += (w * x - y)
        loss += (w * x + b - y)** 2
        
    # w값 업데이트
    # w = w - learning_rate * gradient_sum
    w = w - learning_rate * (gradient_w_sum / len(x_train))
    b = b - learning_rate * (gradient_b_sum / len(x_train))
    
    loss_history.append(loss/len(x_train))
    print(f"Loss: {loss/len(x_train)}")
    
# 테스트 데이터
x_test = [val for val in range(10)]
y_test = [w * val + b for val in x_test]


plt.subplots(1,2)
plt.scatter(x_train, y_train, color='pink')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression')
plt.plot(x_test, y_test, color='blue') 

plt.show() 
