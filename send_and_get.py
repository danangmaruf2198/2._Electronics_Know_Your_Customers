import ftplib
import time
import os

#myserver srv128.main-hosting.eu
#username u788641612
#password LGA772core5
#website=str(input('lebokne web e bos'))


def masuk():
    global ftp
    ftp=ftplib.FTP('srv128.main-hosting.eu')
    ftp.login('u788641612','LGA772core5')
    #print (ftp.getwelcome())
    #print ('saiki ning', ftp.pwd())
def setor(gambar):
    os.chdir('/media/pi/ANONYMOUS1/mechlab/ekyc/send')
    ftp.cwd('/domains/danangmaruf.esy.es/public_html/serverSend')
    print ('saiki ning', ftp.pwd())
    #upload= input ("ameh ngirim file opo?")
    ftp.storbinary('STOR '+ gambar, open(gambar, 'rb'))
    print("sudah keupload")
    print("bar gdbye")
def nerima(gambar):
    os.chdir('/media/pi/ANONYMOUS1/mechlab/ekyc/recieve')
    ftp.cwd('/domains/danangmaruf.esy.es/public_html/serverRecieve')
    print ('saiki ning', ftp.pwd())
    print gambar
    #download= input ("ameh jumuk file opo?")
    ftp.retrbinary('RETR '+ gambar, open(gambar, 'wb').write)
    print("sudah kedownload")
    ftp.quit()
    print("bar gdbye")
def keluar():
    waktuSekarang= str(time.asctime(time.localtime(time.time())))
    waktuSekarang=waktuSekarang[4:].strip().split()
    del waktuSekarang[3:4]
    waktuSekarang=str(waktuSekarang[0])+" "+str(waktuSekarang[1])+" "+str(waktuSekarang[2])
    
    exit()
