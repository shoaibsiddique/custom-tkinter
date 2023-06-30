import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

app.title("My First Button GUI")
app.geometry("500x300")

def button_function():
    print("Button Pressed")


button = customtkinter.CTkButton(master=app, text="Hello Button", command=button_function)
button.place(relx=0.5, rely=0.8, anchor = tkinter.CENTER)

app.mainloop()