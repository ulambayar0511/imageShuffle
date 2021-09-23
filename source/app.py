from PIL import Image
import random


rot = [0, 90, 180, 270]


def mergeImg(arr, size):

    merge_img = Image.new("RGB", size)
    choice_number = [0, 1, 2, 3]

    number = random.choice(choice_number)
    choice_number.remove(number)
    merge_img.paste(arr[number], (0, 0))

    number = random.choice(choice_number)
    choice_number.remove(number)
    merge_img.paste(arr[number], (arr[number].width, 0))

    number = random.choice(choice_number)
    choice_number.remove(number)
    merge_img.paste(arr[number], (0, arr[number].width))

    number = random.choice(choice_number)
    choice_number.remove(number)
    merge_img.paste(arr[number], (arr[number].width, arr[number].width))
    return merge_img


def rotateImg(imgs):
    result = []
    for i in imgs:
        result.append(i.rotate(rot[random.randint(0, 3)]))
    return result


def cropImg(img):
    images = []
    height, width = img.size
    # 1
    left = 0
    top = 0
    right = width / 2
    bottom = height / 2
    img1 = img.crop((left, top, right, bottom))
    # 2
    left = width / 2
    top = 0
    right = width
    bottom = height / 2
    img2 = img.crop((left, top, right, bottom))

    # 3
    left = 0
    top = height / 2
    right = width / 2
    bottom = height
    img3 = img.crop((left, top, right, bottom))
    # 4
    left = width / 2
    top = height / 2
    right = width
    bottom = height
    img4 = img.crop((left, top, right, bottom))
    images.append(img1)
    images.append(img2)
    images.append(img3)
    images.append(img4)
    return images
