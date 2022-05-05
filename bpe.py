from cgitb import text
from re import I
from tkinter import *
from tkinter import filedialog
import tkinter
from turtle import back
from PIL import Image, ImageTk, ImageOps
from tkinter import colorchooser

#implementing methods for functionality
class Functionality:
    def __init__(self):
        pass

    def flip_hor(self):
        img = Image.open(self.imgP)
        newImg = ImageOps.mirror(img)
        newPath = self.imgP
        newPath = newPath[:-4]
        newPath = newPath + "_flip_hor.jpg"
        newImg.save(newPath)
        self.editor.show_image_with_label(newPath, "Modified Image", 6, 2)
        self.imgP = newPath
        # TODO: functionality for flip horizontally
        pass

    def flip_ver(self):
        img = Image.open(self.imgP)
        newImg = ImageOps.flip(img)
        newPath = self.imgP
        newPath = newPath[:-4]
        newPath = newPath + "_flip_ver.jpg"
        newImg.save(newPath)
        self.editor.show_image_with_label(newPath, "Modified Image", 6, 2)
        self.imgP = newPath
        # TODO: functionality for flip vertically
        pass

    def rotate(self, angle): ##angle value added to arguments list --> on every change of the scaler, rotate the image with angle
        # if not amount:
        amount = 45
        img = Image.open(self.imgP)
        newImg = img.rotate(amount)
        newPath = self.imgP
        newPath = newPath[:-4]
        newPath = newPath + "_rotated.jpg"
        newImg.save(newPath)
        self.editor.show_image_with_label(newPath, "Modified Image", 6, 2)
        self.imgP = newPath
        # TODO: functionality for rotate
        pass

    def resize(self, width):
        print(width)
        # TODO: functionality for resize
        pass

    def grayscale(self):
        img = Image.open(self.imgP)
        newImg = ImageOps.grayscale(img)
        newPath = self.imgP
        newPath = newPath[:-4]
        newPath = newPath + "_grayscale.jpg"
        newImg.save(newPath)
        self.editor.show_image_with_label(newPath, "Modified Image", 3, 2)
        self.imgP = newPath
         # TODO: functionality for grayscaling
        pass

    def watermark(self, color, text, opacity):
        print(color, text, opacity, 'cica')
        # TODO: functionality for watermark
        pass

    def threshold(self, level):
        print(level)
        #TODO: functionality for thresholding

    def rgb_transformation(self, r, g, b):
        print(r.get(), g.get(), b.get())
        #TODO: functioanlity for rgb

    def setImg(self, path):
        self.imgP = path
        pass

    def setEditor(self, e):
        self.editor = e

    imgP = ""
    editor = ""


class Editor:
    def __init__(self):
        self.screen_w = root.winfo_screenwidth()
        self.screen_h = root.winfo_screenheight()
        self.imgs = []
        self.fun = Functionality()
        self.fun.setEditor(self)
        self.btns = []
        self.img_width = 0
        self.img_height = 0

    def set_img_size(self, width, height):
        self.img_width = width
        self.img_height = height

    def browse_file(self):
        f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')]  
        root.update()
        file_name = filedialog.askopenfilename(initialdir = "/home/ad.adasworks.com/reka.szabo/", title = "Select a File", filetypes = f_types, multiple=False)
        self.fun.setImg(file_name)
        return file_name

    def calc_img_size(self, img):
        new_w = round(self.screen_w*0.5)
        new_h = round(self.screen_h*0.45)
        w, h = img.size
        if h > new_h or w > new_w:
            if round((new_w/w)*h) > new_h: 
                self.img_height = new_h
                self.img_width = round((new_h/h)*w)
            else: 
                self.img_height = round((new_w/w)*h)
                self.img_width = new_w
        else:
            return h, w
        
    def clear_frame(self):
        for widget in self.frame.winfo_children():
            if type(widget) == tkinter.Label and widget['text'] == 'Options':
                pass
            else:
                widget.destroy()

    def show_image_with_label(self, img_path, txt, px, py):
        Label(root, text=txt,font=("Arial", 12), justify=CENTER).grid(row=px, column=py)
        cw = self.screen_w*0.5
        ch = self.screen_h*0.45
        canv = Canvas(root, width=cw, height=ch)
        canv.grid(row=px+1, column=py, rowspan=4, sticky=E)

        img = Image.open(img_path)
        self.calc_img_size(img)
        resized_img = img.resize((self.img_width, self.img_height))
        self.new_img = ImageTk.PhotoImage(resized_img)
        canv.create_image(10,10, anchor=NW, image=self.new_img)
        self.imgs.append(self.new_img)

        root.update()

    def add_button(self, name, px, py, cmd):
        btn = Button(root, text=name, width=25, command=cmd)
        btn.grid(row=px, column=py, padx = self.screen_w*0.2)
        self.btns.append(btn)

    def create_scaler(self, min, max, default, orient, px, py, command = None):
        scale_value = DoubleVar()
        scaler = Scale(self.frame, variable = scale_value, from_ = min, to = max, orient = orient, command= lambda: command)
        scaler.set(default)
        scaler.grid(row=px, column=py)
        return scale_value

    def choose_color(self):
        self.watermark_color = colorchooser.askcolor(title ="Choose color")

    def watermark(self):
        self.clear_frame()   

        self.watermark_color = 'black'
        btn_color = Button(self.frame, text='Choose color', width=25, command=self.choose_color)
        btn_color.grid(row = 7, column = 1)
        text_editor = Text(self.frame, width=40, height=1)
        text_editor.grid(row=8, column=1)
        opacity_value = self.create_scaler(0, 100, 100, HORIZONTAL, 9, 1)

        btn = Button(self.frame, text='Go!', width=25, command= lambda: self.fun.watermark(color=self.watermark_color[1], text=text_editor.get(0.1,END), opacity=opacity_value.get()))
        btn.grid(row=10, column=1)

    def threshold(self):
        self.clear_frame()

        threshold_value = self.create_scaler(0, 255, 127, HORIZONTAL, 7, 1)

        btn = Button(self.frame, text='Go!', width=25, command= lambda: self.fun.threshold(level=threshold_value.get()))
        btn.grid(row=8, column=1)

    def rgb(self):
        self.clear_frame()

        Label(self.frame, text='Red' ,font=("Arial", 10), justify=CENTER).grid(row=7, column=1) 
        #self.red = self.create_scaler(0, 255, 255, VERTICAL, 8, 1, self.show_cicaolor)
        red_value = DoubleVar()
        red = Scale(self.frame, variable = red_value, from_ = 0, to = 255, orient = VERTICAL, command= lambda x: self.fun.rgb_transformation(red_value, green_value, blue_value))
        red.set(127)
        red.grid(row=8, column=1)
        Label(self.frame, text='Green' ,font=("Arial", 10), justify=CENTER).grid(row=7, column=2) 
        #self.green = self.create_scaler(0, 255, 255, VERTICAL, 8, 2)
        green_value = DoubleVar()
        green = Scale(self.frame, variable = green_value, from_ = 0, to = 255, orient = VERTICAL, command= lambda x: self.fun.rgb_transformation(red_value, green_value, blue_value))
        green.set(127)
        green.grid(row=8, column=2)
        Label(self.frame, text='Blue' ,font=("Arial", 10), justify=CENTER).grid(row=7, column=3) 
        #self.blue = self.create_scaler(0, 255, 255, VERTICAL, 8, 3)
        blue_value = DoubleVar()
        blue = Scale(self.frame, variable = blue_value, from_ = 0, to = 255, orient = VERTICAL, command= lambda x: self.fun.rgb_transformation(red_value, green_value, blue_value))
        blue.set(127)
        blue.grid(row=8, column=3)

    def rotate(self):
        self.clear_frame()

        angle_value = DoubleVar()
        angle = Scale(self.frame, variable = angle_value, from_ = 0, to = 360, length= 300, orient = HORIZONTAL, tickinterval=90, command= lambda x: self.fun.rotate(angle_value))
        angle.set(0)
        angle.grid(row=8, column=1)

    def resize(self):
        self.clear_frame()

        Label(self.frame, text='Width' ,font=("Arial", 10), justify=CENTER).grid(row=7, column=1) 
        width_var = StringVar(root)
        width_var.set(str(self.img_width))
        width_editor = Spinbox(self.frame, from_= 0, to=3000, textvariable=width_var,  command= lambda: self.fun.resize(int(width_editor.get()), int(height_editor.get())))
        width_editor.grid(row=8, column=1)

        Label(self.frame, text='Height' ,font=("Arial", 10), justify=CENTER).grid(row=10, column=1) 
        height_var = StringVar(root)
        height_var.set(str(self.img_height))
        height_editor = Spinbox(self.frame, from_= 0, to=3000, textvariable= height_var,  command= lambda: self.fun.resize(int(width_editor.get()), int(height_editor.get())))
        height_editor.grid(row=11, column=1)

    def open_new_file(self):
        img_path = self.browse_file()
        self.show_image_with_label(img_path, 'Original image', 1, 2)
        self.show_image_with_label(img_path, 'Modified image', 6, 2)

    def open_editor(self):
        btn_open.place_forget()
        menu = Menu(root)
        self.frame = Frame(root)
        self.frame.grid(row=6, column=1, rowspan=5)
        Label(self.frame, text='Options' ,font=("Arial", 12), justify=CENTER).grid(row=6, column=1) 
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Open...', command=self.open_new_file)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=root.quit)
        transfmenu = Menu(menu)
        menu.add_cascade(label='Transform', menu=transfmenu)
        transfmenu.add_command(label='Flip horizontally', command=self.fun.flip_hor)
        transfmenu.add_command(label='Flip vertically', command=self.fun.flip_ver)
        transfmenu.add_command(label='Rotate', command=self.rotate)
        transfmenu.add_command(label='Resize', command=self.resize)

        img_path = self.browse_file()
        self.show_image_with_label(img_path, 'Original image', 1, 2)
        self.show_image_with_label(img_path, 'Modified image', 6, 2)

        self.add_button('Watermark', 2, 1, self.watermark)
        self.add_button('Threshold', 3, 1, self.threshold)
        self.add_button('Grayscale', 4, 1, self.fun.grayscale)
        self.add_button('RGB transformations', 5, 1, self.rgb)

        root.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight())) #fullscreen mode
    root.title('Photo editor for beginners')
    editor = Editor()
    btn_open = Button(root, text='Open', width=25, command=editor.open_editor)
    btn_open.place(relx=0.5, rely=0.5, anchor=CENTER)
    mainloop()