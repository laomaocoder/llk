from PIL import Image


for i in range(1, 9):
    # 打开原始图片
    image = Image.open(f'animal_{i}.png')
    # 调整尺寸为50x50
    image = image.resize((50, 50))
    # 保存处理后的图片
    image.save(f'animal_{i}.png')