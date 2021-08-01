## pip install qrcode
## pip install pillow

import qrcode

my_var = qrcode.make("https://www.andromarket.io")
my_var.save("x.png")

