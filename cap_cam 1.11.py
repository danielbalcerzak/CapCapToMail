from cv2 import VideoCapture, CAP_DSHOW, resize, imwrite
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from time import time



def send_email():
    global message
    message['Subject'] = "Photo"
    smtp_object = SMTP('smtp', 587)
    smtp_object.ehlo()
    smtp_object.starttls()
    smtp_object.login('email-profile', 'email-pass')
    i = 1
    while i != 10:
        start = time()
        end = start
        while end - start < 10:
            end = time()
        addphoto(i)
        i += 1
    smtp_object.sendmail("Nobody", "email", message.as_string())
    smtp_object.quit()


def addphoto(i):
    global message
    cap = VideoCapture(0, CAP_DSHOW)
    ret, frame = cap.read()
    frame = resize(frame, None, fx=0.5, fy=0.5)
    imwrite('picture.jpg', frame)
    fp = open('picture.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<image{}>'.format(i))
    message.attach(msgImage)


if __name__ == '__main__':
    message = MIMEMultipart('related')
    send_email()
