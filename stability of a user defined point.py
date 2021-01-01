import os

try:
    import numpy as np
except ImportError:
    print("Trying to Install required module: numpy \n ")
    os.system('python -m pip install numpy')

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

import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Stability Plot")
root.geometry("500x400")


def fuc(t, c_1, c_2, poww):
    R = 8.314                          # Universal Gas constant
    del_g = c_1*t-c_2
    k = del_g/((R*t)*poww)
    f = np.exp(k)                       # This Function Returns PH2/(pH2+ PH2O)
    return 1/(1+f)


li_t1 = np.linspace(300, 845, 50)
li_t2 = np.linspace(845, 1500, 50)


t = tk.StringVar()


def plot():
    temp = inp1.get()
    ratio = float(frame.get())
    if not temp.isdigit() or float(temp) < 0 or float(temp) > 1500:
        messagebox.showinfo("Error in temperature value",
                            "It should lie between 0-1500 kelvin")
    else:
        plt.figure(figsize=(8, 7))
        plt.plot(li_t2, fuc(li_t2, 69.25, 64900, 1))
        plt.plot(li_t1, fuc(li_t1, 89.2, 101800, 4))
        plt.plot(li_t2, fuc(li_t2, 6.65, 12300, 1))
        plt.plot(float(temp), ratio, marker="*",
                 markersize=25, label="User-Input-Data")
        plt.ylabel(r'$\frac{P(H_2)}{P(H_2)+P(H_2O)}$', fontsize=14)
        plt.xlabel(r'$Temperature(K)$', fontsize=14)
        plt.title(r'Output For UserInput Data', fontweight="bold")
        plt.legend()
        plt.annotate(r"$ Fe \ stable$", xy=(0.75, 0.85),
                     xycoords="axes fraction", fontsize=10)
        plt.annotate(r"$ FeO \ stable$", xy=(0.72, 0.42),
                     xycoords="axes fraction", fontsize=10)
        plt.annotate(r"$Fe_3O_4 \ stable$", xy=(0.15, 0.55),
                     xycoords="axes fraction", fontsize=10)
        plt.grid(True, linewidth=1.1, color='#ffffff', linestyle='-')
        plt.axes().set_facecolor("#f0f6ff")
        plt.show()
    t.set("")


label1 = tk.Label(root, text="Enter the Temperature in kelvin", font=10,)
inp1 = tk.Entry(root, bd=3, textvariable=t, font=10)

label2 = tk.Label(root, text=r"Set P(H2)/(P(H2)+P(H2O))", font=10,)
frame = tk.Scale(root, from_=0, to=1,
                 orient=tk.HORIZONTAL, resolution=0.001, length=200, width=16, font=12)
frame.set(0.4)

b1 = tk.Button(root, font=18, text="Plot Stability Curve",
               bg="green", fg="white", command=plot)

label3 = tk.Label(
    root, text="(User Input will be marked in the plot as '*' star mark and \n You can determine in which stability Region it falls)", font=("Arial", 12))

label1.pack(side=tk.TOP, pady=10)
inp1.pack(side=tk.TOP, pady=5)

label2.pack(side=tk.TOP, pady=10)
frame.pack(side=tk.TOP, pady=5)
b1.pack(side=tk.TOP, pady=8)
label3.pack(side=tk.TOP, pady=30)
root.mainloop()
