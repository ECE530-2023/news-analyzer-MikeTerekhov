import queue
from time import *
import threading 

q = queue.Queue()

import queue

# Define a function to be called by the queue
def my_function(arg1, arg2):
    # do something with the arguments
    print("Function called with arguments:", arg1, arg2)

# Create a queue object
q = queue.Queue()

# Add function calls to the queue
q.put((my_function, "arg1_value", "arg2_value"))
q.put((my_function, "arg1_value_2", "arg2_value_2"))
q.put((my_function, "arg1_value_3", "arg2_value_3"))
q.put((my_function, "arg1_value_4", "arg2_value_4"))
q.put((my_function, "arg1_value_5", "arg2_value_5"))

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Process the queue
while not q.empty():
    # Get the function call from the queue
    func, *args = q.get()
    # Call the function with the arguments
    func(*args)

