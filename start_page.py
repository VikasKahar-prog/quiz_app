import tkinter as tk
import customtkinter as ctk
from PIL import Image,ImageTk
from quiz_page import QuizPage
import json
import time
import os

class CountdownPage(ctk.CTk):
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
        #self.config(bg="#222222")

        self.start_page = ctk.CTkFrame(self.parent_frame,bg_color="#222222")
        self.start_page.pack(fill = "both",expand = True)

        self.add_frame_method("startpage",self.start_page)

        self.background_image = ctk.CTkImage(
                light_image=Image.open("images/quiz_background.png"), 
                dark_image=Image.open("images/quiz_background.png"),
                size=(self.width, self.height)
            )
        
        self.background_label = ctk.CTkLabel(self.start_page, image=self.background_image)
        self.background_label.pack(fill = tk.BOTH, expand = True)
        
        try:
            
            self.gif_path = "gif/countdown.gif"
            self.gif = Image.open(self.gif_path)

            self.frame = ctk.CTkFrame(self.start_page, width = 400, height = 300, fg_color="#0f4c5c", bg_color="#f3de2c", border_width=2, border_color="#0f4c5c")
            self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            self.gif_canvas = tk.Canvas(self.frame, width=400, height=300, highlightthickness=0, bg="#f3de2c")
            self.gif_canvas.pack(padx=10, pady=10)

            self.label = ctk.CTkLabel(self.frame, text = "Your Quiz Will Start in", font = ("Open Sans", 22), text_color="black", fg_color="#f3de2c")
            self.label.place(x = 60, y =30)

            self.gif_image = ImageTk.PhotoImage(self.gif.copy())
            self.gif_id = self.gif_canvas.create_image(200, 180, image=self.gif_image, anchor=tk.CENTER)

            self.frame_count = 0
            self.start_time = time.time()
            self.animate_gif() 

        except FileNotFoundError:
            print("GIF file not found.")

    def animate_gif(self):
        try:
        
            self.gif.seek(self.gif.tell() + 1)
            self.gif_image = ImageTk.PhotoImage(self.gif.copy())
            self.gif_canvas.itemconfig(self.gif_id, image=self.gif_image)
            self.frame_count += 1

            if (time.time() - self.start_time<4):
                self.after(25, self.animate_gif)
            else:
                quiz_page_object = QuizPage(self.parent_frame,self.add_frame_method,self.navigate_frame_method,"Quiz Page")
                self.navigate_frame_method("startpage","quizpage")

        except EOFError:
            pass
'''
if __name__ == "__main__":
    quiz_timer = CountdownPage()
    quiz_timer.mainloop()'''