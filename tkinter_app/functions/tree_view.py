import pandas as pd
from tkinter import messagebox

def update_tree_view(tree_view, data_source: str | pd.DataFrame):
    try:
        # check if is obtain the data from file path, or just a dataframe
        if isinstance(data_source, pd.DataFrame):
            df = data_source.copy(True)
        else:
            if data_source.split('.')[1] == 'csv':
                df = pd.read_csv(data_source)
            elif data_source.split('.')[1] == 'xlsx':
                df = pd.read_excel(data_source) 
            else:
                raise ValueError('Invalid file type, must be either csv or excel sheet.')

        # Clear existing treeview columns and items
        tree_view.delete(*tree_view.get_children())
        tree_view["columns"] = list(df.columns)
        tree_view["show"] = "headings"

        # Add header columns to treeview
        for col in df.columns:
            tree_view.heading(col, text=col)

        # Add data rows to treeview
        for _, row in df.iterrows():
            tree_view.insert("", "end", values=row.tolist())

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")