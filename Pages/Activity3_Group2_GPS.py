import numpy as np
import cv2
import matplotlib.pyplot as plt

choice = []

fig = plt.figure(figsize=(10, 7))
rows = 2
columns = 2
img_ = cv2.imread("verdant_moonlight__commissioned__by_bisbiswas_degzd3v.jpg")
img_2 = cv2.imread("emerald_moon_by_bisbiswas_demugqf.jpg")
img_3 = cv2.imread("a_pink_sunset_by_bisbiswas_dehui96.jpg")
img_4 = cv2.imread("aurora_lights_by_bisbiswas_dedov93.jpg")
img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)

dimension = img_.shape
height = 1920
width = 1080

def translation(height, width):
 m_translation_ = np.float32([[1, 0, 100], [0, 1, 50], [ 0, 0, 1]])
 translated_img_ = cv2.warpPerspective(img_, m_translation_, (height, width))
 plt.title(label = "Translation", fontsize = 16)
 plt.axis('off')
 fig.add_subplot(rows, columns, 1)
 plt.imshow(translated_img_)
 plt.axis('off')
 translated_img_2 = cv2.warpPerspective(img_2, m_translation_, (height, width))
 fig.add_subplot(rows, columns, 2)
 plt.imshow(translated_img_2)
 plt.axis('off')
 translated_img_3 = cv2.warpPerspective(img_3, m_translation_, (height, width))
 fig.add_subplot(rows, columns, 3)
 plt.imshow(translated_img_3)
 plt.axis('off')
 translated_img_4 = cv2.warpPerspective(img_4, m_translation_, (height, width))
 fig.add_subplot(rows, columns, 4)
 plt.imshow(translated_img_4)
 plt.axis('off')
 plt.show()

def Rotate(Rotate):
 plt.title(label = "Rotation", fontsize = 16)
 plt.axis('off')
 rotated_img_ = cv2.rotate(img_, cv2.ROTATE_180)
 fig.add_subplot(rows, columns, 1)
 plt.axis('off')
 plt.imshow(rotated_img_)
 rotated_img_2 = cv2.rotate(img_2, cv2.ROTATE_90_CLOCKWISE)
 fig.add_subplot(rows, columns, 2)
 plt.axis('off')
 plt.imshow(rotated_img_2)
 rotated_img_3 = cv2.rotate(img_3, cv2.ROTATE_90_COUNTERCLOCKWISE)
 fig.add_subplot(rows, columns, 3)
 plt.axis('off') 
 plt.imshow(rotated_img_3)
 fig.add_subplot(rows, columns, 4)
 plt.axis('off')
 plt.imshow(img_)
 plt.show()
 

def Scale():
 x = int(input("Width (1 - 1920):"))
 y = int (input("Height(1 - 1080):"))
 d_size = (x, y)

 plt.title(label = "Scaling", fontsize = 16)
 plt.axis('off')

 R_image_ = cv2.resize(img_, d_size, interpolation = cv2.INTER_AREA)
 fig.add_subplot(rows, columns, 1)
 plt.axis('off')
 plt.imshow(R_image_)
 R_image_2 = cv2.resize(img_2, d_size, interpolation = cv2.INTER_AREA)
 fig.add_subplot(rows, columns, 2)
 plt.axis('off')
 plt.imshow(R_image_2)
 R_image_3 = cv2.resize(img_3, d_size, interpolation = cv2.INTER_AREA)
 fig.add_subplot(rows, columns, 3)
 plt.axis('off')
 plt.imshow(R_image_3)
 R_image_4 = cv2.resize(img_4, d_size, interpolation = cv2.INTER_AREA)
 fig.add_subplot(rows, columns, 4)
 plt.axis('off')
 plt.imshow(R_image_4)
 plt.show()

def Shear():
 plt.title(label = "Shearing", fontsize = 16)
 plt.axis('off')
 m_shearing_x = np.float32([[1, 0.5, 0], [0, 1, 0], [ 0, 0, 1]])
 m_shearing_y = np.float32([[1, 0, 0], [0.5, 1, 0], [ 0, 0, 1]])
 sheared_img_x = cv2.warpPerspective(img_, m_shearing_x, (img_.shape[1],img_.shape[0]))
 sheared_img_y = cv2.warpPerspective(img_, m_shearing_y, (img_.shape[1],img_.shape[0]))
 fig.add_subplot(rows, columns, 1)
 plt.axis('off')
 plt.imshow(sheared_img_x)
 plt.imshow(sheared_img_y)
 sheared_img_x = cv2.warpPerspective(img_2, m_shearing_x, (img_.shape[1],img_.shape[0]))
 sheared_img_y = cv2.warpPerspective(img_2, m_shearing_y, (img_.shape[1],img_.shape[0]))
 fig.add_subplot(rows, columns, 2)
 plt.axis('off')
 plt.imshow(sheared_img_x)
 plt.imshow(sheared_img_y)
 sheared_img_x = cv2.warpPerspective(img_3, m_shearing_x, (img_.shape[1],img_.shape[0]))
 sheared_img_y = cv2.warpPerspective(img_3, m_shearing_y, (img_.shape[1],img_.shape[0]))
 fig.add_subplot(rows, columns, 3)
 plt.axis('off')
 plt.imshow(sheared_img_x)
 plt.imshow(sheared_img_y)
 sheared_img_x = cv2.warpPerspective(img_4, m_shearing_x, (img_.shape[1],img_.shape[0]))
 sheared_img_y = cv2.warpPerspective(img_4, m_shearing_y, (img_.shape[1],img_.shape[0]))
 fig.add_subplot(rows, columns, 4)
 plt.axis('off')
 plt.imshow(sheared_img_x)
 plt.imshow(sheared_img_y)
 plt.show()

def Reflect():
   plt.title(label = "Reflection", fontsize = 16)
   plt.axis('off')
   m_reflection_ = np.float32([[1, 0, 0], [0, -1, width], [0, 0, 1]])
   reflected_img_ = cv2.warpPerspective(img_,m_reflection_,(int(height), int(width)))
   fig.add_subplot(rows, columns, 1)
   plt.axis('off')
   plt.imshow(reflected_img_)
   reflected_img_2 = cv2.warpPerspective(img_2,m_reflection_,(int(height), int(width)))
   fig.add_subplot(rows, columns, 2)
   plt.axis('off')
   plt.imshow(reflected_img_2)
   reflected_img_3 = cv2.warpPerspective(img_3,m_reflection_,(int(height), int(width)))
   fig.add_subplot(rows, columns, 3)
   plt.axis('off')
   plt.imshow(reflected_img_3)
   reflected_img_4 = cv2.warpPerspective(img_4,m_reflection_,(int(height), int(width)))
   fig.add_subplot(rows, columns, 4)
   plt.axis('off')
   plt.imshow(reflected_img_4)
   plt.show()


def main():
 choice = int(input("Choice:"))
 
 if choice == 1:
     translation(height, width)
 if choice == 2:
    Rotate(Rotate)
 if choice == 3:
    Scale()
 if choice == 4:
      Shear()
 if choice == 5:
    Reflect()

if __name__ == '__main__':
 main()

