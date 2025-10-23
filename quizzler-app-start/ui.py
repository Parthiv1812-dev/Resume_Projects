from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250,  bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="text", fill=THEME_COLOR, font=("Ariel", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        tick_image = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=tick_image, highlightthickness=0, bg=THEME_COLOR, command=self.check_true)
        self.tick_button.grid(row=2, column=0)
        cross_image = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_image, highlightthickness=0, bg=THEME_COLOR, command=self.check_false)
        self.cross_button.grid(row=2, column=1)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")


    def check_true(self):
       is_right  = self.quiz.check_answer("true")
       self.give_feedback(is_right)

    def check_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def change_bg_color_white(self):
        self.canvas.configure(bg="white")


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
            self.window.after(1000, lambda: [self.change_bg_color_white(), self.get_next_question()])


        else:
            self.canvas.configure(bg="red")
            self.window.after(1000, lambda: [self.change_bg_color_white(), self.get_next_question()])






