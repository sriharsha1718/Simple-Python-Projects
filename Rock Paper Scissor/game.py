#Rock Paper Scissor Game
from tkinter import *
import random

root = Tk()
root.geometry("300x300")
root.title("Rock Paper Scissor")
root['bg']='black'

computer = {
	"0" : "Rock",
	"1" : "Paper",
	"2" : "Scissor"
}

def reset_game():
	b1['state'] = "active"
	b2['state'] = "active"
	b3['state'] = "active"
	l1.config(text="You")
	l3.config(text="Computer")
	l4.config(text="")

def button_disable():
	b1['state'] = "disable"
	b2['state'] = "disable"
	b3['state'] = "disable"

def isrock(): #player selects rock
	comp_value = computer[str(random.randint(0,2))]
	if comp_value == "Rock":
		result = "Draw!"
	elif comp_value == 'Scissor':
		result = "You Win!"
	else:
		result = "Computer Win!"
	l4.config(text=result)
	l3.config(text="Rock")
	l3.config(text=comp_value)
	button_disable

def ispaper(): #player selects paper
	comp_value = computer[str(random.randint(0,2))]
	if comp_value == "Paper":
		result = "Draw!"
	elif comp_value == 'Rock':
		result = "You Win!"
	else:
		result = "Computer Win!"
	l4.config(text=result)
	l3.config(text="Paper")
	l3.config(text=comp_value)
	button_disable

def isscissor(): #player selects scissor
	comp_value = computer[str(random.randint(0,2))]
	if comp_value == "Scissor":
		result = "Draw!"
	elif comp_value == 'Paper':
		result = "You Win!"
	else:
		result = "Computer Win!"
	l4.config(text=result)
	l3.config(text="Scissor")
	l3.config(text=comp_value)
	button_disable

Label(root, text="Rock Paper Scissor", font = "Calibri 20 bold", fg="White", bg="black").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame, text="You", font=10, bg="black", fg="White")
l2 = Label(frame, text="VS", font="normal 10 bold", bg="black", fg="White")
l3 = Label(frame, text="Computer", font=10, bg="black", fg="White")

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root, text="", font="normal 20 bold", bg="grey", width=15, borderwidth=2, relief='solid')
l4.pack(pady=20)


frame1 = Frame(root, bg="black")
frame1.pack()

b1 = Button(frame1, text="Rock", font="normal 10 bold", width=7, command=isrock, fg="White", bg="black")
b2 = Button(frame1, text="Paper", font="normal 10 bold", width=7, command=ispaper, fg="White", bg="black")
b3 = Button(frame1, text="Scissor", font="normal 10 bold", width=7, command=isscissor, fg="White", bg="black")

b1.pack(side=LEFT, padx = 10)
b2.pack(side=LEFT, padx = 10)
b3.pack(padx=10)

Button(root, text='Reset Game', font="normal 10 bold", fg='red', bg='black', command=reset_game).pack(pady=20)

root.mainloop()