import app
from PIL import Image

height, width = 600, 600
if __name__ == "__main__":
    with Image.open("images/test.jpg") as img:
        img = img.resize((height, width))
        imgs = app.cropImg(img, 4)
        imgs = app.rotateImg(imgs)

        counter = 1
        for i in range(len(imgs)):
            images = app.cropImg(imgs[i], 4)
            images = app.rotateImg(images)
            imgs[i] = app.mergeImg(images, imgs[i].size)
            imgs[i].save("images/{}.jpg".format(counter))
            counter += 1
        img = app.mergeImg(imgs, img.size)
        img.save("images/16.jpg")
