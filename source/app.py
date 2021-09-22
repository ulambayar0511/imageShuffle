from PIL import Image
from random import randint

height, width = 600, 600
rot = [0, 90, 180, 270]


def mergeImg(arr):
    merge_img = Image.new("RGB", (height, width))
    merge_img.paste(arr[0], (0, 0))
    merge_img.paste(arr[2], (arr[2].width, 0))
    merge_img.paste(arr[1], (0, arr[1].width))
    merge_img.paste(arr[3], (arr[3].width, arr[3].width))
    merge_img.show()


def rotateImg(imgs):
    result = []
    for i in imgs:
        result.append(i.rotate(rot[randint(0, 3)]))
    mergeImg(result)


def cropImg(img, count):
    img = img.resize((height, width))
    images = []
    # 1
    left = 0
    top = 0
    right = width / 2
    bottom = height / 2
    img1 = img.crop((left, top, right, bottom))
    img1.save("1.jpg")
    # 2
    left = width / 2
    top = 0
    right = width
    bottom = height / 2
    img2 = img.crop((left, top, right, bottom))

    img2.save("2.jpg")
    # 3
    left = 0
    top = height / 2
    right = width / 2
    bottom = height
    img3 = img.crop((left, top, right, bottom))
    img3.save("3.jpg")
    # 4
    left = width / 2
    top = height / 2
    right = width
    bottom = height
    img4 = img.crop((left, top, right, bottom))
    img4.save("4.jpg")
    images.append(img1)
    images.append(img2)
    images.append(img3)
    images.append(img4)
    rotateImg(images)

    # for i in range(count):

    # img_crop.show()


with Image.open("images/test.jpg") as img:

    # img.show()
    cropImg(img, 4)
