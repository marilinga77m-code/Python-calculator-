from tkinter import *

# function to calculate sum
def calculate_sum():
    try:
        n1 = int(entry1.get())
        n2 = int(entry2.get())
        result.set("addition = " + str(n1 + n2))
    except:
        result.set("Enter valid numbers")

# function to clear inputs
def clear_all():
    entry1.delete(0, END)
    entry2.delete(0, END)
    result.set("")

# window
root = Tk()
root.title("Addition Program")
root.geometry("300x200")

# variables
result = StringVar()

# labels and input boxes
Label(root, text="Number 1").pack()
entry1 = Entry(root)
entry1.pack()

Label(root, text="Number 2").pack()
entry2 = Entry(root)
entry2.pack()

# buttons
Button(root, text="Sum", command=calculate_sum).pack(pady=5)
Button(root, text="Clear", command=clear_all).pack(pady=5)

# result display
Label(root, textvariable=result).pack()

# run window
root.mainloop()
