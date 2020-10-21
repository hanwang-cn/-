import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
plt.figure(figsize = (6.5,6.5))

x = np.array([2.186,2.187,2.188,2.189,2.190,2.191,2.192,2.193,2.194])
y = np.array([8.4, 8.8, 9.0, 9.2,9.6,9.6,9.5,9.4,9.2])
#上面的实验数据换成自己的实验数据，就能生成图片，现在是九组实验数据。

x_new = np.linspace(x.min(),x.max(),300000) #300 represents number of points to make between T.min and T.max
y_smooth = make_interp_spline(x, y)(x_new)
plt.scatter(x, y, c='black',alpha = 0.5)  #alpha:透明度) c:颜色 #这是散点图，为了标注实验原始数据
plt.plot(x_new,y_smooth,c='red')#平滑后的折线图
 
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  #SimHei黑体
plt.rcParams['axes.unicode_minus'] = False
 
plt.title("频率和负载两端电压的关系", fontsize=24)#标题及字号
plt.xlim(2.185, 2.195)
plt.ylim(8.3, 9.7)
plt.xlabel("频率（kHz）", fontsize=24)#X轴标题及字号
plt.ylabel("峰-峰值（V）", fontsize=24)#Y轴标题及字号
plt.tick_params(axis='both', labelsize=14)#刻度大小
plt.grid(linestyle='-.') #网格线的设置
plt.show()
 
#plt.save('squares_plot.png'（文件名）, bbox_inches='tight'（将图表多余的空白部分剪掉）)
#用它替换plt.show实现自动保存图表
