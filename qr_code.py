import qrcode as qr
img = qr.make("https://www.linkedin.com/in/rohini-chavhan/")
img.save("linkdin.png")