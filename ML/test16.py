samples = []
y = []

w = [0.2, 0.3]
b = 0.1

gradient_w = [0.0, 0.0]
gradient_b = 0.0

for dp, y_ in zip(samples, y):
    #　予測値
    predict_y = w[0] * dp[0] + w[1] * dp[1] + b
    #　誤差　:　予測値　－　正解
    error = predict_y - y_
    # 기울기 값 누적
    gradient_w[0] += dp[0] * error
    gradient_w[1] += dp[1] * error
    gradient_b += error
    
    
# update gradient of each w
w[0] = w[0] - gradient_w[0] / len(samples)
w[1] = w[1] - gradient_w[1] / len(samples)

# update gradient of b
b = b - gradient_b / len(samples)