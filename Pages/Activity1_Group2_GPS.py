import matplotlib.pyplot as plt
import streamlit as st

def DDALINE(x1, y1, x2, y2, color):
    dx = x2 - x1 
    dy = y2 - y1
    x3 = (x1 + x2) / 2
    y3 = (y1 + y2) / 2

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)


    Xcoordinate = float(dx / steps)
    Ycoordinate = float(dy / steps)

    for i in range(0, int (steps +1)):
        plt.plot(int(x1), int(y1), color)
        x1 += Xcoordinate
        y1 += Ycoordinate   
    
    plt.plot(x3,y3,marker="o",markersize=5,markerfacecolor="blue")
    st.pyplot()

def bresenham(x1, y1, x2, y2, color): 
   
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x3 = (x1 + x2) / 2
    y3 = (y1 + y2) / 2

    gradient = dy/float(dx)
    
    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2 ,y2 = y2, x2

    p = 2 * dy - dx
    
    xcords = [x]
    ycords =[y]
   
    for k in range(2,dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else :
            p = p + 2 * dy
        
        x = x + 1 if x < x2 else x - 1
        
        xcords.append(x)
        ycords.append(y)

    plt.plot(xcords,ycords)
    plt.plot(x3,y3,marker="o",markersize=5,markerfacecolor="red")
    st.pyplot()

def midpoint(x1, y1, x2, y2, color): 
   
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x3 = (x1 + x2) / 2
    y3 = (y1 + y2) / 2

    gradient = dy/float(dx)
    
    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2 ,y2 = y2, x2

    p = 2 * dy - dx
    
    xcords = [x]
    ycords =[y]
   
    for k in range(2,dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else :
            p = p + 2 * dy
        
        x = x + 1 if x < x2 else x - 1
        
        xcords.append(x)
        ycords.append(y)

    st.write("Midpoint of the line is:", x3)
    plt.plot(x3,y3,marker="o",markersize=5,markerfacecolor="blue")
    plt.show() 

def main():
    x = int(input("Enter X1: "))
    y = int(input("Enter Y1: "))
    xEnd = int(input("Enter X2: "))
    yEnd = int(input("Enter Y2: "))
    color = "r."
    DDALINE(x,y,xEnd,yEnd,color)
    bresenham(x,y,xEnd, yEnd, color)
    midpoint(x,y,xEnd,yEnd,color)

if __name__ == '__main__':
    main()
