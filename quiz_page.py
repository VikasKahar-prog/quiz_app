import customtkinter as ctk 
import tkinter as tk
from PIL import Image,ImageTk
from popup import PopUp
import json


class QuizPage(ctk.CTk):
    def __init__(self,parent_frame,add_frame,navigate_frame,newtitle):
        super().__init__()
        self.parent_frame = parent_frame
        self.add_frame_method = add_frame
        self.navigate_frame_method = navigate_frame
        self.newtitle = newtitle

        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()        
        self.geometry('{}x{}+{}+{}'.format(self.width,self.height,-10,0))
        self.title(self.newtitle)
        #self.config(bg="#ffbe0b")

        self.quiz_page = ctk.CTkFrame(self.parent_frame,fg_color="#ffbe0b")
        self.quiz_page.pack(fill = "both",expand = True)

        self.add_frame_method("quizpage",self.quiz_page)

        self.questions = self.load_questions()
        self.current_question = 0
        self.score = 0
        self.time_limit = 60
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
        self.question_frame = ctk.CTkFrame(self.quiz_page, width = 1300, height = 800, fg_color="#003049", bg_color="#ffbe0b")

        self.question_label = ctk.CTkLabel(self.question_frame, text="", font = ("Helvetica", 20), text_color="white")
        self.question_label.place(x = 700, y = 100)

        self.image_label = ctk.CTkLabel(self.question_frame, text = "")
        self.image_label.place(x = 150, y = 100)

        self.question_number_label = ctk.CTkLabel(self.question_frame, text=f"", font=("Arial", 20, "bold"), text_color="white")
        self.question_number_label.place(x = 20, y = 20)

        self.option_buttons = []
        for i in range(4):
            button = ctk.CTkButton(self.question_frame, text = "", width=300,height = 40, command = lambda i = i: self.check_answer(i), corner_radius=10,border_width = 2,border_color = "#390099", font=("Verdana Pro", 18), fg_color="#70d6ff", text_color="#003049", hover_color="#ff70a6")
            button.place(x = 700, y = 180 + i * 70)
            self.option_buttons.append(button)

        self.timer_label = ctk.CTkLabel(self.question_frame, text=f"Time Left: {self.remaining_time}", font=("Arial", 20, "bold"), text_color="white")
        self.timer_label.place(x = 1150, y = 20)
        
        
        self.next_button = ctk.CTkButton(self.question_frame, text = "NEXT", width=150, height=38, corner_radius=10, font=("Arial", 20, "bold"), border_width=2,  border_color="#ffffff",fg_color="#ffb703", text_color="black", hover_color="#ffbf69",command=self.next_question)
        self.next_button.place(x = 1120, y = 490)
    
        self.question_frame.pack(anchor = "center", pady = 100)

        self.load_question()

    def start_timer(self):
        #print(self.remaining_time)
        self.timer_label.configure(text=f"Time Left: {self.remaining_time}")
        if(self.remaining_time > 0):
           # print(self.remaining_time)
            self.after(1000, self.update_timer)
        else:
            self.end_quiz()

    def update_timer(self):
        self.remaining_time -= 1
        self.start_timer()

    def end_quiz(self):
        self.quiz_page.configure(fg_color = "transparent")
        self.overlay = ctk.CTkFrame(self.quiz_page, fg_color="transparent", corner_radius=0)
        self.overlay.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.next_button.configure(state = "disabled")
        self.result_window = ctk.CTkToplevel()
        self.result_window.title("Quiz Results")
        self.result_window.configure(fg_color = "#ffbe0b")
        self.result_window.overrideredirect(True)

        self.width = 600
        self.height = 300
        self.result_window.geometry('{}x{}+{}+{}'.format(self.width,self.height,400,200))

        self.popup_frame = ctk.CTkFrame(self.result_window,fg_color="transparent")
        self.popup_frame.pack(anchor = "center")

        #self.add_frame_method("popup",self.popup_frame)

        # self.mainframe = ctk.CTkFrame(result_window,border_width=1,border_color="#ffffff",fg_color="#edede9",bg_color="#edede9")
        # self.mainframe.pack(fill = "both",expand = True,anchor = "center",pady = 10,padx = 10)
        
        self.message_val = tk.StringVar()
        self.message_val.set("Congratulations")
        self.message_lbl = ctk.CTkLabel(self.popup_frame,textvariable = self.message_val,fg_color="transparent",font = ctk.CTkFont(family="Tahoma",size=30,weight="bold"))
        self.message_lbl.pack(side = "top",anchor = "center",pady = 20)

        self.score_lbl = ctk.CTkLabel(self.popup_frame,text="Your Score is:",fg_color="transparent",font = ctk.CTkFont(family="Arial",size=20,weight="normal"))
        self.score_lbl.pack(anchor = "center",pady = 10)
        
        self.score_val = tk.StringVar()
        self.score_val.set("80") 
        self.score_val = ctk.CTkLabel(self.popup_frame,textvariable = self.score_val,fg_color="transparent",font = ctk.CTkFont(family="Helvetica",size=40,weight="bold"))
        self.score_val.pack(anchor = "center",pady = 10)

        home_image = ctk.CTkImage(dark_image=Image.open(r'images/home.png'),size = (20,20))

        self.homebutton = ctk.CTkButton(self.popup_frame,corner_radius = 100,image=home_image,hover="disabled",fg_color = "#29B6F6",text = "Back to Home",text_color = "black",font = ctk.CTkFont(family = "Helvetica",weight = "normal",size = 15),command=self.go_to_home)
        self.homebutton.pack(side = "bottom",anchor = "center",pady = 40,ipadx = 10,ipady = 10)

        # self.quiz_page.configure(state = "disabled")

    def go_to_home(self):
        self.navigate_frame_method("quizpage","homepage")
        self.result_window.destroy()

        # self.result_label = ctk.CTkLabel(result_window, text=f"Quiz Over!\nYour Score: {self.score}", font=("Arial", 24, "bold"))
        # self.result_label.pack(pady=50)

        # popup_object = PopUp(self.parent_frame,self.add_frame_method,self.navigate_frame_method,"PopUp Window")
        # self.navigate_frame_method("quizpage","popup")


        # print(f"Quiz Over! Your Score: {self.score}")
'''
if __name__ == "__main__":
    root = QuizPage()
    root.mainloop()'''
