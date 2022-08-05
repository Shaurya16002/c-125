import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from PIL import Image
import PIL.ImageOps

x,y = fetch_openml('mnist_784',version = 1,return_X_y= True)
xTrain,xTest,yTrain,yTest = train_test_split(x,y,train_size=7500,test_size=2500)
xTrainScale = xTrain/255.0
xTestScale = xTest/255.0
model = LogisticRegression(solver = 'saga', multi_class='multinomial').fit(xTrainScale,yTrain)

def getPrediction(img):
    im_pil = Image.open(img)
    image_bw = im_pil.convert('L')
    image_bw_resized = image_bw.resize((28,28), Image.ANTIALIAS)

    pixel_filter = 20
    min_pixel = np.percentile(image_bw_resized, pixel_filter)
    image_bw_resized_inverted_scaled = np.clip(image_bw_resized-min_pixel, 0, 255)
    max_pixel = np.max(image_bw_resized)
    image_bw_resized_inverted_scaled = np.asarray(image_bw_resized_inverted_scaled)/max_pixel
    test_sample = np.array(image_bw_resized_inverted_scaled).reshape(1,784)
    test_pred = model.predict(test_sample)
    return test_pred[0]
