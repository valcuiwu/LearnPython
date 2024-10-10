# -*- coding:utf-8 -*-
import os
import qrcode
from PIL import Image

# 创建QRCode对象
ewm = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# 设置二维码数据，这里为校园场所码编码方案
data = "场所码: 教学楼, 包含: 自习室, 实验室"
ewm.add_data(data=data)

# 更改二维码的颜色，默认是黑色。得到的结果是 PIL 图像对象
ewm.make(fit=True)  # 让二维码得到一个适合的大小值。
ewm_img = ewm.make_image(fill_color="#ff3300", back_color="white")

# 获取二维码大小:宽，高
ewm_size = ewm_img.size
ewm_size_w, ewm_size_h = ewm_size

# 打开图标文件，并获取图标的大小，重新设定图标大小
s = 6
icon = Image.open("neiqian.png")

# 设置小图标的大小
icon_w, icon_h = int(ewm_size_w / s), int(ewm_size_h / s)
icon_small = icon.resize((icon_w, icon_h), Image.ANTIALIAS)  # Image.ANTIALIAS 画面平滑缩放

# 获取粘贴小图标的坐标
icon_x, icon_y = int((ewm_size_w - icon_w) / 2), int((ewm_size_h - icon_h) / 2)

# 把图标“粘贴”到二维码上正中间
ewm_img.paste(icon_small, (icon_x, icon_y))

# 显示二维码
ewm_img.show()  # 如果数据被clear了，会有个二维码，扫它什么都不会发生
ewm_img.save("campus_code.jpg")
