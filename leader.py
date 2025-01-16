import customtkinter as ctk
import tkinter as tk
from PIL import Image,ImageTk
import tkinter.messagebox as msg
import mysql.connector as mycon

class LeaderBoard(ctk.CTk):
    def __init__(self,parent_frame,add_frame,navigate_frame,newtitle):
        super().__init__()
        self.parent_frame = parent_frame
        self.add_frame_method = add_frame
        self.navigate_frame_method = navigate_frame
        self.newtitle = newtitle

        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry('{}x{}+{}+{}'.format(self.width,self.height,-10,-5))
        self.title(self.newtitle)
        #self.config(bg="#ffbe0b")

        self.leader_frame = ctk.CTkFrame(self.parent_frame,fg_color="#ffbe0b")
        self.leader_frame.pack(fill = "both",expand = True)

        self.add_frame_method("leaderboard",self.leader_frame)

        self.back_image = ctk.CTkImage(light_image=Image.open(f"images/arrow.png"), dark_image=Image.open(f"images/arrow.png"), size=(16, 16))
    
        self.back_button = ctk.CTkButton(self.leader_frame,corner_radius = 100,image=self.back_image,hover="disabled",fg_color = "transparent" , bg_color="transparent",text = "Back to Home",text_color = "black",font = ctk.CTkFont(family = "Helvetica",weight = "normal",size = 15), command = self.navigate_to_home)
        self.back_button.pack(side = "top",anchor = "w", pady = 10, padx = 10)

        
        self.leader_lbl = ctk.CTkLabel(self.leader_frame,text = "LEADER BOARD",text_color="#000000",fg_color="#ffbe0b",font = ctk.CTkFont(family = "Impact",size = 45,weight = "normal"))
        self.leader_lbl.pack(side = "top",anchor = "center", pady = (50, 0))



        self.scroll_frame = ctk.CTkScrollableFrame(self.leader_frame,corner_radius=0,border_width=1,border_color="#000000",fg_color="#ffffff",bg_color="#ffbe0b",scrollbar_fg_color="lightgray",scrollbar_button_hover_color="gray",orientation="vertical")
        self.scroll_frame.pack(fill = "both", expand = True,padx = (25,25),pady = (60,60))




        # self.text_frame = ctk.CTkFrame(self.main_frame,fg_color="#ffffff")
        # self.text_frame.pack(fill = "x",padx = (25,25),pady = (10,0))

        # self.date_lbl = ctk.CTkLabel(self.text_frame,text="Date",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        # self.date_lbl.place(x = 50,y = 50)

        # self.rank_lbl = ctk.CTkLabel(self.text_frame,text="Rank",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        # self.rank_lbl.place(x = 270,y = 50)

        # self.name_lbl = ctk.CTkLabel(self.text_frame,text="Name",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        # self.name_lbl.place(x = 500,y = 50)

        # self.score_lbl = ctk.CTkLabel(self.text_frame,text="Score",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        # self.score_lbl.place(x = 770,y = 50)

        # self.time_lbl = ctk.CTkLabel(self.text_frame,text="Time",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        # self.time_lbl.place(x = 1050,y = 50)

        column_widths = {
                "RANK":300,
                "NAME":300,
                "SCORE": 300,
                "TIME":300,
                "DATE":300 
            }
        
        column_list = ["RANK","NAME","SCORE","TIME","DATE"]
        for i ,col in enumerate(column_list):
            column_var = tk.StringVar(value = col)
            width = column_widths.get(col, 250)
            column_box = ctk.CTkEntry(self.scroll_frame, font = ("Helvetica", 17), border_width=1,border_color = "black", width = width, height = 40, textvariable=column_var,corner_radius=0, justify = "center", state = "readonly", fg_color="#176B87",text_color="white")
            column_box.grid(row = 0, column = i)

        
        self.populate_leaderboard()

    
    def get_data(self):
        try:
            con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "quiz_app")
            cur = con.cursor()
            select_query = "select name, score, time, date(edate) from leaderboard order by score desc"
            
            cur.execute(select_query)
            results  = cur.fetchall()

            return results
        
        except Exception as e:
            print("Error : ", e)
        finally:
            con.close()

    def populate_leaderboard(self):
        leader_data = self.get_data()
        name_list = []
        score_list = []
        time_list = []
        date_list = []
        for i in leader_data:
            name_list.append(i[0])
            score_list.append(i[1])
            time_list.append(i[2])
            date_list.append(i[3])

        if not leader_data:
            no_data_label = ctk.CTkLabel(
                self.scroll_frame,
                text="No data available",
                text_color="#000000",
                font=ctk.CTkFont(family="Helvetica", size=20, weight="bold"),
            )
            no_data_label.grid(row=1, column=0, columnspan=5, pady=20)
            return

        for i, entry in enumerate(leader_data):
            rank = tk.StringVar(value = f"{i + 1}")
            name = tk.StringVar(value = name_list[i])
            score = tk.StringVar(value = score_list[i])
            time = tk.StringVar(value = time_list[i])
            date = tk.StringVar(value = date_list[i])
        
        row_data = [rank, name, score, time, date]
        column_width = [300, 300, 300, 300, 270]

        for i, data in enumerate(name_list):
            rank_var = tk.StringVar(value = i+1)
            rank_box = ctk.CTkEntry(self.scroll_frame, font = ("Helvetica", 15), width = 300, height = 40, textvariable=rank_var,corner_radius=0, justify = "center", state = "readonly", fg_color="#e5e5e5",text_color="black")
            rank_box.grid(row = i + 1 , column = 0)

        for i, name_file in enumerate(name_list):
            name_var = tk.StringVar(value = name_file)
            name_box = ctk.CTkEntry(self.scroll_frame, font = ("Helvetica", 15), width = 300, height = 40, textvariable=name_var,corner_radius=0, justify = "center", state = "readonly", fg_color="#e5e5e5",text_color="black")
            name_box.grid(row = i + 1 , column = 1)

        for i, score_file in enumerate(score_list):
            score_var = tk.StringVar(value = score_file)
            score_box = ctk.CTkEntry(self.scroll_frame, font = ("Helvetica", 15), width = 300, height = 40, textvariable=score_var,corner_radius=0, justify = "center", state = "readonly", fg_color="#e5e5e5",text_color="black")
            score_box.grid(row = i + 1 , column = 2)

        for i, time_file in enumerate(time_list):
            time_var = tk.StringVar(value = time_file)
            time_box = ctk.CTkEntry(self.scroll_frame, font = ("Helvetica", 15), width = 300, height = 40, textvariable=time_var,corner_radius=0, justify = "center", state = "readonly", fg_color="#e5e5e5",text_color="black")
            time_box.grid(row = i + 1 , column = 3)

        for i, date_file in enumerate(date_list):
            date_var = tk.StringVar(value = date_file)
            date_box = ctk.CTkEntry(self.scroll_frame, font = ("Helvetica", 15), width = 300, height = 40, textvariable=date_var,corner_radius=0, justify = "center", state = "readonly", fg_color="#e5e5e5",text_color="black")
            date_box.grid(row = i + 1 , column = 4)
        
    def navigate_to_home(self):
        self.navigate_frame_method("leaderboard","homepage")



# leader = LeaderBoard()
# leader.mainloop()
