# -*- coding: utf-8 -*-
"""Feynn

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kmKpzJcKsEqKKhoDDJC9i0uSA4r32KvF
"""

from google.colab import drive
drive.mount('/content/MyDrive/')

import pandas as pd
df = pd.read_csv("/content/MyDrive/MyDrive/feynn/archive 2/wood.csv")

df.head()

from PIL import Image

im = Image.open("/content/MyDrive/MyDrive/feynn/archive 2/images/images/abura-s-60x60.jpg")
im

im = Image.open("/content/MyDrive/MyDrive/feynn/archive 2/images/images/african-mahogany-60x60.jpg")
im

im = Image.open("/content/MyDrive/MyDrive/feynn/archive 2/images/images/american-beech1-60x60.jpg")
im

df.info

