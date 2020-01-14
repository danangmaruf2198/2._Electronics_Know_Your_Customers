'''
#ambil gambar pake library send and request
case misal server mati harus pake volatile variable. solustion= coba redefiniton variable jumlahnya
#coding ngirim respon gambar 
'''
import ftplib
import send_and_get
import time
import numpy as np
import imageprocessing

waktuSekarang= time.asctime(time.localtime(time.time()))
jumlahDataLalu=0
data=[]

def ambilNama(calon):
    global namaGambar
    a,h,r,namaGambar=0,0,'',[]
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
        if len(h)<=6:
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
for i in namaGambar:
    send_and_get.nerima(i) 
    gambarBaru='1|/media/pi/ANONYMOUS1/mechlab/ekyc/'+i
    imageprocessing.dataMasuk(gambarBaru)
    imageprocessing.pilihAkun(imageprocessing.nilai)
    #print imageprocessing.lokasiGambar
    imageprocessing.prosesGambar(imageprocessing.lokasiGambar)
setor(imageprocessing.akun)
cv2.waitKey(0)
cv2.destroyAllWindows()


#bikin hosting isinya tabel nama gambar dan nik misal nama gambar baru diupload nanti bisa kolom nik kosong dan server harus ambil gambar trus di convert trus di upload baru nik ada
