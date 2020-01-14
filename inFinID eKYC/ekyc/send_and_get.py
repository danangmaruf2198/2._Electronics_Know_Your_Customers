import ftplib
import time
#myserver srv128.main-hosting.eu
#username u788641612
#password LGA772core5
#website=str(input('lebokne web e bos'))


def masuk():
    global ftp
    ftp=ftplib.FTP('srv128.main-hosting.eu')
    ftp.login('u788641612','LGA772core5')
    print (ftp.getwelcome())
    print ('saiki ning', ftp.pwd())
def setor():
    ftp.cwd('/domains/danangmaruf.esy.es/public_html/serverSend')
    print ('saiki ning', ftp.pwd())
    upload= input ("ameh ngirim file opo?")
    ftp.storbinary('STOR '+ upload, open(upload, 'rb'))
    print("sudah keupload")
    print("bar gdbye")
def nerima(gambar):
    ftp.cwd('/domains/danangmaruf.esy.es/public_html/serverRecieve')
    print ('saiki ning', ftp.pwd())
    #download= input ("ameh jumuk file opo?")
    ftp.retrbinary('RETR '+ gambar, open(gambar, 'wb').write)
    print("sudah kedownload")
    ftp.quit()
    print("bar gdbye")

#tambah fungsi urutkan sesuai tanggal dan waktu
#ambil yang paling atas
'''for i in data:
	h=i[29:].strip().split()
	if len(h)>6:
		for x in range(len(h)-6):
			nana[a]=h[x+5]
	a+=1
'''
