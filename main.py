
from Calculator import Calculator
from Gui import Gui
from Log import Log
from threading import Thread



calc = Calculator()
log = Log('calculator.log', calc)
gui = Gui(calc, log) 


gui_to_calc_pipe = gui.gui_to_calculator_pipe, calc.gui_to_calculator_pipe
calc_to_log_pipe = calc.calculator_to_log_pipe, log.input_queue


gui_thread = Thread(target=gui.run)
log_thread = Thread(target=log.run)
calc_thread = Thread(target=calc.run)

gui_thread.start()
log_thread.start()
calc_thread.start()


gui_thread.join()




