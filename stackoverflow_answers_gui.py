from tkinter import *
from sotrace import get_links

root = Tk()
root.iconbitmap('./logo.ico')
answer_get = StringVar()
win_width = 800
win_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
start_x = int(screen_width / 2 - win_width / 2)
start_y = int(screen_height / 2 - win_height / 2)

def navigator():
    root.title("Stackoverflow Answers Gui")
    root.geometry("{}x{}+{}+{}".format(win_width, win_height, start_x, start_y))
    root.resizable(False, False)
    root.configure(bg="#EC882E")

def heading():
    text = "You Can Know Everything"
    font = ("Microsoft YaHei", 18, "bold")
    head_label = Label(root, text=text, font=font, fg="#000000", bg="#EC882E", pady=20)
    head_label.pack()

def your_question():
    text = "Your Questions:"
    font = ("Microsoft Yahei", 10, "bold")
    question_label = Label(root, text=text, font=font, fg="#000000", bg="#EC882E")
    question_label.place(relx=0.05, rely=0.3)

def your_question_content():
    font = ("Microsoft Yahei", 10, "bold")
    text_content = Entry(root, width=65, textvariable=answer_get, font=font, fg="#00FF00", bg="#000000")
    text_content.place(relx=0.2, rely=0.31)
def bingo_button(*args):
    text = "Bingo"
    font = ("Microsoft Yahei", 10, "bold")
    bingo_btn = Button(root, width=6, height=1, text=text, font=font, fg="#ff0000", command=show_answer)
    bingo_btn.place(relx=0.88, rely=0.3)

def show_answer_label():
    text = "Select Answers:"
    font = ("Microsoft Yahei", 10, "bold")
    question_label = Label(root, text=text, font=font, fg="#000000", bg="#EC882E")
    question_label.place(relx=0.05, rely=0.43)

def show_answer():
    str = ""
    for i in get_links("{}.".format(answer_get.get()), num_of_results=100):
        str += i + "\n"
    font = ("Microsoft Yahei", 10)
    answers = Text(root, height=8, width=90, font=font, fg="#00FF00", bg="#000000")
    answers.insert(END, str)
    answers.configure(state="disabled")
    answers.place(relx=0.05, rely=0.5)

def main():
    navigator()
    heading()
    bingo_button()
    show_answer()
    your_question()
    your_question_content()
    show_answer_label()
    root.mainloop()
    
if __name__ == "__main__":
    main()