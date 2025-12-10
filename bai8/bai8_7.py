
import tkinter
import random

colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']

score = 0
timeleft = 120   

def startGame(event):
    if timeleft == 120:
        countdown()
    nextColour()

def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()

        if e.get().lower() == colours[1].lower():
            score += 2   
        elif e.get() != "":
            score -= 1   

        e.delete(0, tkinter.END)

        random.shuffle(colours)

        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Điểm số: " + str(score))

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Thời gian còn lại: " + str(timeleft))
        timeLabel.after(1000, countdown)
root = tkinter.Tk()
root.title("TRÒ CHƠI MÀU SẮC")
root.geometry("400x250")

instructions = tkinter.Label(root, 
    text="Nhập tên màu của chữ hiển thị (bằng tiếng Anh), không phải nội dung chữ!",
    font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Nhấn Enter để bắt đầu", font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Thời gian còn lại: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

root.mainloop()
