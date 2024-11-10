import matplotlib.pyplot as plt
import random

x = [x_value for x_value in range(1,100)]

y = [random.randint(1,100) for y_value in range(1,100)]

plt.rc('font', family = 'Malgun Gothic')

plt.plot(x,y)

plt.title('기본 선형 그래프')

plt.xlabel('X 축')

plt.ylabel('Y 축')

plt.show()

plt.plot(x, y, color='red', linestyle='--', linewidth= 2)

plt.title('세부 설정된 그래프')

plt.xlabel('X 축')

plt.ylabel('Y 축')

plt.grid(True)

plt.show()

plt.scatter(x, y, color='blue')

plt.title('산점도 그래프')

plt.xlabel('X 축')

plt.ylabel('Y 축')

plt.show()
