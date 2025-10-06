import qrcode

def QRcreate():
    path = input("Enter link to create QR Code : ")
    img = qrcode.make(path)
    imgName = input("Enter save file name : ")
    try:
        img.save(imgName+'.jpg')
        print(f"QR Code saved as {imgName+'.jpg'}")
    except Exception as e:
        print(f"Failed to save QR Code: {e}")
def QRread():
    import cv2
    d = cv2.QRCodeDetector()
    path = input("Enter path to QR Code: ")
    val, _, _ = d.detectAndDecode(cv2.imread(path))
    return val

if __name__ == '__main__':
    method = input("Enter your method - Create(C) or Read(R) : ")
    if method.upper() == "R":
        value = QRread()
        print(value)

    elif method.upper() == "C":
        QRcreate()
        print("QR Code generated")

    else:
        print("Enter a valid command!")
