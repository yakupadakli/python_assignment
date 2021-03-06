__author__ = 'yakupadakli'
# -*- coding: utf-8 -*-

import sys
from PIL import Image

image_name=sys.argv[1:]
print image_name[0]
image = Image.open(image_name[0])
SHREDS = 20
shredded = Image.new("RGBA", image.size)
width, height = image.size
shred_width = width / SHREDS
sequence = range(0, SHREDS)

new_pic = Image.new('RGBA', image.size)

# get pixel value
def get_pixel_value(x, y):
    pixel = data[x, y]
    return pixel


img_list1 = []
img_list2 = []
region_list = []
# taking image shreds to the list
for i, shred_index in enumerate(sequence):
    shred_x1, shred_y1 = shred_width * shred_index, 0
    shred_x2, shred_y2 = shred_x1 + shred_width, height
    region = image.crop((shred_x1, shred_y1, shred_x2, shred_y2))
    # image part list
    region_list.append(region)


# compare function to one part of
# the image to the other image
def compare(start, finish, direction):
    """
    First we take a

    :param start:
    :param finish:
    :param direction:
    :return:
    """
    global data
    # start form right part of the
    # image compare with the other image`s left part
    if direction == "right":
        x1 = region_list[start].size[0] - 1
        x2 = 0
    # start form left part of the
    # image compare with the other image`s right part
    elif direction == "left":
        x1 = 0
        x2 = region_list[start].size[0] - 1
    r = g = b = 0
    # comparing last pixel of the first image
    # with the first pixel of the other images
    # last x pixel are taking but also all
    # pixel in the y direction are
    for i in range(0, height):
        data = region_list[start].load()
        pixel1 = get_pixel_value(x1, i)
        data = region_list[finish].load()
        pixel2 = get_pixel_value(x2, i)
        r += abs(pixel1[0] - pixel2[0])
        g += abs(pixel1[1] - pixel2[1])
        b += abs(pixel1[2] - pixel2[2])
    return (r + g + b) / 3

# sending all part of the image
for i in range(SHREDS):
    for j in range(SHREDS):
        a = compare(i, j, "right")
        b = compare(i, j, "left")
        temp = i, j, a
        img_list1.append(temp)
        temp1 = i, j, b
        img_list2.append(temp1)

degerler = []
degerler1 = []
index = 0
index1 = 20
index2 = 20


def find_sequence(start, finish, liste):
    """
        Finding the sequence of image
        with compare the value of the lists.
        The minimum number gives us a best match
    :param start:
    :param finish:
    :param liste:
    :return:
    """
    global temp, index, degerler, index, index1, index2
    temp = []
    temp2 = []
    for i in range(start, finish):
        temp.append(img_list1[i])
        temp2.append(img_list2[i])
    ilk = temp[0][2]
    ilk2 = temp2[0][2]
    test = []
    for i in range(SHREDS):
        if ilk >= temp[i][2] and temp[i][0] != temp[i][1]:
            ilk = temp[i][2]
            index1 = temp[i][1]
            test.append(index1)
        if ilk2 >= temp2[i][2] and temp2[i][0] != temp2[i][1]:
            ilk2 = temp2[i][2]
            index2 = temp2[i][1]
    if liste == 1:
        degerler.append(ilk)
        return index1
    elif liste == 2:
        degerler1.append(ilk2)
        return index2

sira1 = []
sira2 = []
# find sequence from left and right
# sides and appending them to the list
for i in range(0, img_list1.__len__(), SHREDS):
    sira1.append(find_sequence(i, i + SHREDS, 1))
    sira2.append(find_sequence(i, i + SHREDS, 2))


a = []
# finding start part of the image by looking the
# big number of the difference between
# left side comparison and right side comparison
for i in range(SHREDS):
    a.append(abs(degerler1[i] - degerler[i]))
en_buyuk = a[0]
for i in range(SHREDS):
    if en_buyuk < a[i]:
        en_buyuk = a[i]
        deger_index = i

# listing my dump list the right form
# first list indexes shows me the image
# after the coming from it. Ex: index 1 has number 3
# which means image 3 comes after the image 1
yeni_sira = []
a = sira1[deger_index]
yeni_sira.append(a)
for i in range(1, SHREDS):
    yeni_sira.append(sira1[a])
    a = sira1[a]

# pasting new image with right order and saving
for i in range(SHREDS):
    new_pic.paste(region_list[yeni_sira[i]], (shred_width * i, 0))

new_pic.save("new_pic.png")
