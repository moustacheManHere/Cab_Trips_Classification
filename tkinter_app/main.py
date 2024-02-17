import tkinter
from tkinter import ttk
from windows.single_pred_win import single_predict
from windows.batch_pred_win import batch_predict_window
from windows.history_win import history

root = tkinter.Tk()
root.title("Car Data Prediction")
# root.resizable(False, False)

home = ttk.Frame(root, padding="20")
home.grid(row=0, column=0, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S))

# Buttons Frame
buttons_frame = ttk.Frame(home)
buttons_frame.grid(row=3, column=0, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S), pady=10, rowspan=3, padx=100)  # Adjusted columnspan

# Buttons
prediction_win = ttk.Button(buttons_frame, text="Predict", command=lambda: single_predict(root))
batch_win = ttk.Button(buttons_frame, text="Batch Predict", command=lambda : batch_predict_window(root))
history_win = ttk.Button(buttons_frame, text="History", command=lambda : history(root))

prediction_win.grid(row=1, column=0, padx=5, pady=5)
batch_win.grid(row=2, column=0, padx=5, pady=5)
history_win.grid(row=3, column=0, padx=5, pady=5)

root.mainloop()