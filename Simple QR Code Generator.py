import qrcode

data = input("Enter text/link: ")

qr = qrcode.make(data)
qr.save("myqrcode.png")

print("QR Code Generated ✅")
