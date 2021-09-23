import app
from PIL import Image

height, width = 600, 600
if __name__ == "__main__":
    with Image.open("images/test.jpg") as img:
        img = img.resize((height, width))
        imgs = app.cropImg(img, 4)
        imgs = app.rotateImg(imgs)
        img = app.mergeImg(imgs, img.size)

        counter = 1
        for i in imgs:
            images = app.cropImg(i, 4)
            images = app.rotateImg(images)
            i = app.mergeImg(images, i.size)
            i.save("images/{}.jpg".format(counter))
            counter += 1
