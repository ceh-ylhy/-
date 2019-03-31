import cv2
import os
def VideoToImages(file):
    # 导入视频
    cap = cv2.VideoCapture(file)
    # 以文件的源路径+_png来创建图片存放路径
    os.makedirs(file+"_png//")
    # 设置保存路径
    outfile_path = file+"_png//"
    print(outfile_path)
    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        params = []
        params.append(1)
        i = i + 1
        cv2.imwrite(outfile_path+str(i)+'.png',frame,params)
    cap.release()
    cv2.destroyAllWindows()

num = 1
pathsaves = "//home//ylhy//nn//" + "sp_%d.avi" % (num)
while os.path.exists(pathsaves):
    VideoToImages(pathsaves)
    num+=1
    pathsaves = "//home//ylhy//nn//" + "sp_%d.avi" % (num)
