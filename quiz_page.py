import customtkinter as ctk 
import tkinter as tk
from PIL import Image,ImageTk
import json


class QuizPage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()        
        self.geometry('{}x{}+{}+{}'.format(self.width,self.height,-10,0))
        self.title("Quiz App")
        self.config(bg="#ffbe0b")


        self.questions = self.load_questions()
        self.current_question = 0
        self.score = 0
        self.time_limit = 10
        self.remaining_time = self.time_limit
        self.selected_option = None

        self.create_widgets()
        self.start_timer()

    def load_questions(self):
        try:
            with open("questions.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: questions.json file not found.")
            return[]
    
    def load_question(self):
        if not self.questions:
            return

        current_question = self.questions[self.current_question]
        self.question_label.configure(text = current_question["question"])
        self.question_number_label.configure(text=f"Question {self.current_question + 1}")

        try:
            img = ctk.CTkImage(light_image=Image.open(current_question["image"]), dark_image=Image.open(current_question["image"]), size=(350, 350))
            self.image_label.configure(image = img)
            self.image_label.image = img
        except FileNotFoundError:
            self.image_label.configure(image = None)

        for i, option in enumerate(current_question["options"]):
            
            option_image = ctk.CTkImage(light_image=Image.open(f"images/number-{i+1}.png"), dark_image=Image.open(f"images/number-{i+1}.png"), size=(20, 20))
    
            self.option_buttons[i].configure(image = option_image, text=f"{option}", fg_color="#70d6ff", text_color="#003049", border_color="#390099",compound = "left",width=300,height = 40)

            # Reset button appearance and state
            if i == self.selected_option: 
                self.option_buttons[i].configure(fg_color="#70d6ff", text_color="#003049", border_color="#390099",width=300,height = 40) 

        for button in self.option_buttons:
            button.configure(state = tk.NORMAL)
        
        self.selected_option = None
        
        # Update next button
        if self.current_question == len(self.questions) - 1:
            self.next_button.configure(text = "SUBMIT", command = self.end_quiz)
        else:
    
            self.next_button.configure(text = "NEXT", command = self.next_question)
    
    def next_question(self):
        self.current_question += 1
        if self.current_question >= len(self.questions):
            self.end_quiz()
        else:
            self.load_question()

    def check_answer(self,selected_option):
        self.selected_option = selected_option
        correct_answer_index = self.questions[self.current_question]["answer"]

        if selected_option == self.questions[self.current_question]["answer"]:
            self.score +=1
            self.option_buttons[selected_option].configure(fg_color = "green", text_color = "white", border_color = "white",width=300,height = 40)
        else:
            self.option_buttons[selected_option].configure(fg_color = "red", text_color = "white", border_color = "white",width=300,height = 40)
            self.option_buttons[correct_answer_index].configure(fg_color="green", text_color="white", border_color="white",width=300,height = 40) 

        for button in self.option_buttons:
            button.configure(state = tk.DISABLED)

    def create_widgets(self):
        self.question_frame = ctk.CTkFrame(self, width = 1300, height = 800, fg_color="#003049", bg_color="#ffbe0b")

        self.question_label = ctk.CTkLabel(self.question_frame, text="Hello", font = ("Helvetica", 20))
        self.question_label.place(x = 700, y = 150)

        self.image_label = ctk.CTkLabel(self.question_frame, text = "")
        self.image_label.place(x = 150, y = 150)

        self.question_number_label = ctk.CTkLabel(self.question_frame, text=f"", font=("Arial", 20, "bold"))
        self.question_number_label.place(x = 20, y = 20)

        self.option_buttons = []
        for i in range(4):
            button = ctk.CTkButton(self.question_frame, text = "", width=300,height = 40, command = lambda i = i: self.check_answer(i), corner_radius=10,border_width = 2,border_color = "#390099", font=("Verdana Pro", 18), fg_color="#70d6ff", text_color="#003049", hover_color="#ff70a6")
            button.place(x = 700, y = 230 + i * 70)
            self.option_buttons.append(button)

        self.timer_label = ctk.CTkLabel(self.question_frame, text=f"Time Left: {self.time_limit}", font=("Arial", 20, "bold"))
        self.timer_label.place(x = 1150, y = 20)
        
        self.next_button = ctk.CTkButton(self.question_frame, text="NEXT", command=self.next_question, height=38, width=150, corner_radius=10, font=("Arial", 20, "bold"), border_width=2, border_color="#ffb703", fg_color="#f77f00", text_color="black", hover_color="#ffbf69")
        self.next_button.place(x = 1120, y = 580)
    
        self.question_frame.pack(anchor = "center", pady = 100)

        self.load_question()

    def start_timer(self):
        self.timer_label.configure(text=f"Time Left: {self.remaining_time}")
        if(self.remaining_time > 0):
            self.after(1000, self.update_timer)
        else:
            # self.next_question()
            self.end_quiz()

    def update_timer(self):
        self.remaining_time -= 1
        self.timer_label.configure(text = f"Time Left: {self.remaining_time}")
        if(self.remaining_time > 0):
            self.after(1000, self.update_timer)
        else:
            # self.next_question()
            self.end_quiz()

    def end_quiz(self):
        self.withdraw()

        result_window = ctk.CTkToplevel()
        result_window.geometry("200x200")
        result_window.title("Quiz Results")

        self.result_label = ctk.CTkLabel(result_window, text=f"Quiz Over!\nYour Score: {self.score}", font=("Arial", 24, "bold"))
        self.result_label.pack(pady=50)

        # print(f"Quiz Over! Your Score: {self.score}")

if __name__ == "__main__":
    root = QuizPage()
    root.mainloop()