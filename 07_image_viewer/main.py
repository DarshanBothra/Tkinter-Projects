from tkinter import *
import tkinter
from PIL import ImageTk, Image

def Back(imgNum):
    global my_label
    global btnNext
    global btnNext

    my_label.grid_forget() # for label to clear or get rid of something gridded!
    my_label = Label(image = imgList[imgNum - 1])
    btnNext = Button(
        root,
        text = "Next >",
        command = lambda: Next(imgNum + 1)
    )

    btnBack = Button(
        root,
        text = "< Back",
        command = lambda: Back(imgNum - 1)
    )

    if imgNum == 1:
        btnBack = Button(
            root,
            text = "< Back",
            state = DISABLED
        )

    my_label.grid(row=0, column=0, columnspan=3)
    btnBack.grid(row = 1, column = 0)
    btnNext.grid(row = 1, column = 2)


def Next(imgNum):
    global my_label
    global btnNext
    global btnNext

    my_label.grid_forget() # for label to clear or get rid of something gridded!
    my_label = Label(image = imgList[imgNum - 1])
    btnNext = Button(
        root,
        text = "Next >",
        command = lambda: Next(imgNum + 1)
    )

    btnBack = Button(
        root,
        text = "< Back",
        command = lambda: Back(imgNum - 1)
    )

    if imgNum == 4:
        btnNext = Button(
            root,
            text = "Next >",
            state = DISABLED
        )

    if imgNum == 1:
        btnBack = Button(
            root,
            text = "Next >",
            state = DISABLED
        )

    my_label.grid(row=0, column=0, columnspan=3)
    btnBack.grid(row = 1, column = 0)
    btnNext.grid(row = 1, column = 2)

root = Tk()
root.title("  Image Viewer")
root.iconbitmap("image_viewer_logo.ico")

myImg1 = ImageTk.PhotoImage(Image.open("01.png"))
myImg2 = ImageTk.PhotoImage(Image.open("baka.jpg"))
myImg3 = ImageTk.PhotoImage(Image.open("one_punch_man.jpg"))
myImg4 = ImageTk.PhotoImage(Image.open("wide_putin.jpg"))

imgList = [
    myImg1,
    myImg2,
    myImg3,
    myImg4
]

my_label = Label(
    root,
    image = myImg1
)

btnBack = Button(
    root,
    text = "< Back",
    command = lambda: Back(1)
)
btnNext =Button(
    root,
    text = "Next >",
    command = lambda:Next(2)
)
btnExit =Button(
    root,
    text = "Exit",
    command = root.quit
)

my_label.grid(row = 0, column = 0, columnspan = 3)
btnBack.grid(row = 1, column = 0)
btnExit.grid(row = 1, column = 1)
btnNext.grid(row = 1, column = 2)


root.mainloop()


