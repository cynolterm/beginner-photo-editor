from tkinter import *

#implementing methods for functionality

#main 

def open_editor():
    btn_open.pack_forget()

    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open...')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=root.quit)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')
    mainloop()



root = Tk()
root.geometry('800x600')
root.title('Photo editor for beginners')
btn_open = Button(root, text='Open', width=25, command=open_editor)
btn_open.pack()
mainloop()