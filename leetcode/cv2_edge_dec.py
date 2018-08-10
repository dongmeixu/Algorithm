# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# image = cv2.imread("F:\\31.jpg")
# edges = cv2.Canny(image, 100, 200)
# plt.subplot(1, 2, 1), plt.imshow(image)
# plt.title('original'), plt.xticks([]), plt.yticks([])
# plt.subplot(1, 2, 2), plt.imshow(edges)
# plt.title('edge image'), plt.xticks([]), plt.yticks([])
# plt.show()


import cv2
def rotate(x, angle):
    """cv2.getRotationMatrix2D函数获得变换矩阵。
        第一参数指定旋转圆点；
        第二个参数指定旋转角度；
        第二个参数指定缩放比例。
    """
    img_h, img_w = image.shape[:2]
    print(img_h)
    M_rotate = cv2.getRotationMatrix2D((img_w / 2, img_h / 2), angle, 1)
    """cv2.warpAffine()的第三个参数是输出图像的大小。
       第二个参数是变换矩阵，对于平移变换，
       变换矩阵M如下：M = [[1, 0, tx], [0, 1, ty]]
       tx为x得偏移量，ty是y轴得偏移量，单位像素。
    """
    xb = cv2.warpAffine(x, M_rotate, (img_w, img_h))
    return xb


image = cv2.imread("F:\\49999_image.tif")
cv2.imshow("image", image)
print(image.shape)

cv2.imshow("rotate", rotate(image, 90))

# image_1 = cv2.resize(image, None,fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# cv2.imshow("image_1", image)
#
# height, width = image.shape[:2]
# image_2 = cv2.resize(image, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
# cv2.imshow("image_2", image)
cv2.waitKey(0)


