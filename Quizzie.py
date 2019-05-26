import random
from tkinter import*
from tkinter.filedialog import askopenfilename

questions = [] # list to hold questions
answers = [] # list to hold answers
qlist = [""]
alist = [""]  # list to hold randomized answers
q = ""
a = ""
qName = ""
aName = ""

def startQuizzie():

    # open the eng_to_hiragana file and save into an array
    qfile = open('%s' %qName, "r", encoding="utf8")
    afile = open('%s' %aName, "r", encoding="utf8")
    while True:
        q = qfile.readline()
        a = afile.readline()
        if not q:
            break
        questions.append(q)
        answers.append(a)

    # fill in another list with randomized hiragana and answers
    listL = len(questions)
    for x in range (listL):
        element = random.randint(0, len(questions)-1)
        qlist.append(questions[element])
        alist.append(answers[element])
        questions.remove(questions[element])
        answers.remove(answers[element])

    alist.pop(0) # remove stupid blank element error

    quizWindow() # open new window and begin quiz

# Choose File Option
def chooseFile(type):
    if type == "q":
        global qName
        qName = askopenfilename()
    elif type == "a":
        global aName
        aName = askopenfilename()

# Next Question Button and Display
def nextQ():
    q = qlist[-1]
    qlist.pop()
    askQ.delete('1.0', END)
    askQ.insert(END, q)
    askQ.tag_configure("center", justify='center')
    askQ.tag_add("center", 1.0, "end")

# Display Answer Button and Display
def displayAnswer():
    while len(qlist) < len(alist):
        alist.pop()
    a = alist[-1]
    giveA.delete('1.0', END)
    giveA.insert(END, a)
    giveA.tag_configure("center", justify='center')
    giveA.tag_add("center", 1.0, "end")

#GUI for the program
root = Tk()


# MAIN WINDOW
def quizWindow():
    window = Toplevel(root)
    # set up question frame
    global askQ, giveA
    askQ = Text(window, height=1, width=10, font=("Helvetica", 100))
    askQ.pack(side=TOP)
    # set up answer frame
    giveA = Text(window, height=1, width=10, font=("Helvetica", 60))
    giveA.pack(side=BOTTOM)
    # set up question and answer button
    nextQ()
    next = Button(window, text="Next", command=nextQ, font=("Arial, 60"))
    next.pack(side=LEFT)
    check = Button(window, text="Check", command=displayAnswer, font=("Arial, 60"))
    check.pack(side=RIGHT)


pickQfile = Button(root, text="Choose Question File", command=lambda: chooseFile("q"), font=("Arial, 30"))
pickAfile = Button(root, text="Choose Answer File", command=lambda: chooseFile("a"), font=("Arial, 30"))
start = Button(root, text="BEGIN TEST", command=lambda: startQuizzie(), font=("Arial, 60"))
pickQfile.grid(row=0, column=1, padx=5, pady=5)
pickAfile.grid(row=0, column=2, padx=5, pady=5)
start.grid(row=1, column=1, columnspan=2)


root.mainloop()





