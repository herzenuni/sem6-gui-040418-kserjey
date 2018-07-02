from tkinter import Tk, Frame, Label, Entry, Button, Text
import numpy


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.array_a = []
        self.array_b = []

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.header = Label(self, text='Ввод данных').grid(row=1, column=3)

        Label(self, text="a1m").grid(row=2, column=1)
        self.x1m = Entry(self, width=10)
        self.x1m.grid(row=2, column=2)
        Label(self, text="a2m").grid(row=3, column=1)
        self.x2m = Entry(self, width=10)
        self.x2m.grid(row=3, column=2)
        Label(self, text="a3m").grid(row=4, column=1)
        self.x3m = Entry(self, width=10)
        self.x3m.grid(row=4, column=2)
        Label(self, text="a4m").grid(row=5, column=1)
        self.x4m = Entry(self, width=10)
        self.x4m.grid(row=5, column=2)

        Label(self, text="b1m").grid(row=2, column=3)
        self.b1m = Entry(self, width=10)
        self.b1m.grid(row=2, column=4)
        Label(self, text="b2m").grid(row=3, column=3)
        self.b2m = Entry(self, width=10)
        self.b2m.grid(row=3, column=4)
        Label(self, text="b3m").grid(row=4, column=3)
        self.b3m = Entry(self, width=10)
        self.b3m.grid(row=4, column=4)
        Label(self, text="b4m").grid(row=5, column=3)
        self.b4m = Entry(self, width=10)
        self.b4m.grid(row=5, column=4)

        self.read_button = Button(
            self, text="Принять", command=self.read_array).grid(row=2, column=7, padx=(10, 0))
        self.solve = Button(self, text="Решить", command=self.solve).grid(
            row=3, column=7, padx=(10, 0))
        self.output = Text(self, bg="lightblue", font="Arial 14",
                           width=35, height=10)

        self.output.grid(row=12, columnspan=8)

    def read_row(self, input):
        return [int(item) for item in input.get().split()]

    def read_array(self):
        row1 = self.read_row(self.x1m)
        row2 = self.read_row(self.x2m)
        row3 = self.read_row(self.x3m)
        row4 = self.read_row(self.x4m)
        self.array_a = [row1] + [row2] + [row3] + [row4]

        inputs = [self.b1m, self.b2m, self.b3m, self.b4m]
        mapped_values = map(lambda x: int(x.get()), inputs)
        self.array_b = list(mapped_values)

    def solve(self):
        a = numpy.array(self.array_a)
        b = numpy.array(self.array_b)
        print(self.array_a, self.array_b)
        result = numpy.linalg.solve(a, b)
        self.output.insert("0.0", result)


root = Tk()
root.title('СЛАУ')
app = Application(master=root)
app.mainloop()
