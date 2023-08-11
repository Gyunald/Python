import qrcode
# from PIL import Image

date = 'WIFI:S:KT_GiGA_5G_6A78;T:WPA;P:woon123456789;H:false'

# QR 코드 생성
qr_code = qrcode.make(date)

# # 생성된 QR 코드를 이미지로 저장
# qr_code.save("qr_code.png")

# 이미지로 생성된 QR 코드를 화면에 표시
qr_code.show()
