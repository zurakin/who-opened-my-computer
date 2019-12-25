import smtplib
from email.message import EmailMessage
import cv2 ,time
import imghdr
from datetime import datetime

EMAIL_ADDRESS = 'happyzura10@gmail.com'
EMAIL_PASSWORD = '********'

contacts = ['happyzura10@gmail.com']
current_time = datetime.now()
now = current_time.strftime('%D %H:%M')
msg = EmailMessage()
msg['Subject'] = f'login notification'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)

msg.set_content(f"Your desktop has been opened at : {now}\n below is a picture fo the intruder")


video = cv2.VideoCapture(0)
for _ in range(5):
    check,frame = video.read()
video.release()
image_path = current_time.strftime('pictures//%d%m%y %H.%M.png')
cv2.imwrite(image_path,frame)
key =cv2.waitKey(0)
cv2.destroyAllWindows()


files = [image_path]

for file in files:
    #rb for read binary
    with open(file, 'rb') as f:
        file_data = f.read()
        #get the type of the image
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type,filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    
