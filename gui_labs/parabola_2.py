from math import*
from tkinter import*

root = Tk()
root.title('Кульчицький Олег')
root.geometry('500x520')

label=Label(root, text='Побудова графіку', font='Arial 14 bold', bg='yellow')
label.pack(fill=X)

canvas = Canvas(root, height=460, width = 500, bg='#F5DEB3')
canvas.pack()

x0, y0 = 200, 300
x1 =50; x2 = 350; dx=10

canvas.create_line(0, y0,430, y0, fill = 'green', arrow = LAST)
canvas.create_line(x0, 110,x0, 450, fill = 'green', arrow = FIRST)


canvas.create_text(209,310, text='10')
canvas.create_text(300,310, text='100')
canvas.create_text(210,200, text='100')
canvas.create_text(x0+5,110, text='y', anchor=W)
canvas.create_text(425,300, text='x', anchor = NW)

canvas.create_rectangle([198,298],[203,303],width=0, fill='orange') 

p = 50
while p<=350:
    canvas.create_line(p, 295,p, 305, fill = 'green')
    canvas.create_line(195, p+100, 205, p+100, fill = 'green')
    p+=10
##----------------------------------------------------------##
points=[]
for x in range(x1+30,x2+dx+30,dx):
    y = y0-(x-x0-30)**2/100
    z = (x,y)
    points.append(z)
##----------------------------------------------------------##
points_1=[]
for x in range(x1+30,x2+30+dx,dx):
    y= y0-(abs(x-x0-30))
    z = (x,y)
    points_1.append(z)
##----------------------------------------------------------##
print(points)
print(len(points))
canvas.create_line(points, fill='blue', smooth=1, width=2)
##----------------------------------------------------------##
print(points_1)
print(len(points_1))
canvas.create_line(points_1, fill='red', smooth=1, width=2)
##----------------------------------------------------------##
button = Button(root, text='Close', command = quit)
button.pack()
