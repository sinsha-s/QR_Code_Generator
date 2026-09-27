import qrcode
data = "https://www.linkedin.com/in/sinsha-sree-9099b2331"

img = qrcode.make(data)
img.save("linkedin_qrcode.png")
print("QR code generated successfully")
