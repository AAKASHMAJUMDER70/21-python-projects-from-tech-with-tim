import qrcode

qrcode_generated = qrcode.QRCode(
    version = 5,
    error_correction =qrcode.constants.ERROR_CORRECT_L,
    box_size = 23,
    border = 1
    )
qrcode_generated.add_data("https://pypi.org/project/qrcode/")
qrcode_generated.make(fit=True)
img = qrcode_generated.make_image(fill_color="black", back_color="white")
img.save("png2.png")