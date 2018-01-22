import numpy as np

x= np.array([1,2,3])
print("x:",x)
print("type of x:",type(x))
print()

y=np.array([2,4,6])
print('y:',y)
print('x+y:',x+y) # 연산은 각각의 원소끼리 한다
print('x-y:',x-y)
print('x*y:',x*y)
print('x/y:',x/y)
print('x+2:',x+2)
print('x/2:',x/2)
print()

a=np.array([[1,2],[3,4]]) # 2차원 배열
print('a:',a)
print(a.shape)
print(a.dtype)
print()

b=np.array([[3,0],[0,6]]) #곱은 행렬곱 형태가 아닌 그냥 원소끼리의 곱
print('b;',b)
print('a+b:',a+b)
print('a*b:',a*b)
print()

print("브로드캐스트")
b=np.array([10,20])
print("b:",b)
print('a*b:',a*b) # b가 [[10,20],[10,20]]으로 알아서 인식댐
print()

x=np.array([[51,55],[14,19],[0,4]])
print('x')
print(x)
print('x[0]:',x[0])
print('x[0][1]:',x[0][1])
print()

print('for문')
for row in x:
    print (row) #이 형식으로도 접근가능
print()

print('flatten(일렬화)')
x=x.flatten()
print(x)
print(x[np.array([0,2,4])])
print()

print('bool 연산')
print(x>15)
print(x[x>15])
