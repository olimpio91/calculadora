from tkinter import *

class Application(Tk):
    def __init__(self):
        super().__init__()
        self.config()
        self.frame1()
        self.frame2()
        self.display()
        self.widgets()

    def config(self):
        self.title("Calculadora")
        self.geometry("400x450")
        self.minsize(width=350, height=450)

    def frame1(self):
        self.frame = Frame(self, width=380, height=150)
        self.frame.pack(side=TOP, fill=X, padx=10, pady=10)
        self.frame.pack_propagate(0)

    def frame2(self):
        self.frame2 = Frame(self)
        self.frame2.pack(side=TOP, fill=BOTH, padx=10, pady=10, expand=True)

    def display(self):
        self.entry = Entry(self.frame)
        self.entry.configure(font=("Arial", 30))
        self.entry.pack(fill=BOTH, ipady=140)

    def widgets(self):
        
        self.clear_all = Button(self.frame2, text="C", width=12, height=2, command=self.clearAll)
        self.clear = Button(self.frame2, text="X", width=12, height=2, command=self.clear_All)
        self.ocupar = Button(self.frame2, width=12, height=2)

        self.division = Button(self.frame2, text="/", width=12, height=2, command=lambda:self.show("/"))

        self.button7 = Button(self.frame2, text="7", width=12, height=2, command= lambda:self.show(7))
        self.button8 = Button(self.frame2, text="8", width=12, height=2, command=lambda:self.show(8))
        self.button9 = Button(self.frame2, text="9", width=12, height=2, command=lambda:self.show(9))
        self.button_multiplication = Button(self.frame2, text="*", width=12, height=2, command=lambda:self.show("*"))

        self.button4 = Button(self.frame2, text="4", width=12, height=2, command=lambda:self.show(4))
        self.button5 = Button(self.frame2, text="5", width=12, height=2, command=lambda:self.show(5))
        self.button6 = Button(self.frame2, text="6", width=12, height=2, command=lambda:self.show(6))
        self.button_subtraction = Button(self.frame2, text="-", width=12, height=2, command=lambda:self.show("-"))

        self.button1 = Button(self.frame2, text="1", width=12, height=2, command=lambda:self.show(1))
        self.button2 = Button(self.frame2, text="2", width=12, height=2, command=lambda:self.show(2))
        self.button3 = Button(self.frame2, text="3", width=12, height=2, command=lambda:self.show(3))
        self.button_sum = Button(self.frame2, text="+", width=12, height=2, command=lambda:self.show("+"))

        self.trocar = Button(self.frame2, text="+/-", width=12, height=2, command=self.substituir)
        self.button0 = Button(self.frame2, text="0", width=12, height=2, command=lambda:self.show(0))
        self.button_decimal = Button(self.frame2, text=",", width=12, height=2, command=lambda:self.show(","))
        self.button_same = Button(self.frame2, text="=", width=12, height=2, command=self.result)


        self.clear_all.grid(row=0, column=0, rowspan=2, columnspan=2, sticky=NSEW)
        self.clear.grid(row=0, column=3, sticky=NSEW)
        self.ocupar.grid(row=0, column=2, rowspan=2, columnspan=1, sticky=NSEW)

        self.division.grid(row=1, column=3, sticky=NSEW)

        self.button7.grid(row=2, column=0, sticky=NSEW)
        self.button8.grid(row=2, column=1, sticky=NSEW)
        self.button9.grid(row=2, column=2, sticky=NSEW)
        self.button_multiplication.grid(row=2, column=3, sticky=NSEW)

        self.button4.grid(row=3, column=0, sticky=NSEW)
        self.button5.grid(row=3, column=1, sticky=NSEW)
        self.button6.grid(row=3, column=2, sticky=NSEW)
        self.button_subtraction.grid(row=3, column=3, sticky=NSEW)
        
        self.button1.grid(row=4, column=0, sticky=NSEW)
        self.button2.grid(row=4, column=1, sticky=NSEW)
        self.button3.grid(row=4, column=2, sticky=NSEW)
        self.button_sum.grid(row=4, column=3, sticky=NSEW)

        self.trocar.grid(row=5, column=0, sticky=NSEW)
        self.button0.grid(row=5, column=1, sticky=NSEW)
        self.button_decimal.grid(row=5, column=2, sticky=NSEW)
        self.button_same.grid(row=5, column=3, sticky=NSEW)

        self.columns = 4
        self.rows = 6

        for x in range(self.columns):
            self.frame2.grid_columnconfigure(x, weight=1)

        for x in range(self.rows):
            self.frame2.grid_rowconfigure(x, weight=1)

    def show(self,value):
        self.entry.focus()
        self.entry.insert(INSERT, value)

    def clear_All(self):

        self.langth = len(self.entry.get())
        self.entry.delete(self.langth - 1)

    def clearAll(self):
        self.entry.delete(0,END)

    def substituir(self):
        pass
        
    def utils(self):
        self.methods = ["+", "-", "*", "/"]
        self.elements = self.entry.get()
        self.firstNumbers = str()
        self.secundNumbers = str()
        self.method = list()

        print("entrada:", self.entry.get())
        for x in self.methods:
            if x in self.elements:
                self.position = self.elements.index(x)
                self.method.append(self.elements[self.position])

        print("metodo:", self.method)

        if "," in self.elements:
            self.elements = self.elements.replace(",", ".")
            self.firstNumbers = float("".join(self.elements[0:self.position]))
            self.secundNumbers = float("".join(self.elements[self.position + 1 : len(self.elements) + 1]))

            return print("numeros primeiro elemento:", self.firstNumbers, "numeros segundo elemento:", self.secundNumbers)
        else:
            self.firstNumbers = int("".join(self.elements[0:self.position]))
            self.secundNumbers = int("".join(self.elements[self.position + 1 : len(self.elements) + 1]))
            
            return print("numeros primeiro elemento:", self.firstNumbers, "numeros segundo elemento:", self.secundNumbers)


    def sum(self):
        if "+" in self.method:
            soma = self.firstNumbers + self.secundNumbers
            self.clearAll()
            self.entry.insert(0,soma)

    def sub(self):
        sub = self.firstNumbers - self.secundNumbers
        self.clearAll()
        self.entry.insert(0,sub)

    def mult(self):
        mult = self.firstNumbers * self.secundNumbers
        self.clearAll()
        self.entry.insert(0,mult)

    def div(self):
        div = self.firstNumbers / self.secundNumbers
        self.clearAll()
        self.entry.insert(0,div)
    
    def result(self):
        self.utils()

        if "+" in self.method:
            self.sum()

        elif "-" in self.method:
            self.sub()

        elif "*" in self.method:
            self.mult()

        else:
            self.div()

run = Application()
run.mainloop()