import matplotlib as plt
from tkinter import *

#podstawowe rzeczy związane z inicjacją programu
root = Tk()
title = "Rysowanie funkcji"
root.title(title)
root.geometry("1000x600+400+250") #do korekty
title_label = Label(root, text=title, font=("Segoe UI bold", 24))
title_label.place(relx=0.5, rely=0.075, anchor=CENTER)

#pole na wzór funkcji
function_formula=StringVar()
entry = Entry(root, textvariable=function_formula, width=29, font=("Segoe UI", 20))
entry.place(relx=0.5, rely=0.25, anchor=CENTER)
entry_label = Label(root, text="f(x)=", font=("Segoe UI", 20))
entry_label.place(relx = 0.25, rely=0.25, anchor=CENTER)

#przyciski do budowania wzoru funkcji
open_parenthesis = Button(root, text="(", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "("))
open_parenthesis.place(relx=0.2, rely=0.48, anchor = CENTER)

close_parenthesis = Button(root, text=")", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + ")"))
close_parenthesis.place(relx=0.25, rely=0.48, anchor=CENTER)

exp = Button(root, text="^", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "^"))
exp.place(relx=0.1, rely=0.48, anchor=CENTER)

sq_root = Button(root, text="√", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "√()"))
sq_root.place(relx=0.15, rely=0.48, anchor=CENTER)
mult = Button(root, text="*", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "*"))
mult.place(relx=0.2, rely=0.4, anchor=CENTER)

div = Button(root, text="/", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "/"))
div.place(relx=0.25, rely=0.4, anchor=CENTER)

add = Button(root, text="+", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "+"))
add.place(relx=0.1, rely=0.4, anchor=CENTER)

sub = Button(root, text="-", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "-"))
sub.place(relx=0.15, rely=0.4, anchor=CENTER)

sine = Button(root, text="sin", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "sin()"))
sine.place(relx=0.1, rely=0.56, anchor=CENTER)

cosine = Button(root, text="cos", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "cos()"))
cosine.place(relx=0.15, rely=0.56, anchor=CENTER)

tangent = Button(root, text="tan", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "tan()"))
tangent.place(relx=0.2, rely=0.56, anchor=CENTER)

logarythm = Button(root, text="log", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "log()"))
logarythm.place(relx=0.25, rely=0.56, anchor=CENTER)

#zakresy X i Y
x_range_label = Label(root, text="zakres osi X:", font=("Segoe UI", 12))
x_range_label.place(relx=0.12, rely=0.66, anchor=CENTER)

x_from_label = Label(root, text="od", font=("Segoe UI", 12))
x_from_label.place(relx=0.1, rely=0.71, anchor=CENTER)

x_from = StringVar()
x_from_entry = Entry(root, textvariable=x_from, width=6, font=("Segoe UI", 12))
x_from_entry.place(relx=0.15, rely=0.71, anchor=CENTER)

x_to_label = Label(root, text="do", font=("Segoe UI", 12))
x_to_label.place(relx=0.20, rely=0.71, anchor=CENTER)

x_to = StringVar()
x_to_entry = Entry(root, textvariable=x_to, width=6, font=("Segoe UI", 12))
x_to_entry.place(relx=0.25, rely=0.71, anchor=CENTER)

y_range_label = Label(root, text="zakres osi Y:", font=("Segoe UI", 12))
y_range_label.place(relx=0.12, rely=0.76, anchor=CENTER)

y_from_label = Label(root, text="od", font=("Segoe UI", 12))
y_from_label.place(relx=0.1, rely=0.81, anchor=CENTER)

y_from = StringVar()
y_from_entry = Entry(root, textvariable=y_from, width=6, font=("Segoe UI", 12))
y_from_entry.place(relx=0.15, rely=0.81, anchor=CENTER)

y_to_label = Label(root, text="do", font=("Segoe UI", 12))
y_to_label.place(relx=0.20, rely=0.81, anchor=CENTER)

y_to = StringVar()
y_to_entry = Entry(root, textvariable=y_to, width=6, font=("Segoe UI", 12))
y_to_entry.place(relx=0.25, rely=0.81, anchor=CENTER)

#określanie tytułu rysunku oraz etykiet osi





