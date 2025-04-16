samples = []
y = []

w = 0.2
b = 0.3

gradient_b = 0.0
gradient_w = 0.0


for f,y_ in zip(y,samples):
    predict_y = w * f + b
    
    error = predict_y - y_
    
    gradient_w += error * f
    
    gradient_b += error
    
w = w - gradient_w / len(samples)
b = b - gradient_b / len(samples)