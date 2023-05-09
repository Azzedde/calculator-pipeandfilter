import tkinter as tk
import subprocess
import os
class Gui:
    def quit(self):
        self.root.quit()

    def trace(self):
        log_file = os.path.join('E:', 'Study docs', 'python-pipeandfilter', 'calculator.log')
        subprocess.run(['open', log_file], check=True)

    def __init__(self, calculator, log):
        self.calculator = calculator
        self.log = log
        self.gui_to_calculator_pipe = self.calculator.gui_to_calculator_pipe
        self.calculator_to_gui_pipe = self.calculator.calculator_to_gui_pipe

    def run(self):
        
        self.root = tk.Tk()
        self.root.title("Calculatrice")
        self.root.geometry("300x200")
        self.root.title('Les formes et les vues')
        self.root.resizable(width=True, height=False)

        self.num1_label = tk.Label(self.root, text='Num 1:')
        self.num1_label.grid(row=0, column=0, padx=5, pady=5)
        self.num1_entry = tk.Entry(self.root, width=10)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        self.num2_label = tk.Label(self.root, text='Num 2:')
        self.num2_label.grid(row=0, column=2, padx=5, pady=5)
        self.num2_entry = tk.Entry(self.root, width=10)
        self.num2_entry.grid(row=0, column=3, padx=5, pady=5)

        self.divider1 = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
        self.divider1.grid(row=1, columnspan=4, sticky='we', padx=5, pady=5)
        # Second line - operation buttons
        self.operation_label = tk.Label(self.root, text='Opération:')
        self.operation_label.grid(row=2, column=0, padx=5, pady=5)
        
        self.sum_button = tk.Button(self.root, text="Somme", command=self.sum)
        self.product_button = tk.Button(self.root, text="Produit", command=self.product)
        self.factorial_button = tk.Button(self.root, text="Factoriel", command=self.factorial)
        self.sum_button.grid(row=2, column=1)
        self.product_button.grid(row=2, column=2)
        self.factorial_button.grid(row=2, column=3)
        
        # Line divider
        self.divider2 = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
        self.divider2.grid(row=3, columnspan=4, sticky='we', padx=5, pady=5)
        
        # Third line - result display
        self.result_label = tk.Label(self.root, text='Résultat:')
        self.result_label.grid(row=4, column=0, padx=5, pady=5)
        

        
        # Fourth line - Quit and Trace buttons
        self.quit_button = tk.Button(self.root, text='Quitter', command=self.quit)
        self.quit_button.grid(row=5, column=1, padx=5, pady=5)
        
        self.trace_button = tk.Button(self.root, text='Trace', command=self.trace)
        self.trace_button.grid(row=5, column=2, padx=5, pady=5)
        self.root.mainloop()

        

    def get_num1(self):
        return int(self.num1_entry.get())

    def get_num2(self):
        return int(self.num2_entry.get())

    def set_result(self, result):
        self.result_label.configure(text="Résultat : " + str(result))

    def sum(self):
        num1 = self.get_num1()
        num2 = self.get_num2()
        self.gui_to_calculator_pipe.put((num1, num2, '+'))
        self.set_result(self.calculator_to_gui_pipe.get())



    def product(self):
        num1 = self.get_num1()
        num2 = self.get_num2()
        self.gui_to_calculator_pipe.put((num1, num2, '*'))
        self.set_result(self.calculator_to_gui_pipe.get())


    def factorial(self):
        num1 = self.get_num1()
        self.gui_to_calculator_pipe.put((num1, 0, '!'))
        self.set_result(self.calculator_to_gui_pipe.get())