from PIL import Image

images = []
WIDTH = 33
L = 24
new_im = Image.new('RGB', (L * WIDTH, L * WIDTH), (250,250,250))
for i in range(0, L):
    for j in range(0, L):
        imagePath = 'output/' + str(i * L + j +1) + '.png'
        print(imagePath)
        img_current = Image.open(imagePath)
        # img_current.show()
        new_im.paste(img_current, (j * WIDTH, i * WIDTH))
new_im.save("merged_images.png", "PNG")
new_im.show()