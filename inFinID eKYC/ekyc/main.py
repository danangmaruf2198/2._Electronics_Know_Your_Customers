'''
#ambil gambar pake library send and request
case misal server mati harus pake volatile variable. solustion= coba redefiniton variable jumlahnya
#tambah coding untuk otomatis convert banyak gambar baru
'''
import ftplib
import send_and_get
import time
import numpy as np
#import imageprocessing
waktuSekarang= time.asctime(time.localtime(time.time()))
jumlahDataLalu=0
data=[]

def ambilNama(calon):
    global a,h,r,namaGambar=0,0,'',[]
    for i in calon:
        h=i[29:].strip().split()
        if len(h)>6:
            for x in range(len(h)-5):
                if x>0:
                    r=r+" "+h[x+5]
                else:
                    r=r+h[x+5]
                namaGambar.append(r)
                r=''
                a+=1
        else:
            namaGambar.append(h[5])
    print namaGambar



while True:
    send_and_get.masuk()
    send_and_get.ftp.cwd('/domains/danangmaruf.esy.es/public_html/serverRecieve')
    send_and_get.ftp.dir('-t',data.append)
    jumlahData= len(data)
    #print str(jumlahData) +" "+ str(jumlahDataLalu)
    if jumlahDataLalu:
        if jumlahData != jumlahDataLalu:
            gambarMasuk= jumlahData-jumlahDataLalu
            del data[gambarMasuk+1:jumlahData]
            del data[0:1]
            dapetGambar=1
            break
    else:
        print "sama"
        jumlahDataLalu=jumlahData
    
    print "sama"
    data=[]
    send_and_get.ftp.quit()

ambilNama(data)
send_and_get.nerima(namaGambar)

#ambil gambar dari server
#coding dapetin nama gambar
'''   
import imageprocessing
for dapetGambar ==1 and jumlahGambarBaru < gambarMasuk:
    gambarBaru="E:/mechlab/ekyc/"+str(lokasiGambarBaru)
    imageprocessing.dataMasuk(gambarBaru)

>>> this_morning = datetime.datetime(2009, 12, 2, 9, 30)
>>> last_night = datetime.datetime(2009, 12, 1, 20, 0)
>>> this_morning.time() < last_night.time()
True
>>> str(array[1]).split("    ")
['drwxr-xr-x   7 u788641612 o36505844', ' 4096 Jan 20 09:29 ..']
>>> 
'''
