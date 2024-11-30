
from tkinter import *
import tkinter.messagebox
from tkmacosx import Button
import math


root = Tk()
root.geometry("850x400+300+300")  # Adjusted width to accommodate columns
root.title("Scientific Calculator")
switch = None
history = []



# --- Functions ---
# Favorites Button Functions
def favorite1_clicked():
    tkinter.messagebox.showinfo("Favorite 1", "You clicked Favorite 1!")

def favorite2_clicked():
    tkinter.messagebox.showinfo("Favorite 2", "You clicked Favorite 2!")

def favorite3_clicked():
    tkinter.messagebox.showinfo("Favorite 3", "You clicked Favorite 3!")

# History Button Function
def history_clicked():

    history_window = Toplevel(root)
    history_window.title("History")
    history_window.geometry("400x400")  # Initial size

    # Function to insert clicked history item into the display
    def insert_to_display(item):
        disp.delete(0, END)
        disp.insert(0, item)

    # Add history items as buttons
    for i, (expression, result, function_type) in enumerate(history):
        function_btn = Button(history_window, text=f"{function_type}",
                              command=lambda exp=expression: insert_to_display(exp))
        expression_btn = Button(history_window, text=f"{expression}",
                                command=lambda exp=expression: insert_to_display(exp))
        result_btn = Button(history_window, text=str(result),
                            command=lambda res=result: insert_to_display(res))
        blank = Button(history_window, text="=", fg="white", bg="#0d1c2f", activebackground="#bf3956")

        # Pack or grid the buttons
        function_btn.grid(row=i, column=0, sticky="nsew")
        expression_btn.grid(row=i, column=1, sticky="nsew")
        blank.grid(row=i, column=2, sticky="nsew")
        result_btn.grid(row=i, column=3, sticky="nsew")

        # Configure columns to expand dynamically
        history_window.grid_columnconfigure(0, weight=1)
        history_window.grid_columnconfigure(1, weight=1)
        history_window.grid_columnconfigure(2, weight=1)
        history_window.grid_columnconfigure(3, weight=1)

    # Add a button to close the window
    close_btn = Button(history_window, text="Close", command=history_window.destroy, fg="white", bg="red",
                       activebackground="#bf3956")
    close_btn.grid(row=len(history), pady=10, column=0, columnspan=4,rowspan=1, sticky="nsew")

    # Ensure window resizes based on the largest widget
    history_window.update_idletasks()  # Force an update to apply the changes


def btn1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')
def btn2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')
def btn3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')
def btn4_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')
def btn5_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')
def btn6_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')
def btn7_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')
def btn8_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')
def btn9_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')
def btn0_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')
def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)
def btnp_clicked():
    pos = len(disp.get())
    disp.insert(pos, '+')
def btnm_clicked():
    pos = len(disp.get())
    disp.insert(pos, '-')
def btnml_clicked():
    pos = len(disp.get())
    disp.insert(pos, '*')
def btnd_clicked():
    pos = len(disp.get())
    disp.insert(pos, '/')
def btnc_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '0')
def comma_clicked():
    pos = len(disp.get())
    disp.insert(pos, ',')

# Trigonometric and Advanced Functions
def sin_clicked():
    if disp.get() == '0':  
        disp.delete(0, END)  
    
    pos = len(disp.get())
    if disp.get() and (disp.get()[-1].isdigit() or disp.get()[-1] == ')'):
        disp.insert(pos, "*sin(")
    else:
        disp.insert(pos, "sin(")

def cos_clicked():
    if disp.get() == '0':  
        disp.delete(0, END)  
    
    pos = len(disp.get())
    if disp.get() and (disp.get()[-1].isdigit() or disp.get()[-1] == ')'):
        disp.insert(pos, "*cos(")
    else:
        disp.insert(pos, "cos(")

def tan_clicked():
    if disp.get() == '0':  
        disp.delete(0, END)  
    
    pos = len(disp.get())
    if disp.get() and (disp.get()[-1].isdigit() or disp.get()[-1] == ')'):
        disp.insert(pos, "*tan(")
    else:
        disp.insert(pos, "tan(")


def arcsin_clicked():
    if disp.get() == '0':  
        disp.delete(0, END)  

    pos = len(disp.get())
    if disp.get() and (disp.get()[-1].isdigit() or disp.get()[-1] == ')'):
        disp.insert(pos, "*arcsin(")
    else:
        disp.insert(pos, "arcsin(")

def arccos_clicked():
    if disp.get() == '0':  
        disp.delete(0, END)  

    pos = len(disp.get())
    if disp.get() and (disp.get()[-1].isdigit() or disp.get()[-1] == ')'):
        disp.insert(pos, "*arccos(")
    else:
        disp.insert(pos, "arccos(")

def arctan_clicked():
    if disp.get() == '0':  
        disp.delete(0, END)  

    pos = len(disp.get())
    if disp.get() and (disp.get()[-1].isdigit() or disp.get()[-1] == ')'):
        disp.insert(pos, "*arctan(")
    else:
        disp.insert(pos, "arctan(")

def pow_clicked():
    pos = len(disp.get())
    disp.insert(pos, '^')
def round_clicked():
    try:
        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
def logarithm_clicked():
    try:
        ans = float(disp.get())
        exp = disp.get()

        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
        history.append((exp, ans, "log"))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def fact_clicked():
    try:
        num = int(disp.get())
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = math.factorial(num)
        disp.delete(0, END)
        disp.insert(0, str(result))
        history.append((f"{num}!", result, "factorial"))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Input must be a non-negative integer.")




def sqr_clicked():
    if disp.get() == '0':  # If the display shows 0, replace it
        disp.delete(0, END)

    pos = len(disp.get())
    if disp.get() and (disp.get()[-1].isdigit() or disp.get()[-1] == ')'):
        disp.insert(pos, "*sqrt(")
    else:
        disp.insert(pos, "sqrt(")


def dot_clicked():
    pos = len(disp.get())
    disp.insert(pos, '.')
def pi_clicked():
    if disp.get() == '0': 
        disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, str(math.pi))
def e_clicked():
    try:
        disp.delete(0, END) 
        disp.insert(0, str(math.e))  
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Error inserting e constant")

def bl_clicked():
    
    if disp.get() == '0':
        disp.delete(0, END)  
    pos = len(disp.get())
    disp.insert(pos, '(')  

def br_clicked():
    
    if disp.get() == '0':
        disp.delete(0, END)  
    pos = len(disp.get())
    disp.insert(pos, ')')  

def del_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])
def conv_clicked():
    global switch
    if switch is None or switch is False:  
        switch = True
        conv_btn['text'] = "Deg"
    else:  # Switch to radians
        switch = False
        conv_btn['text'] = "Rad"


def ln_clicked():
    if disp.get() == '0':  # If the display shows 0, replace it
        disp.delete(0, END)
    
    pos = len(disp.get())
    if disp.get() and (disp.get()[-1].isdigit() or disp.get()[-1] == ')'):
        disp.insert(pos, "*ln(")
    else:
        disp.insert(pos, "ln(")

def mod_clicked():
    pos = len(disp.get())
    disp.insert(pos, '%')
def btneq_clicked():
    try:
        # Map supported functions to the math module
        allowed_functions = {
            'sin': lambda x: math.sin(math.radians(x) if switch else x),
            'cos': lambda x: math.cos(math.radians(x) if switch else x),
            'tan': lambda x: math.tan(math.radians(x) if switch else x),
            'arcsin': lambda x: math.degrees(math.asin(x)) if switch else math.asin(x),
            'arccos': lambda x: math.degrees(math.acos(x)) if switch else math.acos(x),
            'arctan': lambda x: math.degrees(math.atan(x)) if switch else math.atan(x),
            'sinh': math.sinh,
            'cosh': math.cosh,
            'tanh': math.tanh,
            'gamma': math.gamma,
            'log10': math.log10,
            'ln': math.log,
            'sqrt': math.sqrt,
            'pi': math.pi,
            'e': math.e,
            'pi': math.pi
        }

        # Get the expression from the display
        exp = disp.get()

       

        exp = exp.replace(',', '')

        open_parentheses = exp.count('(')
        close_parentheses = exp.count(')')
        if open_parentheses > close_parentheses:
            exp += ')' * (open_parentheses - close_parentheses)

        # Replace caret (^) with exponentiation operator (**)
        exp = exp.replace('^', '**')
   
        # Evaluate the expression with only allowed functions
        res = eval(exp, {"__builtins__": None}, allowed_functions)

        # Display the result
        disp.delete(0, END)
        disp.insert(0, res)

        # Save to history
        history.append((exp.replace("**", "^"), res, "function"))
    except Exception as e:
        tkinter.messagebox.showerror("Value Error", f"Error evaluating expression: {e}")




def std_clicked():
    try:
        values = list(map(float, disp.get().split(',')))
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        std_dev = math.sqrt(variance)
        disp.delete(0, END)
        disp.insert(0, str(std_dev))
        history.append(("STDDEV",std_dev, values ))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Input must be comma-separated numbers.")

def standard_deviation(data):
    mean = sum(data) / len(data)
    squared_deviations = [(x - mean) ** 2 for x in data]
    variance = sum(squared_deviations) / len(data)
    return math.sqrt(variance)

    return std_dev


def sinh_clicked():
    if disp.get() == '0':  # If the display shows 0, replace it
        disp.delete(0, END)
    
    pos = len(disp.get())
    if disp.get() and (disp.get()[-1].isdigit() or disp.get()[-1] == ')'):
        disp.insert(pos, "*sinh(")
    else:
        disp.insert(pos, "sinh(")

def sinh(x):

    # Calculate e^x
    exp_x = math.exp(x)
    # Calculate e^(-x)
    exp_neg_x = math.exp(-x)
    # Apply the formula
    result = (exp_x - exp_neg_x) / 2
    return result



def mad_clicked():
    try:
        values = list(map(float, disp.get().split(',')))
        mean = sum(values) / len(values)
        mad = sum(abs(x - mean) for x in values) / len(values)
        disp.delete(0, END)
        disp.insert(0, str(mad))
        history.append(("MAD",mad, values))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Input must be comma-separated numbers.")

def mean_absolute_deviation(data):
    mean = sum(data) / len(data)
    absolute_deviations = [abs(x - mean) for x in data]
    return sum(absolute_deviations) / len(data)

def gamma_clicked():
    try:
        num = float(disp.get())
        result = math.gamma(num)
        disp.delete(0, END)
        disp.insert(0, str(result))
        history.append((f"gamma({num})", result, "gamma"))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your input.")

# Display Entry
canvas = Canvas(root, width=400, height=400,bg="#1e2e47")
canvas.grid(row=0, column=0, columnspan=14,rowspan=13, sticky="nsew")
disp = Entry(root, font="Verdana 20", fg="black", bg="mistyrose", bd=4, justify=RIGHT, background="#d9e2eb", foreground="black")
disp.grid(row=0, column=0, columnspan=14,pady=10,padx=50, sticky="nsew")  # Entry spans across all columns


# Configure grid for resizing
root.grid_rowconfigure(0, weight=1)  # Entry row
for i in range(1, 10):  # Button rows
    root.grid_rowconfigure(i, weight=1)
for j in range(9):  # Columns
    root.grid_columnconfigure(j, weight=1)

# --- Buttons ---

# Column 1
pow_btn = Button(root, text="x^y", font="Calibri 17", relief=GROOVE, bd=0, command=pow_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
pow_btn.grid(row=1, column=0, sticky="nsew")

sqr_btn = Button(root, text="√x", font="Calibri 17", relief=GROOVE, bd=0, command=sqr_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
sqr_btn.grid(row=2, column=0, sticky="nsew")

sin_btn = Button(root, text="sin", font="Calibri 17", relief=GROOVE, bd=0, command=sin_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
sin_btn.grid(row=3, column=0, sticky="nsew")

arcsin_btn = Button(root, text="arcsin",font= "Calibri 15" , relief=GROOVE, bd=0, command=arcsin_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
arcsin_btn.grid(row=4, column=0, sticky="nsew")

bl_btn = Button(root, text="(", font="Calibri 21", relief=GROOVE, bd=0, command=bl_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
bl_btn.grid(row=5, column=0, sticky="nsew")
fact_btn = Button(root, text=" x! ", font="Calibri 18", relief=GROOVE, bd=0, command=fact_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
fact_btn.grid(row=6, column=0, sticky="nsew")




# Column 2
std_btn = Button(root, text="σ", font="Calibri 17", relief=GROOVE, bd=0, command=std_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
std_btn.grid(row=1, column=1, sticky="nsew")

logarithm_btn = Button(root, text="log", font="Calibri 17", relief=GROOVE, bd=0, command=logarithm_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
logarithm_btn.grid(row=2, column=1, sticky="nsew")

cos_btn = Button(root, text="cos", font="Calibri 17", relief=GROOVE, bd=0, command=cos_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
cos_btn.grid(row=3, column=1, sticky="nsew")

arccos_btn = Button(root, text="arccos", font="Calibri 12", relief=GROOVE, bd=0, command=arccos_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
arccos_btn.grid(row=4, column=1, sticky="nsew")

br_btn = Button(root, text=")", font="Calibri 21", relief=GROOVE, bd=0, command=br_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
br_btn.grid(row=5, column=1, sticky="nsew")

e_btn = Button(root, text="e", font="Calibri 18", relief=GROOVE, bd=0, command=e_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
e_btn.grid(row=5, column=2, sticky="nsew")

ln_btn = Button(root, text="ln", font="Calibri 18", relief=GROOVE, bd=0, command=ln_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
ln_btn.grid(row=6, column=2, sticky="nsew")

sinh_btn = Button(root, text="sinh", font="Calibri 17", relief=GROOVE, bd=0, command=sinh_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
sinh_btn.grid(row=6, column=1, sticky="nsew")
#gamma_btn = Button(root, text=" gamma ", font="Calibri 18", relief=GROOVE, bd=0, command=gamma_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
#gamma_btn.grid(row=7, column=0, sticky="nsew")

# Column 3
mad_btn = Button(root, text="MAD", font="Calibri 17", relief=GROOVE, bd=0, command=mad_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
mad_btn.grid(row=1, column=2, sticky="nsew")

pi_btn = Button(root, text="π", font="Calibri 17", relief=GROOVE, bd=0, command=pi_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
pi_btn.grid(row=2, column=2, sticky="nsew")

tan_btn = Button(root, text="tan", font="Calibri 17", relief=GROOVE, bd=0, command=tan_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
tan_btn.grid(row=3, column=2, sticky="nsew")

arctan_btn = Button(root, text="arctan", font="Calibri 12", relief=GROOVE, bd=0, command=arctan_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
arctan_btn.grid(row=4, column=2, sticky="nsew")

# Column 4 (Blank)

# Shifted Columns 3, 4, 5 -> 5, 6, 7
# Column 5
btn1 = Button(root, text="1", font="Calibri 23", relief=GROOVE, bd=0, command=btn1_clicked, fg="white", bg="#0d1c2f", activebackground="#bf3956")
btn1.grid(row=1, column=4, sticky="nsew")

btn4 = Button(root, text="4", font="Calibri 23", relief=GROOVE, bd=0, command=btn4_clicked, fg="white", bg="#0d1c2f", activebackground="#bf3956")
btn4.grid(row=2, column=4, sticky="nsew")

btn7 = Button(root, text="7", font="Calibri 23", relief=GROOVE, bd=0, command=btn7_clicked, fg="white", bg="#0d1c2f", activebackground="#bf3956")
btn7.grid(row=3, column=4, sticky="nsew")

btnc = Button(root, text="C", font="Calibri 23", relief=GROOVE, bd=0, command=btnc_clicked, fg="white", bg="#ee4932", activebackground="#bf3956")
btnc.grid(row=4, column=4, sticky="nsew")
del_btn = Button(root, text="⌫", font="Calibri 20", relief=GROOVE, bd=0, command=del_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
del_btn.grid(row=5, column=4, sticky="nsew")

# Column 6
btn2 = Button(root, text="2", font="Calibri 23", relief=GROOVE, bd=0, command=btn2_clicked, fg="white", bg="#0d1c2f", activebackground="#bf3956")
btn2.grid(row=1, column=5, sticky="nsew")

btn5 = Button(root, text="5", font="Calibri 23", relief=GROOVE, bd=0, command=btn5_clicked, fg="white", bg="#0d1c2f", activebackground="#bf3956")
btn5.grid(row=2, column=5, sticky="nsew")

btn8 = Button(root, text="8", font="Calibri 23", relief=GROOVE, bd=0, command=btn8_clicked, fg="white", bg="#0d1c2f", activebackground="#bf3956")
btn8.grid(row=3, column=5, sticky="nsew")

btn0 = Button(root, text="0", font="Calibri 23", relief=GROOVE, bd=0, command=btn0_clicked, fg="white", bg="#0d1c2f", activebackground="#bf3956")
btn0.grid(row=4, column=5, sticky="nsew")

dot_btn = Button(root, text=" • ", font="Calibri 21", relief=GROOVE, bd=0, command=dot_clicked, fg="white", bg="#0d1c2f", activebackground="#bf3956")
dot_btn.grid(row=5, column=5, sticky="nsew")
comma_btn = Button(root, text=" , ", font="Calibri 21", relief=GROOVE, bd=0, command=comma_clicked, fg="white", bg="#0d1c2f", activebackground="#bf3956")
comma_btn.grid(row=6, column=5, sticky="nsew")

# Column 7
btn3 = Button(root, text="3", font="Calibri 23", relief=GROOVE, bd=0, command=btn3_clicked, fg="white", bg="#0d1c2f", activebackground="#bf3956")
btn3.grid(row=1, column=6, sticky="nsew")

btn6 = Button(root, text="6", font="Calibri 23", relief=GROOVE, bd=0, command=btn6_clicked, fg="white", bg="#0d1c2f", activebackground="#bf3956")
btn6.grid(row=2, column=6, sticky="nsew")

btn9 = Button(root, text="9", font="Calibri 23", relief=GROOVE, bd=0, command=btn9_clicked, fg="white", bg="#0d1c2f", activebackground="#bf3956")
btn9.grid(row=3, column=6, sticky="nsew")

btneq = Button(root, text="=", font="Calibri 23", relief=GROOVE, bd=0, command=btneq_clicked, fg="white", bg="#4696ff", activebackground="#bf3956")
btneq.grid(row=4, column=6, sticky="nsew")
round_btn = Button(root, text="round", font="Calibri 15 bold", relief=GROOVE, bd=0, command=round_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
round_btn.grid(row=5, column=6, sticky="nsew")

# Remaining Buttons in Other Columns
conv_btn = Button(root, text="rad", font="Calibri 23", relief=GROOVE, bd=0, command=conv_clicked, fg="white", bg="#4696ff", activebackground="#bf3956")
conv_btn.grid(row=1, column=8, sticky="nsew")

btnp = Button(root, text="+", font="Calibri 25", relief=GROOVE, bd=0, command=btnp_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
btnp.grid(row=2, column=8, sticky="nsew")

btnm = Button(root, text="-", font="Calibri 23", relief=GROOVE, bd=0, command=btnm_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
btnm.grid(row=3, column=8, sticky="nsew")

btnml = Button(root, text="*", font="Calibri 23", relief=GROOVE, bd=0, command=btnml_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
btnml.grid(row=4, column=8, sticky="nsew")

btnd = Button(root, text="/", font="Calibri 23", relief=GROOVE, bd=0, command=btnd_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
btnd.grid(row=5, column=8, sticky="nsew")





mod_btn = Button(root, text="%", font="Calibri 21", relief=GROOVE, bd=0, command=mod_clicked, fg="white", bg="#374f6d", activebackground="#bf3956")
mod_btn.grid(row=6, column=8, sticky="nsew")


#bottom row
fav_btn1 = Button(root, text="", font="Calibri 23", relief=FLAT, bd=0, command=favorite1_clicked, fg="white", bg="#1e2e47", activebackground="#bf3956")
fav_btn1.grid(row=8, column=3, sticky="nsew")
history_btn = Button(root, text="History", font="Calibri 18", relief=GROOVE, bd=0, command=history_clicked, fg="white", bg="#4696ff", activebackground="#bf3956")
history_btn.grid(row=8, column=7, sticky="nsew")



root.mainloop()
