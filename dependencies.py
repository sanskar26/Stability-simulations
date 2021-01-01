import os

try:
    import numpy as np
except ImportError:
    print("Trying to Install required module: numpy \n ")
    os.system('python -m pip install numpy')


try:
    import plotly.express as px
except ImportError:
    print("Trying to Install required module: plotly-express \n ")
    os.system('python -m pip install pandas')
    os.system('python -m pip install plotly')


try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Trying to Install required module: matplotlib \n ")
    os.system('python -m pip install matplotlib')

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print("Trying to Install required module: tkinter \n ")
    os.system('python -m pip install tk')
    from tkinter import messagebox


print(" \n All dependencies are installed \n")


messagebox.showinfo("Successfully",
                    "All dependencies are installed successfully")
