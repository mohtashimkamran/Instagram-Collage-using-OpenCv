import numpy as np
import pandas as pd
import cv2 
import matplotlib.pyplot as plt
topleft=cv2.imread('top_left.jpg',1)#1 for showing colored image
topleftfinal=cv2.resize(topleft,(200,200))
topleftwithborder=cv2.copyMakeBorder(topleftfinal,10,5,10,5,cv2.BORDER_CONSTANT)
plt.imshow(topleft)
plt.imshow(topleftwithborder)
plt.show()

topright=cv2.imread('top_right.jpg',1)#1 for showing colored image
toprightfinal=cv2.resize(topright,(200,200))
toprightwithborder=cv2.copyMakeBorder(toprightfinal,10,5,5,10,cv2.BORDER_CONSTANT)


bottomleft=cv2.imread('bottom_left.jpg',1)#1 for showing colored image
bottomleftfinal=cv2.resize(bottomleft,(200,200))
bottomleftwithborder=cv2.copyMakeBorder(bottomleftfinal,5,10,10,5,cv2.BORDER_CONSTANT)


bottomright=cv2.imread('bottom_right.jpg',1)#1 for showing colored image
bottomrightfinal=cv2.resize(bottomright,(200,200))
bottomrightwithborder=cv2.copyMakeBorder(bottomrightfinal,5,10,5,10,cv2.BORDER_CONSTANT)  #top, bottom, left, right

bottomright=cv2.imread('bottom_right.jpg',1)#1 for showing colored image
bottomrightfinal=cv2.resize(bottomright,(200,200))
bottomrightwithborder=cv2.copyMakeBorder(bottomrightfinal,5,10,5,10,cv2.BORDER_CONSTANT)  #top, bottom, left, right

center=cv2.imread('center.jpeg',1)#1 for showing colored image
centerfinal=cv2.resize(center,(100,100))
centerwithborder=cv2.copyMakeBorder(centerfinal,10,10,10,10,cv2.BORDER_CONSTANT)  #top, bottom, left, right

img1=np.hstack((topleftwithborder,toprightwithborder))
img2=np.hstack((bottomleftwithborder,bottomrightwithborder))
img=np.vstack((img1,img2))
im=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

centerfwithborder=cv2.cvtColor(centerfwithborder,cv2.COLOR_BGR2RGB)
im[155:275,155:275]=centerfwithborder
plt.imshow(im)
plt.show()

# arr=np.array(im)
# df=pd.DataFrame(arr.reshape(-1,3),columns=['r','g','b'])
# print(arr.shape)
# df.to_csv("instagram_collage.csv",index=False)