from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
from tkinter import font as tkfont
import random


# ---------------Initialized frames-------------
class TicTac(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Computer, Player):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


# ---------------Initialized frames-------------

# -----------------start window--------------------

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller = controller
        controller.title("Tic Tac Toe")
        Tk.configure(self, bg="lightblue")
        path = "/home/ajmal/PycharmProjects/pro1/ttt.jpg"

        def showImg(img):
            image = Image.open(img)
            photo = ImageTk.PhotoImage(image)
            canvas = Canvas(self, width=277, height=315)
            canvas.create_image(0, 0, image=photo, anchor="nw")
            canvas.photo = photo
            canvas.place(x=-1, y=-1)
            canvas.create_text(135, 40, font=("Times", 30, "bold"), text="Tic Tac Toe")

        showImg(path)

        button1 = Button(self, text="vs Computer", bg="light gray", fg="black", width=8, height=2,
                         command=lambda: controller.show_frame("Computer"))
        button2 = Button(self, text="vs Player", bg="light gray", fg="black", width=8, height=2,
                         command=lambda: controller.show_frame("Player"))
        button1.place(x=10, y=140)
        button2.place(x=10, y=210)


# -----------------start window end--------------------

Cflag = 0
Clist = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# ---------------------vs computer window-------------------
class Computer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def result():
            global Cflag
            if Cflag <= 5 and (b1["text"] == b2["text"] and b2["text"] == b3["text"] and b1["text"] == "X" or
                               b4["text"] == b5["text"] and b5["text"] == b6["text"] and b4["text"] == "X" or
                               b7["text"] == b8["text"] and b8["text"] == b9["text"] and b7["text"] == "X" or
                               b1["text"] == b4["text"] and b4["text"] == b7["text"] and b1["text"] == "X" or
                               b2["text"] == b5["text"] and b5["text"] == b8["text"] and b2["text"] == "X" or
                               b3["text"] == b6["text"] and b6["text"] == b9["text"] and b3["text"] == "X" or
                               b1["text"] == b5["text"] and b5["text"] == b9["text"] and b1["text"] == "X" or
                               b3["text"] == b5["text"] and b5["text"] == b7["text"] and b3["text"] == "X"):
                showinfo("Game Over", "You won")

            elif Cflag <= 5 and (b1["text"] == b2["text"] and b2["text"] == b3["text"] and b1["text"] == "0" or
                                 b4["text"] == b5["text"] and b5["text"] == b6["text"] and b4["text"] == "0" or
                                 b7["text"] == b8["text"] and b8["text"] == b9["text"] and b7["text"] == "0" or
                                 b1["text"] == b4["text"] and b4["text"] == b7["text"] and b1["text"] == "0" or
                                 b2["text"] == b5["text"] and b5["text"] == b8["text"] and b2["text"] == "0" or
                                 b3["text"] == b6["text"] and b6["text"] == b9["text"] and b3["text"] == "0" or
                                 b1["text"] == b5["text"] and b5["text"] == b9["text"] and b1["text"] == "0" or
                                 b3["text"] == b5["text"] and b5["text"] == b7["text"] and b3["text"] == "0"):
                showinfo("Game Over", "You lose ")
            elif Cflag >= 5:
                showinfo("Game Over", "Tie")

        def set(num):
            global Cflag, Clist
            if num == 1:
                if b1["text"] == " ":
                    Clist.remove(1)
                    b1["text"] = "X"
                    random.seed()
                    if len(Clist) >= 1:
                        no = random.choice(Clist)
                        Clist.remove(no)
                        if no == 2 and b2["text"] == " ":
                            b2["text"] = "0"
                        elif no == 3 and b3["text"] == " ":
                            b3["text"] = "0"
                        elif no == 4 and b4["text"] == " ":
                            b4["text"] = "0"
                        elif no == 5 and b5["text"] == " ":
                            b5["text"] = "0"
                        elif no == 6 and b6["text"] == " ":
                            b6["text"] = "0"
                        elif no == 7 and b7["text"] == " ":
                            b7["text"] = "0"
                        elif no == 8 and b8["text"] == " ":
                            b8["text"] = "0"
                        elif no == 9 and b9["text"] == " ":
                            b9["text"] = "0"

                    Cflag += 1
                    result()
                else:
                    showinfo("Error", "Button is already clicked")
            elif num == 2:
                if b2["text"] == " ":
                    Clist.remove(2)
                    b2["text"] = "X"
                    random.seed()
                    if len(Clist) >= 1:
                        no = random.choice(Clist)
                        Clist.remove(no)
                        if no == 1 and b1["text"] == " ":
                            b1["text"] = "0"
                        elif no == 3 and b3["text"] == " ":
                            b3["text"] = "0"
                        elif no == 4 and b4["text"] == " ":
                            b4["text"] = "0"
                        elif no == 5 and b5["text"] == " ":
                            b5["text"] = "0"
                        elif no == 6 and b6["text"] == " ":
                            b6["text"] = "0"
                        elif no == 7 and b7["text"] == " ":
                            b7["text"] = "0"
                        elif no == 8 and b8["text"] == " ":
                            b8["text"] = "0"
                        elif no == 9 and b9["text"] == " ":
                            b9["text"] = "0"
                    Cflag += 1
                    result()
                else:
                    showinfo("", "Button is already clicked")
            elif num == 3:
                if b3["text"] == " ":
                    Clist.remove(3)
                    b3["text"] = "X"
                    random.seed()
                    if len(Clist) >= 1:
                        no = random.choice(Clist)
                        Clist.remove(no)
                        if no == 1 and b1["text"] == " ":
                            b1["text"] = "0"
                        elif no == 2 and b2["text"] == " ":
                            b2["text"] = "0"
                        elif no == 4 and b4["text"] == " ":
                            b4["text"] = "0"
                        elif no == 5 and b5["text"] == " ":
                            b5["text"] = "0"
                        elif no == 6 and b6["text"] == " ":
                            b6["text"] = "0"
                        elif no == 7 and b7["text"] == " ":
                            b7["text"] = "0"
                        elif no == 8 and b8["text"] == " ":
                            b8["text"] = "0"
                        elif no == 9 and b9["text"] == " ":
                            b9["text"] = "0"
                    Cflag += 1
                    result()
                else:
                    showinfo("", "Button is already clicked")
            elif num == 4:
                if b4["text"] == " ":
                    Clist.remove(4)
                    b4["text"] = "X"
                    random.seed()
                    if len(Clist) >= 1:
                        no = random.choice(Clist)
                        Clist.remove(no)
                        if no == 1 and b1["text"] == " ":
                            b1["text"] = "0"
                        elif no == 2 and b2["text"] == " ":
                            b2["text"] = "0"
                        elif no == 3 and b3["text"] == " ":
                            b3["text"] = "0"
                        elif no == 5 and b5["text"] == " ":
                            b5["text"] = "0"
                        elif no == 6 and b6["text"] == " ":
                            b6["text"] = "0"
                        elif no == 7 and b7["text"] == " ":
                            b7["text"] = "0"
                        elif no == 8 and b8["text"] == " ":
                            b8["text"] = "0"
                        elif no == 9 and b9["text"] == " ":
                            b9["text"] = "0"
                    Cflag += 1
                    result()
                else:
                    showinfo("", "Button is already clicked")
            elif num == 5:
                if b5["text"] == " ":
                    Clist.remove(5)
                    b5["text"] = "X"
                    random.seed()
                    if len(Clist) >= 1:
                        no = random.choice(Clist)
                        Clist.remove(no)
                        if no == 1 and b1["text"] == " ":
                            b1["text"] = "0"
                        elif no == 3 and b3["text"] == " ":
                            b3["text"] = "0"
                        elif no == 4 and b4["text"] == " ":
                            b4["text"] = "0"
                        elif no == 2 and b2["text"] == " ":
                            b2["text"] = "0"
                        elif no == 6 and b6["text"] == " ":
                            b6["text"] = "0"
                        elif no == 7 and b7["text"] == " ":
                            b7["text"] = "0"
                        elif no == 8 and b8["text"] == " ":
                            b8["text"] = "0"
                        elif no == 9 and b9["text"] == " ":
                            b9["text"] = "0"
                    Cflag += 1
                    result()
                else:
                    showinfo("", "Button is already clicked")
            elif num == 6:
                if b6["text"] == " ":
                    Clist.remove(6)
                    b6["text"] = "X"
                    random.seed()
                    if len(Clist) >= 1:
                        no = random.choice(Clist)
                        Clist.remove(no)
                        if no == 1 and b1["text"] == " ":
                            b1["text"] = "0"
                        elif no == 3 and b3["text"] == " ":
                            b3["text"] = "0"
                        elif no == 4 and b4["text"] == " ":
                            b4["text"] = "0"
                        elif no == 5 and b5["text"] == " ":
                            b5["text"] = "0"
                        elif no == 2 and b2["text"] == " ":
                            b2["text"] = "0"
                        elif no == 7 and b7["text"] == " ":
                            b7["text"] = "0"
                        elif no == 8 and b8["text"] == " ":
                            b8["text"] = "0"
                        elif no == 9 and b9["text"] == " ":
                            b9["text"] = "0"
                    Cflag += 1
                    result()
                else:
                    showinfo("", "Button is already clicked")
            elif num == 7:
                if b7["text"] == " ":
                    Clist.remove(7)
                    b7["text"] = "X"
                    random.seed()
                    if len(Clist) >= 1:
                        no = random.choice(Clist)
                        Clist.remove(no)
                        if no == 1 and b1["text"] == " ":
                            b1["text"] = "0"
                        elif no == 3 and b3["text"] == " ":
                            b3["text"] = "0"
                        elif no == 4 and b4["text"] == " ":
                            b4["text"] = "0"
                        elif no == 5 and b5["text"] == " ":
                            b5["text"] = "0"
                        elif no == 6 and b6["text"] == " ":
                            b6["text"] = "0"
                        elif no == 2 and b2["text"] == " ":
                            b2["text"] = "0"
                        elif no == 8 and b8["text"] == " ":
                            b8["text"] = "0"
                        elif no == 9 and b9["text"] == " ":
                            b9["text"] = "0"
                    Cflag += 1
                    result()
                else:
                    showinfo("", "Button is already clicked")
            elif num == 8:
                if b8["text"] == " ":
                    Clist.remove(8)
                    b8["text"] = "X"
                    random.seed()
                    if len(Clist) >= 1:
                        no = random.choice(Clist)
                        Clist.remove(no)
                        if no == 1 and b1["text"] == " ":
                            b1["text"] = "0"
                        elif no == 3 and b3["text"] == " ":
                            b3["text"] = "0"
                        elif no == 4 and b4["text"] == " ":
                            b4["text"] = "0"
                        elif no == 5 and b5["text"] == " ":
                            b5["text"] = "0"
                        elif no == 6 and b6["text"] == " ":
                            b6["text"] = "0"
                        elif no == 7 and b7["text"] == " ":
                            b8["text"] = "0"
                        elif no == 2 and b2["text"] == " ":
                            b2["text"] = "0"
                        elif no == 9 and b9["text"] == " ":
                            b9["text"] = "0"
                    Cflag += 1
                    result()
                else:
                    showinfo("", "Button is already clicked")
            elif num == 9:
                result()
                if b9["text"] == " ":
                    Clist.remove(9)
                    b9["text"] = "X"
                    random.seed()
                    if len(Clist) >= 1:
                        no = random.choice(Clist)
                        Clist.remove(no)
                        if no == 1 and b1["text"] == " ":
                            b1["text"] = "0"
                        elif no == 3 and b3["text"] == " ":
                            b3["text"] = "0"
                        elif no == 4 and b4["text"] == " ":
                            b4["text"] = "0"
                        elif no == 5 and b5["text"] == " ":
                            b5["text"] = "0"
                        elif no == 6 and b6["text"] == " ":
                            b6["text"] = "0"
                        elif no == 7 and b7["text"] == " ":
                            b7["text"] = "0"
                        elif no == 8 and b8["text"] == " ":
                            b8["text"] = "0"
                        elif no == 2 and b2["text"] == " ":
                            b2["text"] = "0"
                    Cflag += 1
                    result()
                else:
                    showinfo("", "Button is already clicked")

        def reset():
            global Cflag, Clist
            Cflag = 0
            b1["text"] = " "
            b2["text"] = " "
            b3["text"] = " "
            b4["text"] = " "
            b5["text"] = " "
            b6["text"] = " "
            b7["text"] = " "
            b8["text"] = " "
            b9["text"] = " "
            Clist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        b1 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(1))
        b1.grid(row=0, column=0)
        b2 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(2))
        b2.grid(row=0, column=1)
        b3 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(3))
        b3.grid(row=0, column=2)
        b4 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(4))
        b4.grid(row=1, column=0)
        b5 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(5))
        b5.grid(row=1, column=1)
        b6 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(6))
        b6.grid(row=1, column=2)
        b7 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(7))
        b7.grid(row=2, column=0)
        b8 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(8))
        b8.grid(row=2, column=1)
        b9 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(9))
        b9.grid(row=2, column=2)
        res = Button(self, text="Reset", bg="gray", width=8, height=3, command=lambda: reset())
        res.grid(row=3, column=1)
        home = tk.Button(self, text="Home", bg="gray", width=8, height=3,
                         command=lambda: controller.show_frame("StartPage"))
        home.grid(row=3, column=2)
        player = Button(self, text="vs Player", bg="gray", width=8, height=3,
                        command=lambda: controller.show_frame("Player"))
        player.grid(row=3, column=0)


# ---------------------vs computer window end-------------------
player1 = []  # it will store button no pressed by the player 1
player2 = []  # it will store button no pressed by the player 2
turn = 1
flag = 0


# ---------------------vs player window-------------------
class Player(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def result():
            global player1, player2
            from itertools import permutations
            set1 = permutations([1, 2, 3])
            set2 = permutations([4, 5, 6])
            set3 = permutations([7, 8, 9])
            set4 = permutations([1, 4, 7])
            set5 = permutations([2, 5, 8])
            set6 = permutations([3, 6, 9])
            set7 = permutations([1, 5, 9])
            set8 = permutations([3, 5, 7])
            for i in set1, set2, set3, set4, set5, set6, set7, set8:
                for j in list(i):
                    plyr1 = all(elem in player1 for elem in j)
                    plyr2 = all(elem in player2 for elem in j)
                if flag <= 9 and plyr1 == True:
                    showinfo("Game Over", "player 1 X has won")
                    break
                elif flag <= 9 and plyr2 == True:
                    showinfo("Game Over", "player 2 0 has won")
                    break
                elif flag >= 9:
                    showinfo("Game Over", "Tie")
                    break

        def set(num):
            global turn, flag, player1, player2
            if num == 1:
                if b1["text"] == " ":
                    if turn == 1:
                        b1["text"] = "X"
                        player1.append(num)
                        turn = 2
                    elif turn == 2:
                        b1["text"] = "O"
                        player2.append(num)
                        turn = 1
                    flag += 1
                else:
                    showinfo("Tic-Tac-Toe", "Button already Clicked!")
                result()
            elif num == 2:
                if b2["text"] == " ":
                    if turn == 1:
                        b2["text"] = "X"
                        player1.append(num)
                        turn = 2
                    elif turn == 2:
                        b2["text"] = "O"
                        player2.append(num)
                        turn = 1
                    flag += 1
                else:
                    showinfo("Tic-Tac-Toe", "Button already Clicked!")
                result()
            elif num == 3:
                if b3["text"] == " ":
                    if turn == 1:
                        b3["text"] = "X"
                        player1.append(num)
                        turn = 2
                    elif turn == 2:
                        b3["text"] = "O"
                        player2.append(num)
                        turn = 1
                    flag += 1
                else:
                    showinfo("Tic-Tac-Toe", "Button already Clicked!")
                result()
            elif num == 4:
                if b4["text"] == " ":
                    if turn == 1:
                        b4["text"] = "X"
                        player1.append(num)
                        turn = 2
                    elif turn == 2:
                        b4["text"] = "O"
                        player2.append(num)
                        turn = 1
                    flag += 1
                else:
                    showinfo("Tic-Tac-Toe", "Button already Clicked!")
                result()
            elif num == 5:
                if b5["text"] == " ":
                    if turn == 1:
                        b5["text"] = "X"
                        player1.append(num)
                        turn = 2
                    elif turn == 2:
                        b5["text"] = "O"
                        player2.append(num)
                        turn = 1
                    flag += 1
                else:
                    showinfo("Tic-Tac-Toe", "Button already Clicked!")
                result()
            elif num == 6:
                if b6["text"] == " ":
                    if turn == 1:
                        b6["text"] = "X"
                        player1.append(num)
                        turn = 2
                    elif turn == 2:
                        b6["text"] = "O"
                        player2.append(num)
                        turn = 1
                    flag += 1
                else:
                    showinfo("Tic-Tac-Toe", "Button already Clicked!")
                result()
            elif num == 7:
                if b7["text"] == " ":
                    if turn == 1:
                        b7["text"] = "X"
                        player1.append(num)
                        turn = 2
                    elif turn == 2:
                        b7["text"] = "O"
                        player2.append(num)
                        turn = 1
                    flag += 1
                else:
                    showinfo("Tic-Tac-Toe", "Button already Clicked!")
                result()
            elif num == 8:
                if b8["text"] == " ":
                    if turn == 1:
                        b8["text"] = "X"
                        player1.append(num)
                        turn = 2
                    elif turn == 2:
                        b8["text"] = "O"
                        player2.append(num)
                        turn = 1
                    flag += 1
                else:
                    showinfo("Tic-Tac-Toe", "Button already Clicked!")
                result()
            elif num == 9:
                if b9["text"] == " ":
                    if turn == 1:
                        b9["text"] = "X"
                        player1.append(num)
                        turn = 2
                    elif turn == 2:
                        b9["text"] = "O"
                        player2.append(num)
                        turn = 1
                    flag += 1
                else:
                    showinfo("Tic-Tac-Toe", "Button already Clicked!")
                result()

        def reset():
            global flag, player1, player2, turn
            b1["text"] = " "
            b2["text"] = " "
            b3["text"] = " "
            b4["text"] = " "
            b5["text"] = " "
            b6["text"] = " "
            b7["text"] = " "
            b8["text"] = " "
            b9["text"] = " "
            flag = 0
            player1 = []
            player2 = []
            turn = 1

        b1 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(1))
        b1.grid(row=0, column=0)
        b2 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(2))
        b2.grid(row=0, column=1)
        b3 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(3))
        b3.grid(row=0, column=2)
        b4 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(4))
        b4.grid(row=1, column=0)
        b5 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(5))
        b5.grid(row=1, column=1)
        b6 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(6))
        b6.grid(row=1, column=2)
        b7 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(7))
        b7.grid(row=2, column=0)
        b8 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(8))
        b8.grid(row=2, column=1)
        b9 = Button(self, text=" ", bg="light gray", fg="black", width=8, height=4, command=lambda: set(9))
        b9.grid(row=2, column=2)

        res = Button(self, text="Reset", bg="gray", fg="black", width=8, height=3, command=lambda: reset())
        res.grid(row=3, column=1)
        home = Button(self, text="Home page", bg="gray", fg="black", width=8, height=3,
                      command=lambda: controller.show_frame("StartPage"))
        home.grid(row=3, column=2)
        comp = Button(self, text="vs Computer", bg="gray", fg="black", width=8, height=3,
                      command=lambda: controller.show_frame("Computer"))
        comp.grid(row=3, column=0)


# ---------------------vs player window end-------------------

if __name__ == "__main__":
    app = TicTac()
    app.mainloop()
