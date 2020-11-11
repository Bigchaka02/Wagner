from tkinter import *

# https://pypi.org/project/tkmacosx/
# pip3 install tkmacosx
from tkmacosx import *

#Hello

classes = ['SDS A', 'Fundamentals C', 'CSP D', 'CSP E', 'APCS F']

# ==================================================================================================================================
# ==================================================================================================================================
# ==================================================================================================================================

def DrawText(pic, text):

    global wordsLabel
    global puppyLabel
    puppyLabel.config(image=pic)

    #frame2.delete()
    wordsLabel.config(text=text)

    pass

# ==================================================================================================================================
# ==================================================================================================================================
# ==================================================================================================================================


root = Tk()
root.title("Mr. Wagner Card")
root.configure(background='light pink')

frame1 = Frame(root, bg='sky blue', bd=10)
frame1.pack(side=TOP)

label1 = Label(frame1, text="Mr. Wagner,", fg="black", bg="sky blue", width=25, height=1)
label1.pack(side=TOP)


mainCanvas = Canvas(frame1, width=400, height=400, bg='sky blue')
mainCanvas.pack(side=TOP)


# this adds photo to main canvas
puppy = PhotoImage(file='dapup.png')
puppyPhoto1 = PhotoImage(file='puppy1.png')
puppyPhoto2 = PhotoImage(file='puppy2.png')
puppyPhoto3 = PhotoImage(file='puppy3.png')
puppyPhoto4 = PhotoImage(file='puppy4.png')
puppyPhoto5 = PhotoImage(file='puppy5.png')

puppyLabel = Label(mainCanvas, image=puppy)
puppyLabel.pack()

wordsLabel = Label(mainCanvas, text='Click a class below.', fg="black", bg="light grey")
wordsLabel.pack(side=TOP)

frame2 = Frame(root)
frame2.pack(side=BOTTOM)

c1 = Button(frame2, text=classes[0], borderless=1, bg='white', command=lambda: DrawText(puppyPhoto1, '"We are very sorry for your loss and you are in our thoughts and prayers.\nAs students of yours for two years now, we’ve been able to see your positive attitude and quirky\nhumor firsthand and can’t imagine what you’re going through right now. We can’t wait to see you and hear some more dad jokes!" -' + classes[0]))
c1.pack(side=LEFT)

c2 = Button(frame2, text=classes[1], borderless=1, bg='white', command=lambda: DrawText(puppyPhoto2, '"On behalf of our programming class, we want to tell you that we love you and support you." -' + classes[1]))
c2.pack(side=LEFT)

c3 = Button(frame2, text=classes[2], borderless=1, bg='white', command=lambda: DrawText(puppyPhoto3, '"We think about you every day, and we are deeply sorry for your loss." -' + classes[2]))
c3.pack(side=LEFT)

c4 = Button(frame2, text=classes[3], borderless=1, bg='white', command=lambda: DrawText(puppyPhoto4, '"We have all been thinking of you during this time, we missed you and we can\'t wait to see you in class." -' + classes[3]))
c4.pack(side=LEFT)

c5 = Button(frame2, text=classes[4], borderless=1, bg='white', command=lambda: DrawText(puppyPhoto5, '"We missed you, and we hope you know you\'re surrounded by people who love you." -' + classes[4]))
c5.pack(side=LEFT)

#c6 = Button(frame2, text="Home Screen", borderless=1, bg='white', command=lambda: HomeScreen(''))
#c6.pack(side=RIGHT)


# ==================================================================================================================================

mainloop()
