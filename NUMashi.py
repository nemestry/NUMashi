import RTKashi
import SETashi
import DETashi
import cv2
import numpy as np

SETashi.DETashiModelPath = "custom/NUMashi.pb"

config = SETashi.SETashi()

ia = RTKashi.RTKashi(config)

img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")

ia.process([img1,img2])

ia.draw_symbols([img1, img2], ["img1_det.jpg", "img2_det.jpg"])

res = ia.get_numbers()[0]
print('Номер', res[0][0])
print('Уверенность', res[0][1])
