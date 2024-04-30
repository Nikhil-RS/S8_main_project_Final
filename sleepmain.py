import cv2
from functools import wraps
from pygame import mixer
import time
import mysql.connector

sql=mysql.connector.connect(host="localhost",user="root",passwd="nikhil@695521",database="project")
mql=sql.cursor()
global count2
count2=0
lastsave = 0
def counter(func):
    @wraps(func)
    def tmp(*args, **kwargs):
        tmp.count += 1
        global lastsave
        if time.time() - lastsave > 3:
            # this is in seconds, so 5 minutes = 300 seconds
            lastsave = time.time()
            tmp.count = 0
        return func(*args, **kwargs)
    tmp.count = 0
    return tmp


face_cascade = cv2.CascadeClassifier(r'E:\Mini project\haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier(r'E:\Mini project\haarcascade_eye.xml')

cap = cv2.VideoCapture(0)


@counter
def closed():
   global count2
   count2=count2+1
   print(count2)
   print("Eye Closed")
def openeye():
  print ("Eye is Open")


def sound():
    mixer.init()
    mixer.music.load(r'E:\Mini project\alram.mp3')
    mixer.music.play()
while 1:
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
   

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
     

        if eyes is not ():
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                count2=0
                openeye()   
        else:
           closed()
           if closed.count == 2:
               sound()
           if closed.count >3:
            mql.execute("select status from condtion")
            mrec=mql.fetchall()
            for x in mrec:
                (a,)=x
                if a=="stroke detected":
                    from sos import *
               
    cv2.imshow('img', img)
    key=cv2.waitKey(25)
    if key==27:
        break


cap.release()
cv2.destroyAllWindows()
