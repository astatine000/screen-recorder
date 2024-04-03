import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time


width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

dim=(width,height)
format =cv2.VideoWriter_fourcc(*'XVID')
filename='output,avi'
output=cv2.VideoWriter("test.avi",format,30.0,dim)
#duration
now_start_time=time.time()
duration=10

end_time=now_start_time+duration
#how to record video

while True:
    image =pyautogui.screenshot()
    frame_1=np.array(image)
    colour =cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)

    output.write(colour)
    currentime=time.time()

    if currentime > end_time:
        break

output.release()

print("end")