from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

#implementing methods for functionality

def browse_file():
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')]  
    root.update()
    file_name = filedialog.askopenfilename(initialdir = "/home/ad.adasworks.com/reka.szabo/", title = "Select a File", filetypes = f_types, multiple=False)
    print(file_name)

def calc_img_size(img):
    #return height and with
    pass

def show_image(image_path):
    Label(root, text="Original image",font=("Arial", 12)).grid(row=1, column=2)    
    canv = Canvas(root, width=400, height=300, bg='white')
    canv.grid(row=2, column=2)

    img = Image.open('/home/ad.adasworks.com/reka.szabo/Downloads/Adding-seasoning-mixing-and-served-guacamole-with-chips.jpg')
    #arányosan méretezzen --> számoljuk ki a két értéket --> calc_img_size
    resized_img = img.resize((300,400), Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(resized_img)
    canv.create_image(0,0, anchor=NW, image=new_img)     

    Label(root, text="Modified image",font=("Arial", 12)).grid(row=3, column=2)    
    canv = Canvas(root, width=400, height=300, bg='white')
    canv.grid(row=4, column=2)

    img = Image.open('/home/ad.adasworks.com/reka.szabo/Downloads/Adding-seasoning-mixing-and-served-guacamole-with-chips.jpg')
    #arányosan méretezzen --> számoljuk ki a két értéket --> calc_img_size
    resized_img = img.resize((300,400), Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(resized_img)
    canv.create_image(0,0, anchor=NW, image=new_img)     

    root.mainloop()


#main 

def open_editor():
    btn_open.pack_forget()
    #img_path = browse_file()
    show_image('cica')

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