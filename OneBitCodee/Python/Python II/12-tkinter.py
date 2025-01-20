import tkinter as tk

window = tk.Tk()

window.geometry("300x150")
window.title("Gerenciador de frases")


frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)


label = tk.Label(frame, text="Hello World")
label.pack(fill = 'x', expand=True)

frase_lab = tk.Label(frame, text='frase')
frase_lab.pack(fill ='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill = 'x', expand=True)

def click():
    label.config(text= frase_inp.get())

button = tk.Button(frame, text='enviar', command= click)
button.pack()
window.mainloop()




