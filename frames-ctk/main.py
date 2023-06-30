import tkinter
import customtkinter
from functions import button_function1, button_function2

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


app = customtkinter.CTk()
app.geometry("400x240")

frame = customtkinter.CTkFrame(master = app, 
                               width=200,
                               height=200,
                               corner_radius=20,
                               bg_color="white")

frame.pack(padx=20, pady=20)

button1 = customtkinter.CTkButton(master = frame, text="Button_1", command= button_function1)
button1.place(relx=0.5, rely=0.3, anchor = tkinter.CENTER)

button2 = customtkinter.CTkButton(master = frame, text="Button_2", command= button_function2)
button2.place(relx=0.5, rely=0.7, anchor = tkinter.CENTER)

app.mainloop()