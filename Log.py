from queue import Queue
class Log:
    def __init__(self, filename, calc):
        self.input_queue = calc.calculator_to_log_pipe
        self.filename = filename

    def run(self):
        while True:
            op1, op2, result, operation = self.input_queue.get()

            with open(self.filename, 'a') as f:
                if operation == '+':
                    message = f"{op1} + {op2} = {result}"
                elif operation == '*':
                    message = f"{op1} * {op2} = {result}"
                elif operation == '!':
                    message = f"{op1}! = {result}"
                f.write(f"{message}\n")


    def get_input(self):
        return self.input_queue.get()