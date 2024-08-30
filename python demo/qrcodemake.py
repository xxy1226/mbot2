import qrcode     #调用qrcode库
# img = qrcode.make('一起在mCode上学Python吧！')   #填写二维码的内容
img = qrcode.make("上学")
img.save("text.png")   #生成本地文件