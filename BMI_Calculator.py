from tkinter import *
from tkinter import messagebox

def get_weight():
    weight = float(ENTRY1.get())
    return weight

def get_height():
    height = float(ENTRY2.get())
    return height

def calculate_bmi(a=""):   
    print(a)
    try:
        height = get_height()
        weight = get_weight()
        if 0<height and 0<weight:
            height = height / 100.0
            bmi = weight / (height ** 2)
            bmi = round(bmi, 2)
        else:
            messagebox.showinfo("Result", "Please Enter Positive Height And Weight!!")
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please Enter Positive Height!")
    except ValueError:
        messagebox.showinfo("Result", "Please Enter Valid Data!")
    else:
        if 0 < bmi <= 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
            messagebox.showinfo("Result", res)
        elif 18.5 <= bmi < 25.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Normal Weight."
            messagebox.showinfo("Result", res)
        elif 25.0 <= bmi < 30:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Obese!"
            messagebox.showinfo("Result", res)


if __name__ == '__main__':
    root = Tk()
    root.bind("<Return>", calculate_bmi)
    root.geometry("360x270")
    root.configure(background="misty rose")
    root.title("BMI Calculator")
    root.resizable(width=False, height=False)
    LABLE = Label(root, bg="misty rose", text="Welcome to BMI Calculator", font=("Helvetica", 15, "bold"), pady=10)
    LABLE.place(x=50, y=8)
    LABLE1 = Label(root, bg="misty rose", text="Enter Weight (in kg) :", bd=6,font=("Helvetica", 10, "bold"), pady=5)
    LABLE1.place(x=65, y=62)
    ENTRY1 = Entry(root, bd=5, width=6, font="Roboto 11")
    ENTRY1.place(x=235, y=66)
    LABLE2 = Label(root, bg="misty rose", text="Enter Height (in cm) :", bd=6,font=("Helvetica", 10, "bold"), pady=5)
    LABLE2.place(x=65, y=122)
    ENTRY2 = Entry(root, bd=5, width=6, font="Roboto 11")
    ENTRY2.place(x=235, y=126)
    BUTTON = Button(bg="deepskyblue", bd=5, text="Calculate",width=10, command=calculate_bmi, fg='black', activebackground="teal", font=("Helvetica", 15, "bold"))
    BUTTON.grid(row=2, column=0, sticky=W)
    BUTTON.place(x=110, y=190)
    root.mainloop()