import cv2
import os
#data input should be "nilaiAkun|"+"lokasiGambar"
biodata=['nama','tanggal lahir','alamat','agama','SPerkawinan','Pekerjaan','kewarganegaraan']
def dataMasuk(dataInput):
    global lokasiGambar,nilai
    #dataInput=str(input('masukan kodeAkun dan lokasigambar'))
    dataInput= dataInput.split('|')
    nilai= int (dataInput[0])
    lokasiGambar= str(dataInput[1])
    #print str(nilai)+" "+str(lokasi)
def pilihAkun(lala):
    global akun
    switcher={
        1: "danang.txt",
        2: "dadang.txt",
        3: "rifan.txt"
        }
    akun=switcher.get(lala)
    print akun
def prosesGambar(lala):    
   # code untuk image recognition
    gambar=cv2.imread(lala,0)
    print lala
    #gray = cv2.cvtColor(gambar,cv2.COLOR_BGR2GRAY)
    cv2.imshow('before',gambar)
    os.chdir('/media/pi/ANONYMOUS1/mechlab/ekyc/send')
    #cv2.imshow ('gray',gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

