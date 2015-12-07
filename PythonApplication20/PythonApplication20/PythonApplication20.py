from matplotlib import pyplot as plt
import numpy as np


### 하나의 리스트나 배열이 주어질 경우, y축 값으로 처리
### x축 값은 0부터 같은 길이의 벡터를 만듦.
#plt.plot([1,2,3,4]) # y 축 
#plt.show()

#plt.plot([1,2,3,4],[1,4,9,16], 'ro-') # x 축, y 축, marker
#plt.show()

#t = np.arange(0., 5., 0.2)
#plt.plot(t, t, 'c--', t, t**2, 'ms', t, t**3, 'y^')
#plt.show()


## Create a figure of size 8x6 inches, 80 dots per inch
#plt.figure(figsize=(8, 6), dpi=80)
## Create a new subplot from a grid of 1x1 (row, col, viewpos)
#plt.subplot(1, 1, 1)

#x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
#c=np.cos(x)
#s=np.sin(x)
#plt.plot(x, c, color="cyan", linewidth=1.0, linestyle="-", label="cosine")
#plt.plot(x, s, color="magenta", linewidth=1.0, linestyle="-", label="sine")
#plt.legend(loc='upper left')
#plt.show()

## Set x limits
#plt.xlim(-4.0, 4.0)
## Set x ticks
#plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
## Set y limits
#plt.ylim(-1.0, 1.0)
## Set y ticks
#plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

#plt.show()


### 그래프 나누기 서브플롯 #### 

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

#t1 = np.arange(0.0, 5.0, 0.1)
#t2 = np.arange(0.0, 5.0, 0.02)

#plt.figure(1)
#plt.subplot(211) # 2x1 분할 하고 1 택
#plt.plot(t1, f(t1), 'co', t2, f(t2), 'y')

#plt.subplot(212) # 2x1 분할 하고 2 택
#plt.plot(t2, np.cos(2*np.pi*t2), 'm--')
#plt.show()



#### Spine : 축의 tick marks과 연결된 라인 #####

#ax = plt.gca() # gca stands for 'get current axis'
#ax.spines['right'].set_color('yellow')
#ax.spines['top'].set_color('black')
#ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom'].set_position(('data',0.7))
#ax.yaxis.set_ticks_position('left')
#ax.spines['left'].set_position(('data',0.7))

#x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
#c=np.cos(x)
#s=np.sin(x)
#plt.plot(x, c, color="cyan", linewidth=1.0, linestyle="-", label="cosine")
#plt.plot(x, s, color="magenta", linewidth=1.0, linestyle="-", label="sine")

#plt.show()


####### Regular Plots 오밀조밀 점들의 분포 #############
#n = 1024
#X = np.random.normal(0, 1, n)
#Y = np.random.normal(0, 1, n)
#T = np.arctan2(Y, X)
#plt.axes([0.025, 0.025, 0.95, 0.95])
#plt.scatter(X, Y, s=75, c=T, alpha=.5)
#plt.xlim(-1.5, 1.5)
#plt.xticks(())
#plt.ylim(-1.5, 1.5)
#plt.yticks(())
#plt.show()


####### Contour Plots 등고선 #############
#def f(x,y):
# return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)
#n = 256
#x = np.linspace(-3, 3, n)
#y = np.linspace(-3, 3, n)
#X,Y = np.meshgrid(x, y)

#plt.axes([0.025, 0.025, 0.95, 0.95])

## contourf : draw filled contours( X, Y : 좌표,  f(X,Y) : contour plot, 8 : 주어진 레벨까지 선택)
#plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot) 
#C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5) #contour : draw contour lines
#plt.clabel(C, inline=1, fontsize=10)

#plt.xticks(()) 
#plt.yticks(())
#plt.show()



####### Imshow 등고선 #############

def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3 ) * np.exp(-x ** 2 - y ** 2)

n = 10
x = np.linspace(-3, 3, 3.5 * n)
y = np.linspace(-3, 3, 3.0 * n)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.imshow(Z, interpolation='nearest', cmap='bone', origin='lower')
plt.colorbar(shrink=.92)

plt.xticks(())
plt.yticks(())
plt.show()