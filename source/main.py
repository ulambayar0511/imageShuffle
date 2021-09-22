from PIL import Image
import numpy as np


image1 = Image.open("images/test.jpg")
# image1.show()
image2 = Image.open("images/image.jpg")
# image2.show()
# resize, first image
image1 = image1.resize((426, 240))
image1_size = image1.size
image2_size = image2.size
new_image = Image.new("RGB", (2 * image1_size[0], image1_size[1]), (250, 250, 250))
new_image.paste(image1, (0, 0))
new_image.paste(image2, (image1_size[0], 0))
new_image.save("images/merged_image.jpg", "JPEG")
new_image.show()
# angle = 40
# r_img = img.rotate(angle)
# Resizing an image using resize()
# size = (600, 600)
# r_img = img.resize(size)
# r_img.show()
# im1 = img.split(r_img)
# im1 = Image.Image.split(img)
# im1[0].show()


# a = np.asarray(r_img)
# print(a)
#   Saving an image using save()
# print(img.mode)
# print(img.size)
# (left, upper, right, lower) = (20, 20, 100, 100)

#     # Here the image "im" is cropped and assigned to new variable im_crop
#     im_crop = im.crop((left, upper, right, lower))
# img.show()
