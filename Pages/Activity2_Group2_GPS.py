import numpy as np
import matplotlib.pyplot as plt

two_d_arr = np.array([[1,0,1], [0,1,0],[1,0,1]])

x = []
y =[]
c = []

def change(x,y,color):
 
 for i in range(len(two_d_arr)):
    for j in range(len(two_d_arr[i])):
        two_d_arr[x][y] = color

 img = plt.imshow(two_d_arr, interpolation = 'none', cmap = 'Pastel2')
 img.set_clim([0,50])
 plt.colorbar()
 plt.show()

def main():
 x_val = int(input("X coords:"))
 y_val = int(input("Y coords:"))
 c_val = int(input("Color Value (1-50)"))

 change (x_val, y_val, c_val)

if __name__ == '__main__':
 main()