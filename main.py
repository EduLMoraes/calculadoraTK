from tkinter import *

class Main:
    def __init__(self):
        self.num = []
        self.res = 0
        self.ope = None
        self.cal = str()
        self.resultado = False
    
    def window(self):
        self.window = Tk()  
        self.window.title("Calculadora")
        self.window.minsize(width=390, height=300)
        self.window.maxsize(width=390, height=300)
        self.window.configure(background='black')
        self.texto = StringVar()
    

        self.addText(width=100, row=0, column=0)
        
        self.frame = Frame(self.window)
        self.frame.pack()

        self.addButton("clear", width="5", background="#ff5050", command=lambda: self.clear(), row=1, column=0)
        self.addButton("backspace", width="10", command=lambda: self.back(), background="#202020", row=1, column=1)
        
        self.addButton("1", width="10", command=lambda: self.number(1), background="#202020", row=2, column = 0)
        self.addButton("2", width="10", command=lambda: self.number(2), background="#202020", row=2, column = 1)
        self.addButton("3", width="10", command=lambda: self.number(3), background="#202020", row=2, column = 2)
        self.addButton("4", width="10", command=lambda: self.number(4), background="#202020", row=3, column = 0)
        self.addButton("5", width="10", command=lambda: self.number(5), background="#202020", row=3, column = 1)
        self.addButton("6", width="10", command=lambda: self.number(6), background="#202020", row=3, column = 2)
        self.addButton("7", width="10", command=lambda: self.number(7), background="#202020", row=4, column = 0)
        self.addButton("8", width="10", command=lambda: self.number(8), background="#202020", row=4, column = 1)
        self.addButton("9", width="10", command=lambda: self.number(9), background="#202020", row=4, column = 2)
        self.addButton("0", width="10", command=lambda: self.number(0), background="#202020", row=5, column = 1)
        
        self.addButton("=", width="10", command=lambda: self.realize(), background="#202020", row=6, column = 2)
        self.addButton("-", width="10", command=lambda: self.sub(), background="#202020", row=6, column = 0)
        self.addButton("+", width="10", command=lambda: self.sum(), background="#202020", row=6, column = 1)
        self.addButton("*", width="10", command=lambda: self.mul(), background="#202020", row=5, column = 2)
        self.addButton("/", width="10", command=lambda: self.div(), background="#202020", row=5, column = 0)
        
        
        self.window.mainloop()
        
    def addButton(self, text, command = None, width = None, row = None, column = None, background = None):
        self.button = Button(self.frame,
                             text=text,
                             command=command,
                             width=width,
                             font="bold",
                             background=background,
                             fg="white")
        self.button.grid(row=row, column=column)
        
    def addInput(self, text, width = None, row = None, column = None):
        self.entry = Entry(self.window, text = text, width=width)
        self.entry.grid(row=row, column=column)
        
    def addText(self, text = None, textvariable = None, width = None, justify = "right", row = None, column = None):
        self.text = Label(self.window,
                          textvariable=str(self.texto),
                          width=width, font="bold",
                          background="#333",
                          height="5",
                          justify=justify,
                          fg="white")
        self.text.pack()
        
    def number(self, number):
        self.addNum(number)
        self.texto.set(self.cal)
        
    def addNum(self, number):
        self.num.append(number)
        
        if self.resultado:
            self.resultado = False
        
        for i in self.num:
            self.cal += str(i)
            
        self.num = []
            
    def clear(self):
        self.num = []
        self.cal = ""
        self.texto.set(self.cal)
        
    def back(self):
        self.cal = self.cal[:-1]
        self.texto.set(self.cal)
        
    def mul(self):
        if self.resultado:
            self.cal = ""
            self.cal += str(self.resultado)
        self.cal = self.cal + "*"
        self.num = []
        self.texto.set(self.cal)
        
    def sum(self):
        if self.resultado:
            self.cal = ""
            self.cal += str(self.resultado)
        self.cal = self.cal + "+"
        self.num = []
        self.texto.set(self.cal)

    def sub(self):
        if self.resultado:
            self.cal = ""
            self.cal += str(self.resultado)
        self.cal = self.cal + "-"
        self.num = []
        self.texto.set(self.cal)

    def div(self):
        if self.resultado:
            self.cal = ""
            self.cal += str(self.resultado)
        self.cal = self.cal + "/"
        self.num = []
        self.texto.set(self.cal)

    def realize(self):
        self.resultado = eval(self.cal)
        self.num.append(self.resultado)
        self.texto.set(self.num)
        self.num = []
        self.cal = ""

Main().window()
