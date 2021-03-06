import smtplib, os
from email.message import EmailMessage
import cv2 ,time
import imghdr
from datetime import datetime

#create the pictures folder if it doesn't already exist
os.chdir('C://Users//ilyas//Documents//GitHub//who-opened-my-computer')
try:
    os.mkdir('pictures')
except:
    pass

EMAIL_ADDRESS = os.environ.get('EMAIL')
EMAIL_PASSWORD = os.environ.get('PASSWORD')


contacts = ['azirarilyass@gmail.com']
current_time = datetime.now()
now = current_time.strftime('%D %H:%M')
msg = EmailMessage()
msg['Subject'] = f'login notification'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)

msg.set_content(f"Your desktop has been opened at : {now}\n below is a picture of the intruder")

for _ in range(3):
    try:
        video = cv2.VideoCapture(0)
        for _ in range(5):
            check,frame = video.read()
        video.release()
        image_path = current_time.strftime('pictures//%d%m%y %H.%M.png')
        cv2.imwrite(image_path,frame)
    except:
        time.sleep(5)
        continue


files = [image_path]

for file in files:
    #rb for read binary
    with open(file, 'rb') as f:
        file_data = f.read()
        #get the type of the image
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type,filename = file_name)


for _ in range(3):
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
    except:
        time.sleep(5)
        continue
