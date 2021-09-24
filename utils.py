import os

import cv2
import io
import numpy as np
import matplotlib.pyplot as plt


def get_img_from_fig(fig, dpi=180):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi)
    buf.seek(0)
    img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    buf.close()

    img = cv2.imdecode(img_arr, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

# x = os.listdir(r'E:\Dataset\D3')
# y = [len(os.listdir(r'E:\Dataset\D3' + '/' + i)) for i in x]
#
# indices = np.argsort(np.array(y))
# x = np.array(x)[indices[::-1]]
# y = np.array(y)[indices[::-1]]
#
# fig, ax = plt.subplots()
# ax.bar([i+1 for i in range(len(x))], y, width=0.5)
# plt.xticks([i+1 for i in range(len(x))], x, rotation=90)
# plt.title('D3')
# plt.tight_layout()
#
# # plt.show()
# plt.savefig('1.jpg')
# from lib.gradCam import *
# img_path = './imgs/2010_Unit164_Ivan076_img0294.jpg'
# model_path = ''
# model_name = 'resnet50'
# select_t_layer = False
# class_index = None
# grad_cam = GradCAM(img_path, model_name, model_path, select_t_layer, class_index)
# heat_map = grad_cam()
# cv2.imshow('0', heat_map)
# cv2.waitKey(0)



