from tkinter import*


    # top = Tk()
    # label = Label(top,text="Shuabham",font=("consolas",40))
    # label.pack()
    # canvas = Canvas(top,bg="red",height=500,width=800)
    # canvas.pack()
    # top.mainloop()



main = Tk()

def leftKey(event):
    print("Left key pressed")

def rightKey(event):
    print("Right key pressed")

frame = Frame(main, width=400, height=400)
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
frame.pack()
main.mainloop()