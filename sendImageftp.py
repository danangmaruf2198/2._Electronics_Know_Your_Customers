import pysftp as sftp
def sftpExample():
    try:
        s=sftp.Connection(host='danangmaruf.esy.es', username='u788641612_sopir', password='12345678')
        receiver= '/public_html/ekycWeb/example.jpg'
        transmiter='/home/pi/Desktop/a.jpg'
        s.put(transmiter,receiver)
        s.close()
    except Exception, e:
        print str(e)

sftpExample()
