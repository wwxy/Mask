import cv2
img = cv2.imread('image1.jpg')
imgInfo = img.shape

size = (imgInfo[1],imgInfo[0])
print(size)

videoWrite = cv2.VideoWriter('2.mp4',-1,5,size)

for i in range(1,11):
 
    fileName = 'image'+str(i)+'.jpg'
   
    img = cv2.imread(fileName)
    
    videoWrite.write(img)
    videoWrite.release()  
print('end!')