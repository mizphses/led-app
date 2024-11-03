from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont
from time import sleep

# LEDマトリックスの設定
options = RGBMatrixOptions()
options.rows = 32
options.cols = 128
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'  # または 'adafruit-hat' など
options.gpio_slowdown = 4
options.disable_hardware_pulsing = True

matrix = RGBMatrix(options=options)

# 日本語フォントの読み込み
font_path = "./fonts/NotoSansCJKjp-Regular.otf"
font1 = ImageFont.truetype(font_path, 8)
font2 = ImageFont.truetype(font_path, 14)

import sys
# 表示する日本語の文章
text = sys.argv[1]
text2 = sys.argv[2]

# テキストを描画するための画像を作成
image = Image.new("RGB", (128, 32))
draw = ImageDraw.Draw(image)
draw.text((0, 0), text, font=font1, fill=(255,255,255))
draw.text((0, 10), text2, font=font2, fill=(255,255,255))

# 画像をLEDマトリックスに表示
matrix.SetImage(image.convert('RGB'))

sleep(1000)