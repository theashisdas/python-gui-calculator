from tkinter import *

# Create Main window 
root = Tk()
root.title("Simple Calculator by Ashis Das")
root.geometry("300x500")

# Display box 
entry = Entry(root, font=("Arial", 20), bd=5, relief=RIDGE)
entry.grid(row=0, column=0, columnspan=3, pady=10)

# Show value on display when button is clicked
def click(value):
    entry.insert(END, value)

# Clear all text from display (AC)
def all_clear():
    entry.delete(0, END)

# Delete last character from display (DEL)
def delete_one():
    current_text = entry.get()
    entry.delete(0, END)
    entry.insert(0, current_text[:-1])

# Result value (=)
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# [3 x 7] Buttons 

# Row 1 [Buttons : AC, DEL, =]
Button(root, text="AC", width=10, height=2, command=all_clear).grid(row=1, column=0)
Button(root, text="DEL", width=10, height=2, command=delete_one).grid(row=1, column=1)
Button(root, text="=", width=10, height=2, command=calculate).grid(row=1, column=2)

# Row 2 [Buttons : (, ), %]
Button(root, text="(", width=10, height=2, command=lambda: click("(")).grid(row=2, column=0)
Button(root, text=")", width=10, height=2, command=lambda: click(")")).grid(row=2, column=1)
Button(root, text="%", width=10, height=2, command=lambda: click("%")).grid(row=2, column=2)

# Row 3 [Buttons : 7, 8, 9]
Button(root, text="7", width=10, height=2, command=lambda: click("7")).grid(row=3, column=0)
Button(root, text="8", width=10, height=2, command=lambda: click("8")).grid(row=3, column=1)
Button(root, text="9", width=10, height=2, command=lambda: click("9")).grid(row=3, column=2)

# Row 4 [Buttons : 4, 5, 6]
Button(root, text="4", width=10, height=2, command=lambda: click("4")).grid(row=4, column=0)
Button(root, text="5", width=10, height=2, command=lambda: click("5")).grid(row=4, column=1)
Button(root, text="6", width=10, height=2, command=lambda: click("6")).grid(row=4, column=2)

# Row 5 [Buttons : 1, 2, 3]
Button(root, text="1", width=10, height=2, command=lambda: click("1")).grid(row=5, column=0)
Button(root, text="2", width=10, height=2, command=lambda: click("2")).grid(row=5, column=1)
Button(root, text="3", width=10, height=2, command=lambda: click("3")).grid(row=5, column=2)

# Row 6 [Buttons : 0 , . , +]
Button(root, text="0", width=10, height=2, command=lambda: click("0")).grid(row=6, column=0)
Button(root, text=".", width=10, height=2, command=lambda: click(".")).grid(row=6, column=1)
Button(root, text="+", width=10, height=2, command=lambda: click("+")).grid(row=6, column=2)

# Row 7 [Buttons : - , * , /]
Button(root, text="-", width=10, height=2, command=lambda: click("-")).grid(row=7, column=0)
Button(root, text="*", width=10, height=2, command=lambda: click("*")).grid(row=7, column=1)
Button(root, text="/", width=10, height=2, command=lambda: click("/")).grid(row=7, column=2)

# Keep the program running
root.mainloop()
