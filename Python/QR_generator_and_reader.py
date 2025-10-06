import qrcode
import cv2

def QRcreate():
    path = input("Enter link to create QR Code : ")
    img = qrcode.make(path)
    imgName = input("Enter save file name : ")
    img.save(imgName+'.jpg')

def QRread():
    d = cv2.QRCodeDetector()
    path = input("Enter path to QR Code: ")
    img = cv2.imread(path)
    if img is None:
        print("Error: File not found or invalid image format.")
        return None
    val, _, _ = d.detectAndDecode(img)
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
