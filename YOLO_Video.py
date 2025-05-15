from ultralytics import YOLO
import cv2
import math
from timeit import default_timer as timer
from email_alert_function import em
import concurrent.futures

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from whatsapp_alert_function import whatsapp
from sms_alert_function import sms

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def em(receiver, image):
    sender = "nithinrohitian@gmail.com"
    password = "qakjaqgekbkozspd"  # Replace with your app-specific password (not regular Gmail password)

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = "Guardian Vision Alert"
    body = "Alert detected. Check the image or logs."

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Failed to send email:", e)



def video_detection(path_x,receiver):
    video_capture = path_x
    #Create a Webcam Object
    cap=cv2.VideoCapture(video_capture)

    # Gun Model 
    model=YOLO('ModelWeights/gun_nano_best.pt')
    classNames = ["Gun"]

    
    model2=YOLO('ModelWeights/Kniife_best.pt')
    classNames1 = ["Knife"]
    while True:
        success, img = cap.read()
        results=model(img,stream=True,conf=0.5)
        results2=model2(img,stream=True,conf=0.5)

        for r in results:
            boxes=r.boxes
            for box in boxes:
                x1,y1,x2,y2=box.xyxy[0]
                x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
                print(x1,y1,x2,y2)
                conf=math.ceil((box.conf[0]*100))/100
                cls=int(box.cls[0])
                class_name=classNames[cls]
                label=f'{class_name} {conf*100}%'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                print(t_size)
                c2 = x1 + t_size[0], y1 - t_size[1] - 3

                color = (105, 245,66)
                if (conf >=0.75):
                    color = (66, 138, 245)
                if (conf >= 0.9):
                    color = (66, 66, 245)
                
                cv2.rectangle(img, (x1,y1), (x2,y2), color ,3)
                cv2.rectangle(img, (x1,y1), c2, color, -1, cv2.LINE_AA)  # filled
                cv2.putText(img, label, (x1,y1-2),0, 1,[255,255,255], thickness=2,lineType=cv2.LINE_AA)
                print("Image",img)
                print("Receiver",receiver)
                if(conf>=0.9):
                    # em(receiver,img)
                    whatsapp()
                    sms()
        for r in results2:
            boxes=r.boxes
            for box in boxes:
                x1,y1,x2,y2=box.xyxy[0]
                x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
                print(x1,y1,x2,y2)
                conf=math.ceil((box.conf[0]*100))/100
                cls=int(box.cls[0])
                class_name=classNames1[cls]
                label=f'{class_name} {conf*100}%'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                print(t_size)
                c2 = x1 + t_size[0], y1 - t_size[1] - 3

                color = (105, 245,66)
                if (conf >=0.75):
                    color = (66, 138, 245)
                if (conf >= 0.9):
                    color = (66, 66, 245)
                
                cv2.rectangle(img, (x1,y1), (x2,y2), color ,3)
                cv2.rectangle(img, (x1,y1), c2, color, -1, cv2.LINE_AA)
                cv2.putText(img, label, (x1,y1-2),0, 1,[255,255,255], thickness=2,lineType=cv2.LINE_AA)

                print(img)
                if(conf>=0.9):
                    # em(receiver,img)
                    whatsapp()
                    sms()
                
        yield img 
        cv2.destroyAllWindows()