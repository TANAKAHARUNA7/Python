import numpy as np
import matplotlib.pyplot as plt
 

# 미래의 인구를 계산하는 프로그램
# 구하고자 하는 연도 입력을 받는다
input_year = int(input("구하고자 하는 연도： "))

#기준년도
standard_year = 210000

# t년 = 2020년 - 1999년 
# t년전 인구
t_year_hyuman = 89000

# 기준년도 인구수 / t년전 인구수 ** 1 / t년 -1 
r = ((standard_year / t_year_hyuman) ** (1 / 21)) - 1

# 
year = (1 + r) ** (input_year - 2020) * standard_year

print(f"{input_year}년 인구는 {year:.0f}명")