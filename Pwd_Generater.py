import random, string
from tkinter import *
import pyperclip

def randPassGen():
    password = "" 
    for y in range(pass_len.get()-2):
        char_type = random.choice(all_combi)   
        password = password + random.choice(char_type)
    password = password + random.choice(string.digits) + random.choice(string.punctuation)
    output_pass.set(password)

def copyPass():
    pyperclip.copy(output_pass.get())
  
root =Tk()
root.geometry("400x400") 
root.configure(background="misty rose")
root.title("Random Password Generator")
root.resizable(width=False, height=False)
output_pass = StringVar()
all_combi = [string.ascii_uppercase, string.ascii_lowercase]  
pass_head = Label(root, bg="misty rose",text = 'Password Length', font=("Helvetica", 15, "bold"), pady=10).pack(pady=10) 
pass_len = IntVar()
length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len , width = 24, bd=5, font="Roboto 11").pack()
BUTTON1=Button(root,bg="deepskyblue", bd=5, command = randPassGen, text = "Generate Password", font=("Helvetica", 12, "bold"), fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
pass_label = Label(root, bg="misty rose", text = 'Random Generated Password', font =("Helvetica", 15, "bold"), pady=10).pack(pady="30 10")
Entry(root , textvariable = output_pass, width = 24, bd=5, font="Roboto 11").pack()
BUTTON2=Button(root,bg="deepskyblue", bd=5, text = 'Copy to Clipboard', command = copyPass, font=("Helvetica", 12, "bold"), fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
root.mainloop()  