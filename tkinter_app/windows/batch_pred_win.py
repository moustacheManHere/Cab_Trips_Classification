import tkinter
from tkinter import ttk, filedialog
from functions.prediction import batch_predict
from functions.tree_view import update_tree_view

def browse_excel(tree_view):
    # Open a file dialog to select an Excel file
    global file_path_xlsx
    file_path_xlsx = filedialog.askopenfilename(filetypes=[("Excel files", ".xls;.xlsx"), ("CSV files", ".csv")])

    # Display the selected file path (optional)
    if file_path_xlsx:
        print(f"Selected file: {file_path_xlsx}")

        # Update the treeview with the content of the Excel file
        update_tree_view(tree_view, file_path_xlsx)


def batch_predict_window(root):
    # Create a new window for batch prediction
    batch_window = tkinter.Toplevel(root)
    batch_window.title("Batch Prediction")

    # Create a treeview to display the content of the selected Excel file
    tree_view = ttk.Treeview(batch_window)
    tree_view.pack(pady=10, padx=10, fill='both', expand=True)

    # Create a button to browse and select an Excel file
    browse_button = ttk.Button(batch_window, text="Browse Excel/CSV", command=lambda : browse_excel(tree_view))
    browse_button.pack(pady=10)

    # Create a scrollbar for the treeview
    scrollbar_y = ttk.Scrollbar(batch_window, orient="vertical", command=tree_view.yview)
    scrollbar_y.pack(side="right", fill="y")
    tree_view.configure(yscrollcommand=scrollbar_y.set)

    scrollbar_x = ttk.Scrollbar(batch_window, orient="horizontal", command=tree_view.xview)
    scrollbar_x.pack(side="bottom", fill="x")
    tree_view.configure(xscrollcommand=scrollbar_x.set)

    # Create a button to perform batch prediction
    batch_predict_button = ttk.Button(batch_window, text="Batch Predict", command=lambda: batch_predict(tree_view, file_path_xlsx))
    batch_predict_button.pack(pady=10)