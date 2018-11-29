from math import*
from tkinter import*
from random import*
root = Tk()
root.title('Метод Монте-Карло')
root.geometry('600x650')

label=Label(root, text='Графік квдрата та кола', font='Arial 15')
label.pack(fill=X)

label1=Label(root,  font='Arial 15')
label1.pack(fill=X)

label2=Label(root,  font='Arial 15')
label2.pack(fill=X)

label3=Label(root, font='Arial 15')
label3.pack(fill=X)

canvas=Canvas(root, height=400, width = 400, bg='#F5DEB3')
canvas.pack()

canvas.create_rectangle(90,90,290,290, outline = 'blue')
canvas.create_oval(90,90,290,290, outline='red')
p=0

def circle():
    canvas.create_rectangle(80,80,300,300,  fill = '#F5DEB3',outline = '#F5DEB3')
    canvas.create_rectangle(90,90,290,290, outline = 'blue')
    canvas.create_oval(90,90,290,290, outline='red')

    n=int(ent.get())
    ind=0
    for i in range(1,n+1):
        x=uniform(90,290)
        y=uniform(90,290)
        if sqrt(pow(x-190,2)+pow(y-190,2))<100:
                canvas.create_oval(x-2,y-2,x+2,y+2,fill='green')
                ind+=1
        else:
                canvas.create_oval(x-2,y-2,x+2,y+2,fill='red')
    ind2=ind/1000
    res = ind2*200*200
    
    result1 = 'Кількість точок в колі:{}'.format(ind)
    label1.configure(text =  result1)
    
    result2 = 'Наближена площа кола:{}'.format(res)
    label2.configure(text =  result2)
    
    result3 = 'Точна площа кола:{}'.format(pi*10000)
    label3.configure(text =  result3)

Label(root,text='Введіть к-сть точок n:').pack()
ent = Entry()
ent.config(fg = "black", font = 'Arial 10')
ent.insert(0, '')
ent.bind('<Return>', circle)
ent.pack(side = TOP)
button = Button(root, text='Розрахувати', command = circle)        
button.pack(side=TOP)
button_exit= Button(root, text='Закрити', command = root.destroy)
button_exit.pack()

root.mainloop()
