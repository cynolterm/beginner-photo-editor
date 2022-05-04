from tkinter import *
from tkinter import filedialog
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
        self.editor.show_image_with_label(newPath, "Modified Image", 3, 2)
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
        self.editor.show_image_with_label(newPath, "Modified Image", 3, 2)
        self.imgP = newPath
        # TODO: functionality for flip vertically
        pass

    def rotate(self):
        # if not amount:
        amount = 45
        img = Image.open(self.imgP)
        newImg = img.rotate(amount)
        newPath = self.imgP
        newPath = newPath[:-4]
        newPath = newPath + "_rotated.jpg"
        newImg.save(newPath)
        self.editor.show_image_with_label(newPath, "Modified Image", 3, 2)
        self.imgP = newPath
        # TODO: functionality for rotate
        pass

    def resize():
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

    def browse_file(self):
        f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')]  
        root.update()
        file_name = filedialog.askopenfilename(initialdir = "/home/ad.adasworks.com/reka.szabo/", title = "Select a File", filetypes = f_types, multiple=False)
        self.fun.setImg(file_name)
        return file_name

    def calc_img_size(self, img):
        new_w = round(self.screen_w*0.5)
        new_h = round(self.screen_h*0.45)
        print(self.screen_h, self.screen_w, new_w, new_h)
        w, h = img.size
        if h > new_h or w > new_w:
            if round((new_w/w)*h) > new_h: 
                return new_h, round((new_h/h)*w)
            else: 
                return round((new_w/w)*h), new_w
        else:
            return h, w
        

    def show_image_with_label(self, img_path, txt, px, py):
        print(px, py)
        Label(root, text=txt,font=("Arial", 12), justify=CENTER).grid(row=px, column=py)    
        print(Label)
        cw = self.screen_w*0.5
        ch = self.screen_h*0.45
        canv = Canvas(root, width=cw, height=ch)
        canv.grid(row=px+1, column=py, rowspan=4, sticky=E)

        img = Image.open(img_path)
        img_h, img_w = self.calc_img_size(img)
        resized_img = img.resize((img_w, img_h))
        new_img = ImageTk.PhotoImage(resized_img)
        canv.create_image(10,10, anchor=NW, image=new_img)
        self.imgs.append(new_img)

        root.update()

    def add_button(self, name, px, py, cmd):
        btn = Button(root, text=name, width=25, command=cmd)
        btn.grid(row=px, column=py, padx = self.screen_w*0.2)
        self.btns.append(btn)

    def choose_color(self):
        self.watermark_color = colorchooser.askcolor(title ="Choose color")
        print(self.watermark_color)

    def watermark(self):
        Label(self.frame, text='Options' ,font=("Arial", 12), justify=CENTER).grid(row=6, column=1)    

        self.watermark_color = 'black'
        btn_color = Button(self.frame, text='Choose color', width=25, command=self.choose_color)
        btn_color.grid(row = 7, column = 1)
        text_editor = Text(self.frame, width=40, height=1)
        text_editor.grid(row=8, column=1)
        opacity_value = DoubleVar()
        opacity = Scale(self.frame, variable = opacity_value, from_ = 0, to = 100, orient = HORIZONTAL)
        opacity.set(100)
        opacity.grid(row=9, column=1)

        btn = Button(self.frame, text='Go!', width=25, command= lambda: self.fun.watermark(color=self.watermark_color[1], text=text_editor.get(0.1,END), opacity=opacity_value.get()))
        btn.grid(row=10, column=1)
         # TODO: color picker, fontsize, textbox for the text and slider for opacity
        pass

    def threshold(self):
         # TODO: slider (0-255) for thresholding level
        pass

    def rgb(self):
        # TODO: three sliders for Red, Green and Blue
        pass

    def open_new_file(self):
        img_path = self.browse_file()
        self.show_image_with_label(img_path, 'Original image', 1, 2)
        self.show_image_with_label(img_path, 'Modified image', 3, 2)

    def open_editor(self):
        btn_open.place_forget()
        menu = Menu(root)
        self.frame = Frame(root)
        self.frame.grid(row=6, column=1, rowspan=5)
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
        transfmenu.add_command(label='Rotate', command=self.fun.rotate)
        transfmenu.add_command(label='Resize', command=self.fun.resize)

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