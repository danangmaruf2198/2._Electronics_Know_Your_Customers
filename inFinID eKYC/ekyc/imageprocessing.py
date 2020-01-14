import cv2

#data input should be "nilaiAkun|"+"lokasiGambar"
dataInput=0
def dataMasuk(dataInput):
    #dataInput=str(input('masukan kodeAkun dan lokasigambar'))
    dataInput= dataInput.split('|')
    nilai= int (dataInput[0])
    lokasiGambar= str(dataInput[1])
    #print str(nilai)+" "+str(lokasi)
def pilihAkun(lala):
    switcher={
        1: "danang",
        2: "dadang",
        3: "rifan"
        }
    akun=switcher.get(lala)
    print akun
def prosesGambar(lala):    
   # code untuk image recognition
    gambar=cv2.imread(lala,0)
    #gray = cv2.cvtColor(gambar,cv2.COLOR_BGR2GRAY)
    cv2.imshow('before',gambar)
    #cv2.imshow ('gray',gray)
'''
pilihAkun(nilai)
prosesGambar(lokasiGambar)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
