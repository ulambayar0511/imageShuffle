import app
import os
from PIL import Image

height, width = 600, 600
if __name__ == "__main__":
    arr = os.listdir("images/")
    for j in arr:
        with Image.open("images/{}".format(j)) as img:
            img = img.resize((height, width))
            imgs = app.cropImg(img)
            imgs = app.rotateImg(imgs)

            for i in range(len(imgs)):
                images = app.cropImg(imgs[i])
                images = app.rotateImg(images)

                for k in range(len(images)):
                    ims = app.cropImg(images[k])
                    ims = app.rotateImg(ims)
                    images[k] = app.mergeImg(ims, images[k].size)
                imgs[i] = app.mergeImg(images, imgs[i].size)
            img = app.mergeImg(imgs, img.size)
            img.save("shuffleImg/{}".format(j))
