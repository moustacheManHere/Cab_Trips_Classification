import tkinter
from tkinter import ttk
from functions.tree_view import update_tree_view
import pandas as pd
from tkinter import messagebox

def history(root):
    # Create a new window for history display
    history_window = tkinter.Toplevel(root)
    history_window.title("Prediction History")

    # Create a treeview to display the history
    history_tree = ttk.Treeview(history_window)
    history_tree.pack(pady=10, padx=10, fill='both', expand=True)

    # Create a scrollbar for the treeview
    scrollbar = ttk.Scrollbar(history_window, orient="vertical", command=history_tree.yview)
    scrollbar.pack(side="right", fill="y")
    history_tree.configure(yscrollcommand=scrollbar.set)

    scrollbar_x = ttk.Scrollbar(history_window, orient="horizontal", command=history_tree.xview)
    scrollbar_x.pack(side="bottom", fill="x")
    history_tree.configure(xscrollcommand=scrollbar_x.set)

    try:
        # try to get the csv, see if is empty
        df = pd.read_csv('.data/history.csv')
        # check if is empty
        if not len(df):
            messagebox.showwarning('Empty history', 'Your history is empty, there is nothing to show.')
        else:
            # Load and display the content of the storage.xlsx file
            update_tree_view(history_tree, df)
    
    # if the error is because of totally empty data when opening the csv, then yea
    except pd.errors.EmptyDataError:
        messagebox.showwarning('Empty history', 'Your history is empty, there is nothing to show.')
    
    except FileNotFoundError:
        messagebox.showwarning('Empty history', 'Your history is empty, there is nothing to show.')
