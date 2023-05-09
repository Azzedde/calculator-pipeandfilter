from queue import Queue
from Log import Log
from math import factorial

class Calculator:
    def __init__(self):
        self.gui_to_calculator_pipe = Queue(maxsize=0)
        self.calculator_to_gui_pipe = Queue(maxsize=0)
        self.calculator_to_log_pipe = Queue(maxsize=0)

    def run(self):
        while True:
            # Receive user input from the GUI filter
            x, y, operation = self.gui_to_calculator_pipe.get()

            
            if operation == '+':
                result = x + y
            elif operation == '*':
                result = x * y
            elif operation == '!':
                result = factorial(x)

            
            self.calculator_to_gui_pipe.put(result)
           
            self.calculator_to_log_pipe.put((x, y, result, operation))


