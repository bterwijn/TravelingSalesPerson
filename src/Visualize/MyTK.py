
#from PIL import Image, ImageTk, ImageGrab  # For Windows & OSx
import pyscreenshot as ImageGrab # For Linux
from tkinter import *
import random

tk = Tk()
cv = Canvas(tk, width=800, height=800) # create canvas cv
cv.config(bg="black")
cv.pack(fill=BOTH, expand=YES)

def tk_update():
    tk.update_idletasks()
    tk.update()
tk_update()

def tk_save(filename):
    x=tk.winfo_x()
    y=tk.winfo_y()
    w=cv.winfo_width()
    h=cv.winfo_height()
    ImageGrab.grab((x,y,x+w,y+h)).save(filename)

def myDrawTest():
    cv.delete("all") # remove all previous drawings
    w=cv.winfo_width() # window knows its own size
    h=cv.winfo_height()
    cv.create_line(0, 0, w, h, # draw lines
              fill="blue",arrow=LAST,arrowshape=(12,14,5),width=3,dash=())
    cv.create_line(0, h, w, 0,
              fill="blue",arrow=LAST,arrowshape=(12,14,5),width=3,dash=())
    for i in range(0,100):
        x=20+random.random()*(w-40);
        y=20+random.random()*(h-40);
        cv.create_oval(x,
                       y,
                       x+random.random()*50+8,
                       y+random.random()*50+8,
                       fill="red");
    
if __name__ == "__main__":
    while True:
        myDrawTest()        # draw
        tk_update()         # update
        tk_save("test.png") # save
