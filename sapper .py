from tkinter import *               
from random import shuffle          
column = 7                         
row = 7                             
btn = []
playground = [1,0,0,0,0] * (row*column//5+1)      
shuffle(playground)

def play(n):                      
    m = 0
    for i in [n-column, n, n+column]:
        for j in [-1, 0, 1]:
            if (i+j >= 0 and i+j < row*column
                and i//column == (i+j)//column):
                m += playground[i+j]
    if playground[n] == 1:
        btn[n].config(text='M', bg='#f88', activebackground='#f66')
    elif m == 0:
        btn[n].config(text=0, fg='#afa', bg='#afa', activebackground='#7f7')
    else :
        btn[n].config(text=m, bg='#ccc', activebackground='#aaa')

def marker(n):
    if btn[n].cget('text') == '':
        btn[n].config(text='F', bg='#ffa', activebackground='#ff7')
    elif btn[n].cget('text') == 'F':
        btn[n].config(text='', bg='#ccc', activebackground='#aaa')

for i in range(row):
    f = Frame()                     
    f.pack(expand=YES, fill=BOTH)   
    for j in range(column):
        n = i * column + j
        btn += [Button(f)]
        btn[n].pack(expand=YES, fill=BOTH, side=LEFT)
        btn[n].config(width=3, height=2)
        btn[n].config(bg='#ccc', activebackground='#aaa')
        btn[n].config(command=lambda n=n: play(n))
        btn[n].bind('<Button-3>', lambda event, n=n: marker(n))

mainloop()                         
