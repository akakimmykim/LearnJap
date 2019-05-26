import random
from tkinter import*

questions = [] # list to hold questions
answers = [] # list to hold answers
qlist = []
alist = [] # list to hold randomized answers
q = ""
a = ""

# open the eng_to_hiragana file and save into an array
qfile = open("etoHQs.txt", "r")
afile = open("etoHAns.txt", "r", encoding="utf8")
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

# function for button
def nextQ():
    q = qlist[-1]
    qlist.pop()
    askQ.delete('1.0', END)
    askQ.insert(END, q)
    askQ.tag_configure("center", justify='center')
    askQ.tag_add("center", 1.0, "end")

def displayAnswer():
    while len(qlist)+1 < len(alist):
        alist.pop()
    a = alist[-1]
    giveA.delete('1.0', END)
    giveA.insert(END, a)
    giveA.tag_configure("center", justify='center')
    giveA.tag_add("center", 1.0, "end")

#GUI for the program

root = Tk()
# set up question frame
askQ = Text(root, height=1, width=10, font=("Helvetica",100))
askQ.pack(side=TOP)
# set up answer frame
giveA = Text(root, height=1, width=10, font = ("Helvetica", 60))
giveA.pack(side=BOTTOM)
# set up question and answer button
nextQ()
next = Button(root, text="Next", command=nextQ, font=("Arial, 60"))
next.pack(side=LEFT)
check = Button(root, text="Check", command=displayAnswer, font=("Arial, 60"))
check.pack(side=RIGHT)

root.mainloop()





