import tkinter as tk
import math

class Application:

    buttonWidth = 3

    def __init__(self, master):
        master.title("Calculator")

        self.frame0 = tk.Frame(master)
        self.frame0.grid(row=0, column=0)

        self.input = tk.StringVar()

        self.entry = tk.Entry(self.frame0, textvariable=self.input)
        self.entry.grid(row=0, column=0)

        self.frame = tk.Frame(master)
        self.frame.grid(row=1, column=0)

        self.createWidgets()

    def createWidgets(self):
        #====== Row 0 ========#
        self.buttonSqrt = tk.Button(self.frame, text="√", width=self.buttonWidth,
                                    command=lambda : self.input.set(str(eval(self.input.get()) **0.5)))
        self.buttonSqrt.grid(row=0, column=0)
        self.buttonSquare = tk.Button(self.frame, text="x^2", width=self.buttonWidth,
                                    command=lambda :self.input.set(str(eval(self.input.get() **2))))
        self.buttonSquare.grid(row=0, column=1)
        self.buttonLn = tk.Button(self.frame, text="ln", width=self.buttonWidth,
                                command=lambda :self.input.set(str(math.log(eval(self.input.get())))))
        self.buttonLn.grid(row=0, column=2)
        self.buttonClear = tk.Button(self.frame, text="C", width=self.buttonWidth,
                                    command=lambda :self.input.set(""))
        self.buttonClear.grid(row=0, column=3)

        #====== Row 1 ======#
        self.button7 = tk.Button(self.frame, text="7", width=self.buttonWidth,
                                command=lambda : self.input.set(self.input.get() + "7"))
        self.button7.grid(row=1, column=0)
        self.button8 = tk.Button(self.frame, text="8", width=self.buttonWidth,
                                command=lambda : self.input.set(self.input.get() + "8"))
        self.button8.grid(row=1, column=1)
        self.button9 = tk.Button(self.frame, text="9", width=self.buttonWidth,
                                command=lambda : self.input.set(self.input.get() + "9"))
        self.button9.grid(row=1, column=2)
        self.buttonAdd = tk.Button(self.frame, text="+", width=self.buttonWidth,
                                    command=lambda : self.input.set(self.input.get() + "+"))
        self.buttonAdd.grid(row=1, column=3)

        #====== Row 2 ========#
        self.button4 = tk.Button(self.frame, text="4", width=self.buttonWidth,
                                command=lambda : self.input.set(self.input.get() + "4"))
        self.button4.grid(row=2, column=0)
        self.button5 = tk.Button(self.frame, text="5", width=self.buttonWidth,
                                command=lambda : self.input.set(self.input.get() + "5"))
        self.button5.grid(row=2, column=1)
        self.button6 = tk.Button(self.frame, text="6", width=self.buttonWidth,
                                command=lambda : self.input.set(self.input.get() + "6"))
        self.button6.grid(row=2, column=2)
        self.buttonSubtract = tk.Button(self.frame, text="-", width=self.buttonWidth,
                                        command=lambda : self.input.set(self.input.get() + "-"))
        self.buttonSubtract.grid(row=2, column=3)

        #====== Row 3 ========#
        self.button1 = tk.Button(self.frame, text="1", width=self.buttonWidth,
                                command=lambda : self.input.set(self.input.get() + "1"))
        self.button1.grid(row=3, column=0)
        self.button2 = tk.Button(self.frame, text="2", width=self.buttonWidth,
                                command=lambda : self.input.set(self.input.get() + "2"))
        self.button2.grid(row=3, column=1)
        self.button3 = tk.Button(self.frame, text="3", width=self.buttonWidth,
                                command=lambda : self.input.set(self.input.get() + "3"))
        self.button3.grid(row=3, column=2)
        self.buttonMultiply = tk.Button(self.frame, text="*", width=self.buttonWidth,
                                        command=lambda : self.input.set(self.input.get() + "*"))
        self.buttonMultiply.grid(row=3, column=3)

        #====== Row 4 ========#
        self.button0 = tk.Button(self.frame, text="0", width=3*self.buttonWidth -1,
                                command=lambda : self.input.set(self.input.get() + "0"))
        self.button0.grid(row=4, columnspan=2, column=0)
        self.buttonEqual = tk.Button(self.frame, text="=", width=self.buttonWidth,
                                    command=lambda : self.input.set(eval(self.input.get())))
        self.buttonEqual.grid(row=4, column=2)
        self.buttonDivide = tk.Button(self.frame, text="/", width=self.buttonWidth,
                                    command=lambda : self.input.set(self.input.get() + "/"))
        self.buttonDivide.grid(row=4, column=3)


root = tk.Tk()
window = Application(root)
root.mainloop()
