# 画像をNumPy配列形式に変換

from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

classes = ["monkey","boar","crow"]
num_classes = len(classes)
image_size = 50
num_testdata = 100

# 画像の読み込み

x_train = []
x_test = []
y_train = []
y_test = []

for index, classlabel in enumerate(classes):
    photos_dir = "image/" + classlabel
    files = glob.glob(photos_dir + "/*.jpg")
    for i, file in enumerate(files):
        if i >= 200: break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)

        if i < num_testdata:
            x_test.append(data)
            y_test.append(index)
        else:
            for angle in range(-20, 20, 5):
                #回転
                img_r = image.rotate(angle)
                data = np.asarray(img_r)
                x_train.append(data)
                y_train.append(index)

                #反転
                img_trans = image.transpose(Image.FLIP_LEFT_RIGHT)
                data = np.asarray(img_trans)
                x_train.append(data)
                y_train.append(index)

x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

xy = (x_train, x_test, y_train, y_test)
np.save("./animal_aug.npy", xy)