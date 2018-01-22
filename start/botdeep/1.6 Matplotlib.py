import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,6,0.1) #0~6(6은포함x)에서 0.1 간격으로 1차원 array 생성
y1=np.sin(x)
y2=np.cos(x)

plt.plot(x,y1,label="sin") #그리는거 sin 나타냄
plt.plot(x,y2,linestyle='--',label='cos')# 점선(?) cos 나타냄
plt.xlabel("x") #x축 이름
plt.ylabel('y') #y축 이름
plt.title('sin cos') #제목

plt.legend()#왼쪽 밑에 라벨 표시
plt.show() #보이기