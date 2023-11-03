import tkinter as tk
import random
import string

def generate_password():
    length = int(entry_length.get())
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    label_password.config(text="Generated Password: " + password)

window = tk.Tk()
window.title("Password Generator")

label_length = tk.Label(window, text="Password Length:")
label_length.pack()
entry_length = tk.Entry(window)
entry_length.pack()

button_generate = tk.Button(window, text="Generate Password", command=generate_password)
button_generate.pack()

label_password = tk.Label(window, text="Generated Password:")
label_password.pack()

window.configure(bg="#f0f0f0")

window.mainloop()
