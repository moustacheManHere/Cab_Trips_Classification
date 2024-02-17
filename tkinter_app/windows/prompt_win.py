from tkinter import Toplevel, Label, Button
from tkinter.filedialog import asksaveasfilename
import pandas as pd
import os

# if user picked "save" then overwrite the data
def save(win : Toplevel, df : pd.DataFrame, file_path : str):
    if file_path.split('.')[1] == 'csv':
        df.to_csv(file_path, index=False)
    else:
        df.to_excel(file_path, index=False)
    win.destroy()

# if user picked "save as" then will show the thing to display where to save the file
def save_as(win : Toplevel, df : pd.DataFrame):
    win.destroy()
    file_name = asksaveasfilename(filetypes=[("CSV files", ".csv")])
    print(file_name)
    # check file extension and then save
    df.to_csv(file_name, index=False)

def messageWindow(df : pd.DataFrame, file_path : str):
    win = Toplevel()
    win.title('Saving results')
    Label(win, text='Do you want to save the results?', padx=5, pady=10).pack()
    Button(win, text='Save', command = lambda : save(win, df, file_path), pady=2).pack()
    Button(win, text='Save as', command = lambda : save_as(win, df), pady=2).pack()
    Button(win, text='Cancel', command=win.destroy, pady=2).pack()