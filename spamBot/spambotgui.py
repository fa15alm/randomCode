import tkinter as tk
import pyautogui, time, keyboard

pyautogui.PAUSE = 0.01
HEIGHT = 500
WIDTH = 600
text = 'You\'re Getting Spammed!'
amount = 50
LOOPSLEEPTIME = 0.15

def setText(newText):
    global text
    if(newText == 'reset'):
        text = 'You\'re Getting Spammed!'
    text = newText
    textLab['text'] = 'Current Text: ' + text
    textEntry.delete(0, 'end')

def setAmount(newAmount):
    global amount
    if(newAmount == 'reset'):
        amount = 50
    amount = int(newAmount)
    amountLab['text'] = 'Current Amount: ' + str(amount) + ' times'
    amountEntry.delete(0, 'end')

def spamBot():
    time.sleep(5)
    for x in range(1, amount + 1):
        pyautogui.typewrite(text)
        pyautogui.press('enter')
        time.sleep(LOOPSLEEPTIME)

root = tk.Tk()
root.title('SpamBot')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#TO SET TEXT

textFrame = tk.Frame(root, bg='#80c1ff', bd=5)
textFrame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

textButton = tk.Button(textFrame,  text='Set Text', font=40, command=lambda: setText(textEntry.get()))
textButton.place(relx=0.7, relheight=1, relwidth=0.3)

textEntry = tk.Entry(textFrame, font=40)
textEntry.place(relwidth=0.65, relheight=1)

textLab = tk.Label(root, text='Current Text: ' + text, anchor='n')
textLab.place(relx=0.5, rely=0.03, anchor='n')

#TO SET AMOUNT

amountFrame = tk.Frame(root, bg='#80c1ff', bd=5)
amountFrame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.1, anchor='n')

amountButton = tk.Button(amountFrame,  text='Set Amount', font=40, command=lambda: setAmount(amountEntry.get()))
amountButton.place(relx=0.7, relheight=1, relwidth=0.3)

amountEntry = tk.Entry(amountFrame, font=40)
amountEntry.place(relwidth=0.65, relheight=1)

amountLab = tk.Label(root, text='Current Amount: ' + str(amount) + ' times', anchor='n')
amountLab.place(relx=0.5, rely=0.23, anchor='n')

# SpamBot Button

spamBotFrame = tk.Frame(root, bg='#80c1ff', bd=5)
spamBotFrame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.1, anchor='n')

spamBotButton = tk.Button(spamBotFrame, text='Start SpamBot (5s Buffer Time)', font=40, command=lambda: spamBot())
spamBotButton.place(relx=0.5, relheight=1, relwidth=0.9, anchor = 'n')

root.mainloop()
