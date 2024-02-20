import qrcode

create_qrcode = qrcode.make("https://pypi.org/project/qrcode/")
print(type(create_qrcode))
create_qrcode.save("png1.png")