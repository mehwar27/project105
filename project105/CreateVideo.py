import os
import cv2


path = "Images"


Images=[]


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)


frame = cv2.imread(images[0])
height , width ,chanels = frame.shape
size= (width , height)

out = cv2.VideoWriter("project105.mp4",cv2.VideoWriter_fourcc(*'DIVX'),20, size )


for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)
    
out.release() # releasing the video generated

print("Done")




cv2.waitKey(0)

