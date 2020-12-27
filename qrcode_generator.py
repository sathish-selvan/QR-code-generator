import qrcode
import tkinter as tk
from PIL import Image,ImageTk


root  = tk.Tk()
root.geometry("250x100")
root.title("QR Code Generator")
def gen_qr(data):

    qr = qrcode.QRCode(version=1,box_size=10,border=5)
    
    if data == "":

        data="Please Enter something in the text box"

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black",back_color="white")

    img.save("1.png")
    top = tk.Toplevel()
    top.title("QR Code")
    img_lable =tk.Label(top)
    img_lable.image = ImageTk.PhotoImage(Image.open("1.png"))
    img_lable["image"]=img_lable.image

    img_lable.pack()

data = tk.StringVar()  
my_lable = tk.Label(root,text = "Enter the text",cursor="dot").grid(row=0,column=0,padx = 10, pady = 10)
my_entry = tk.Entry(root, textvariable=data).grid(row=0,column =1,padx = 10, pady = 10)

my_button = tk.Button(root, text ="GENERATE",cursor="heart",fg="red",command =lambda:gen_qr(data.get())).grid(row=1,column=0,padx=10,pady=10)


root.mainloop()
