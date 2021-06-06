import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import messagebox
from numpy import sqrt,sin,cos,tan,log,linspace
from math import ceil

#podstawowe rzeczy związane z inicjacją programu
root = Tk()
title = "Rysowanie funkcji"
root.title(title)
root.geometry("1000x600+460+220")

#przycisk kończący działanie programu
exit_button = Button(root, text="Wyjdź", command=root.destroy)
exit_button.place(relx=1, rely=0, anchor=NE)

#pole na wzór funkcji
function_formula=StringVar()
entry = Entry(root, textvariable=function_formula, width=25, font=("Segoe UI", 20))
entry.place(relx=0.26, rely=0.1, anchor=CENTER)
entry_label = Label(root, text="f(x)=", font=("Segoe UI", 20))
entry_label.place(relx = 0.04, rely=0.1, anchor=CENTER)

#przyciski do budowania wzoru funkcji




div = Button(root, text="/", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "/"))
div.place(relx=0.25, rely=0.2, anchor=CENTER)

add = Button(root, text="+", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "+"))
add.place(relx=0.1, rely=0.2, anchor=CENTER)

sub = Button(root, text="-", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "-"))
sub.place(relx=0.15, rely=0.2, anchor=CENTER)

exp = Button(root, text="^", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "^"))
exp.place(relx=0.1, rely=0.28, anchor=CENTER)

sq_root = Button(root, text="√", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "√()"))
sq_root.place(relx=0.15, rely=0.28, anchor=CENTER)

mult = Button(root, text="*", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "*"))
mult.place(relx=0.2, rely=0.2, anchor=CENTER)

open_parenthesis = Button(root, text="(", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + "("))
open_parenthesis.place(relx=0.2, rely=0.28, anchor = CENTER)

close_parenthesis = Button(root, text=")", height=1, width=4, font=("Segoe UI", 12), command = lambda: function_formula.set(function_formula.get() + ")"))
close_parenthesis.place(relx=0.25, rely=0.28, anchor=CENTER)

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
plot_title_label.place(relx=0.18, rely=0.68, anchor=E)

plot_title=StringVar()
plot_title_entry = Entry(root, textvariable=plot_title, font=("Segoe UI", 12))
plot_title_entry.place(relx=0.285, rely=0.68, anchor=CENTER)

plot_xlabel_label = Label(root, text="nazwa etykiety osi X:", font=("Segoe UI", 12))
plot_xlabel_label.place(relx=0.18, rely=0.73, anchor=E)

plot_xlabel = StringVar()
plot_xlabel_entry = Entry(root, textvariable=plot_xlabel, font=("Segoe UI", 12))
plot_xlabel_entry.place(relx=0.285, rely=0.73, anchor=CENTER)

plot_ylabel_label = Label(root, text="nazwa etykiety osi Y:", font=("Segoe UI", 12))
plot_ylabel_label.place(relx=0.18, rely=0.78, anchor=E)

plot_ylabel = StringVar()
plot_ylabel_entry = Entry(root, textvariable=plot_ylabel, font=("Segoe UI", 12))
plot_ylabel_entry.place(relx=0.285, rely=0.78, anchor=CENTER)

#przycisk legendy
legend_button_val = IntVar()
legend_button = Checkbutton(root, text="legenda", variable=legend_button_val, onvalue=1, offvalue=0, font=("Segoe UI", 12))
legend_button.place(relx=0.1, rely=0.88, anchor=CENTER)

#konwersja StringVarów na floaty
def convert(x_from, x_to, y_from, y_to):
    """Przetwarza zakresy osi X i Y podane w typie StringVar, zwracając je w typie float w liście, w kolejności, w jakiej się je podawało jako argumenty"""
    val_list = [x_from.get(), x_to.get(), y_from.get(), y_to.get()]
    for i in range(len(val_list)):
        val_list[i] = val_list[i].replace(",",".")
        try:
            val_list[i] = float(val_list[i])
        except:
            pass
    return val_list

#przekształcenie wzoru / wzorów
def nice_formula(function_formula):
    """Przekształca wzór (lub wzory) funkcji podany w polu tekstowym na język zrozumiały dla Pythona"""
    nice_formula=function_formula.get().replace("^","**")
    nice_formula=nice_formula.replace("√","sqrt")
    nice_formula=nice_formula.replace(",",".")
    nice_formula_list=nice_formula.split("; ")
    return nice_formula_list   

#funkcja rysowania wykresu
def make_plot(x_from,x_to,y_from,y_to,function_formula,legend_button_val):
    """Rysuje wykres funkcji, korzystając z danych zwracanych przez funkcje convert() oraz nice_formula(), opcjonalnie dodaje do wykresy legendę"""
    val_list = convert(x_from, x_to, y_from, y_to)
    for i in val_list:
        if type(i) != float:
            messagebox.showerror("Błąd","Proszę podać poprawne zakresy osi.")
            return
    xs = linspace(val_list[0], val_list[1], num=ceil(val_list[1]-val_list[0])*100).tolist()
    formula=function_formula.get()
    formula_list = formula.split("; ")
    nice_formula_list = nice_formula(function_formula)
    ys = [ [] for i in range(len(nice_formula_list)) ]
    for i in range(len(nice_formula_list)):
        for j in range(len(xs)):
            try:
                x = xs[j]
                ys[i].append(eval(nice_formula_list[i]))
            except:
                if len(formula_list) <= 1:
                    messagebox.showerror("Błąd","Proszę podać poprawny wzór funkcji.")
                    return
                else:
                    messagebox.showerror("Błąd","Proszę podać poprawne zwory funkcji.")
                    return
    figure = Figure(figsize=(5,5), dpi=100)
    plotter = figure.add_subplot(111)
    for i in range(len(ys)):
           plotter.plot(xs, ys[i], label = formula_list[i])
    plotter.set_title(plot_title.get())
    plotter.set_xlabel(plot_xlabel.get())
    plotter.set_ylabel(plot_ylabel.get())
    plotter.set_ylim(val_list[2], val_list[3])
    plotter.set_xlim(val_list[0], val_list[1])
    figure.tight_layout()
    if legend_button_val.get() == 1:
        plotter.legend()
    canvas = FigureCanvasTkAgg(figure, root)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.97, rely=0.95, anchor=SE)

#przycisk do rysowania
plot_button = Button(root, text="Rysuj", height=1, width=11, font=("Segoe UI", 20), command = lambda: make_plot())
plot_button.place(relx=0.29, rely=0.88, anchor=CENTER)

root.mainloop()
