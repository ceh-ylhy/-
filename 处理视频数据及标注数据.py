import cv2

# 导入一个本地视频赋给cap
cap = cv2.VideoCapture("//home//ylhy//桌面//ad.mp4")

# 获取视频的帧速率fps
fps = int(cap.get(cv2.CAP_PROP_FPS))
# 获取视频的宽高
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# 设置视频的解码器
fourcc = cv2.VideoWriter_fourcc('D','I','V','X')
# 获取视频的总帧数
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# 10秒的总帧率
framss = 10*fps

print('视频详细信息：\n\tfps：',fps,'\n\t宽、高：',size,'\n\t总帧数：',frames,'\n\t解码器：',fourcc)

# i用来计数每一帧视频，n用来计数视频个数
i = 0
n = 1
print('写入第%d个视频中...'%n)
out = cv2.VideoWriter('//home//ylhy//nn//sp_' + str(n) + '.avi', fourcc, fps, size)

while True:
    # .read()方法将会返回一个布尔值和一组矩阵
    ret,frame = cap.read()
    if ret:
        i = i + 1

        if(i%framss == 0):
            n = n + 1
            print('写入第%d个视频中...'%n)
            # 创建一个视频对象，并依次设置输出路径下的名称、解码器、每秒帧率、视频宽高
            out = cv2.VideoWriter('//home//ylhy//nn//sp_' + str(n) + '.avi', fourcc, fps, size)
        out.write(frame)
    else:
        print('...结束，本次处理输出共',n,'个视频。')
        break
# 释放内存资源
cap.release()
out.release()
cv2.destroyAllWindows()
