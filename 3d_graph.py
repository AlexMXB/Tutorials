from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import time

# fig = plt.figure()
# ax = fig.add_subplot(111,projection='3d')
# X,Y,Z = np.arange(10),[2,1,5,3,6,8,9,4,7,8],[5,6,3,2,1,4,7,9,8,2]
# ax.plot_wireframe(X,Y,Z)

# X =[1,5,2,3,6,9,4,7,8,5]
# Y =[7,5,2,6,3,1,4,8,9,2]
# Z =[2,3,6,5,4,1,7,8,9,6]
# ax.scatter(X,Y,Z,c='r',marker='o')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# X =[1,5,2,3,6,9,4,7,8,5]
# Y =[7,5,2,6,3,1,4,8,9,2]
# Z =[2,3,6,5,4,1,7,8,9,6]

# Xs =[-1,5,2,-3,6,9,-4,7,8,5]
# Ys =[-7,5,2,6,-3,1,4,8,-9,2]
# Zs =[2,-3,6,-5,4,1,7,-8,9,6]

# ax.scatter(X,Y,Z,c='r',marker='o')
# ax.scatter(Xs,Ys,Zs,c='b',marker='^')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# Xpos =[1,5,2,3,6,9,4,7,8,5]
# Ypos =[7,5,2,6,3,1,4,8,9,2]
# Zpos =[0,0,0,0,0,0,0,0,0,0]

# dx = np.ones(10)
# dy = np.ones(10)
# dz = [1,2,3,4,5,6,7,8,9,10]

# ax.bar3d(Xpos,Ypos,Zpos,dx,dy,dz,color='#00ceaa')
# x,y,z = axes3d.get_test_data(0.5)
# ax.plot_wireframe(x,y,z,rstride=1,cstride=1)

# plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
	pullData = open('sample.txt').read()
	dataArray = pullData.split('\n')
	xvar = []
	yvar = []
	for each in dataArray:
		if len(each)>1:
			x,y = each.split(',')
			xvar.append(int(x))
			yvar.append(int(y))
	ax1.plot(xvar,yvar)
ani = animation.FuncAnimation(fig, animate,interval=1000)
plt.show()