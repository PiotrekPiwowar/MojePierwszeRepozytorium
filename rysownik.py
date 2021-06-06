import matplotlib as plt
from tkinter import *
import numpy as np

#podstawowe rzeczy związane z inicjacją programu
root = Tk()
title = "Rysowanie funkcji"
root.title(title)
root.geometry("1000x600+400+250") #do korekty

#przycisk kończący działanie programu
exit_button = Button(root, text="Wyjdź", command=root.destroy)
exit_button.place(relx=1, rely=1, anchor=SE)

#pole na wzór funkcji
function_formula=StringVar()
entry = Entry(root, textvariable=function_formula, width=29, font=("Segoe UI", 20))
entry.place(relx=0.5, rely=0.1, anchor=CENTER)
entry_label = Label(root, text="f(x)=", font=("Segoe UI", 20))
entry_label.place(relx = 0.25, rely=0.1, anchor=CENTER)

#przyciski do budowania wzoru funkcji
open_parenthesis = Button(root, text="(", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "("))
open_parenthesis.place(relx=0.2, rely=0.28, anchor = CENTER)

close_parenthesis = Button(root, text=")", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + ")"))
close_parenthesis.place(relx=0.25, rely=0.28, anchor=CENTER)

exp = Button(root, text="^", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "^"))
exp.place(relx=0.1, rely=0.28, anchor=CENTER)

sq_root = Button(root, text="√", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "√()"))
sq_root.place(relx=0.15, rely=0.28, anchor=CENTER)
mult = Button(root, text="*", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "*"))
mult.place(relx=0.2, rely=0.2, anchor=CENTER)

div = Button(root, text="/", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "/"))
div.place(relx=0.25, rely=0.2, anchor=CENTER)

add = Button(root, text="+", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "+"))
add.place(relx=0.1, rely=0.2, anchor=CENTER)

sub = Button(root, text="-", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "-"))
sub.place(relx=0.15, rely=0.2, anchor=CENTER)

sine = Button(root, text="sin", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "sin()"))
sine.place(relx=0.1, rely=0.36, anchor=CENTER)

cosine = Button(root, text="cos", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "cos()"))
cosine.place(relx=0.15, rely=0.36, anchor=CENTER)

tangent = Button(root, text="tan", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "tan()"))
tangent.place(relx=0.2, rely=0.36, anchor=CENTER)

logarythm = Button(root, text="log", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "log()"))
logarythm.place(relx=0.25, rely=0.36, anchor=CENTER)

#zakresy X i Y
x_range_label = Label(root, text="zakres osi X:", font=("Segoe UI", 12))
x_range_label.place(relx=0.12, rely=0.46, anchor=CENTER)

x_from_label = Label(root, text="od", font=("Segoe UI", 12))
x_from_label.place(relx=0.1, rely=0.51, anchor=CENTER)

x_from = StringVar()
x_from_entry = Entry(root, textvariable=x_from, width=6, font=("Segoe UI", 12))
x_from_entry.place(relx=0.15, rely=0.51, anchor=CENTER)

x_to_label = Label(root, text="do", font=("Segoe UI", 12))
x_to_label.place(relx=0.20, rely=0.51, anchor=CENTER)

x_to = StringVar()
x_to_entry = Entry(root, textvariable=x_to, width=6, font=("Segoe UI", 12))
x_to_entry.place(relx=0.25, rely=0.51, anchor=CENTER)

y_range_label = Label(root, text="zakres osi Y:", font=("Segoe UI", 12))
y_range_label.place(relx=0.12, rely=0.56, anchor=CENTER)

y_from_label = Label(root, text="od", font=("Segoe UI", 12))
y_from_label.place(relx=0.1, rely=0.61, anchor=CENTER)

y_from = StringVar()
y_from_entry = Entry(root, textvariable=y_from, width=6, font=("Segoe UI", 12))
y_from_entry.place(relx=0.15, rely=0.61, anchor=CENTER)

y_to_label = Label(root, text="do", font=("Segoe UI", 12))
y_to_label.place(relx=0.20, rely=0.61, anchor=CENTER)

y_to = StringVar()
y_to_entry = Entry(root, textvariable=y_to, width=6, font=("Segoe UI", 12))
y_to_entry.place(relx=0.25, rely=0.61, anchor=CENTER)

#określanie tytułu rysunku oraz etykiet osi

plot_title_label = Label(root, text="nazwa rysunku:", font=("Segoe UI", 12))
plot_title_label.place(relx=0.18, rely=0.7, anchor=E)

plot_title=StringVar()
plot_title_entry = Entry(root, textvariable=plot_title, font=("Segoe UI", 12))
plot_title_entry.place(relx=0.285, rely=0.7, anchor=CENTER)

plot_xlabel_label = Label(root, text="nazwa etykiety osi X:", font=("Segoe UI", 12))
plot_xlabel_label.place(relx=0.18, rely=0.75, anchor=E)

plot_xlabel = StringVar()
plot_xlabel_entry = Entry(root, textvariable=plot_xlabel, font=("Segoe UI", 12))
plot_xlabel_entry.place(relx=0.285, rely=0.75, anchor=CENTER)

plot_ylabel_label = Label(root, text="nazwa etykiety osi Y:", font=("Segoe UI", 12))
plot_ylabel_label.place(relx=0.18, rely=0.8, anchor=E)

plot_ylabel = StringVar()
plot_ylabel_entry = Entry(root, textvariable=plot_ylabel, font=("Segoe UI", 12))
plot_ylabel_entry.place(relx=0.285, rely=0.8, anchor=CENTER)

#przycisk legendy
legend_button_val = IntVar()
legend_button = Checkbutton(root, text="legenda", variable=legend_button_val, onvalue=1, offvalue=0, font=("Segoe UI", 12))
legend_button.place(relx=0.1, rely=0.9, anchor=CENTER)



