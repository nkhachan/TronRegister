import qrcode
from User import user

def createQR():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(user.address)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.show()
    img.save("img.png", "PNG")
    return img