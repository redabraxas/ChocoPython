import numpy as np
from matplotlib import pyplot as plt

# np.array 는 모두 같은 데이터형을 가짐
data = np.array([[1,2,3],[4,5,6],[7,8,9]])


data.ndim
len(data) # 첫번째 dimension 크기
data.shape
len(data)


# 데이터형 변경
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
data.astype(np.float)
data = np.array(['1','2','3'])
data.astype(np.int)

# 데이터형 지정
data = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=float)
data = np.array([1,2,3], dtype=complex)


# 1로 채워진 행렬
np.ones((3,2))
# 0으로 채워진 행렬np.zeros((3,2))# 단위 행렬 & 대각행렬np.eye((3))np.diag(np.array([1,2,3,4]))# 전치 행렬
data.T


# 범위 지정하여 등간격 배열 만들기
data= np.arange(10) # 0, . . . n-1
data= np.arange(10,1,-1) #start, end(exclusive), step
data= np.arange(10,1,-1)[:, np.newaxis] #행 증가
data= np.arange(2, 8, dtype=np.float)
data= np.arange(35).reshape(5,7)


data= np.linspace(1., 3., 5) # start, end, num-points
data= np.linspace(1., 4., 5, endpoint=False)  # 마지막수 포함할껀지


## 난수 생성
data = np.random.rand(4) # 0~1
data = np.random.randn(4)  # 가우시안 펑션이용: -1 < < 1

##### 응용 예시
data = np.loadtxt('data.txt')
year, hares, lynxes, carrots = data.T
#plt.plot(year, hares, year, lynxes, year, carrots)
#plt.show()
print(data)

# 년도별 평균?
# 년도별 표준편차?
# 매년 가장높은 개체수의 종은?



data[0] #첫행
data[2][0] #두번째행의 첫칸
data[2,0]
data[-1] #마지막행
data[0:2] #0번에서 2-1번째 행
data[:2] #0번~2-1번째 행
data[1:4:2] # start:end:step
data[1:4:2, ::3]
data[::-1]



### 인덱스 배열
x= np.arange(10,1,-1)
# 3 = x인덱스
x[np.array([3,3,1,8])]
x[np.array([[1,1],[2,3]])]

y=np.arange(35).reshape(5,7)
y[np.array([0,2,4])] # 행번호 가지고 출력
b = y>20
y[b]




#boolean masks
data = np.arange(36).reshape(6,6)

mask = np.array(np.array([1,0,1,0,0,1], dtype=bool))
data[mask,2]


mask1=np.array([0,1,2,3,4])
mask2=np.array([1,2,3,4,5])
data[mask1,mask2]
print(data[mask1,mask2])

mask3 = np.array([0,2,5])
data[3,mask3]
