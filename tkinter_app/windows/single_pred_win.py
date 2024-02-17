import tkinter
from tkinter import ttk
from functions.prediction import predict

def change_entry_height(entry_widget, new_height):
    style = ttk.Style()
    style.configure("TEntry", fieldbackground="white", font=("Helvetica", new_height))  # Adjust font size
    entry_widget.config(font=("Helvetica", new_height))  # Also set font size for compatibility with some themes

def single_predict(root):
    frame = tkinter.Toplevel(root)
    frame.title("Single row prediction")

    # Car Info Frame
    car_info_frame = ttk.LabelFrame(frame, text="Car Information", )
    car_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10, columnspan=3)  # Adjusted columnspan
    car_info_label_style = ttk.Style(car_info_frame)
    car_info_label_style.configure("TLabelFrame", font=("Helvetica", 96))  # Adjust the font size as needed

    style = ttk.Style()
    #style.configure('TButton', font=('Arial', 96), padding=5)
    style.theme_use('clam')
    style.configure("TButton", foreground="black", background="lightgrey", font=("Helvetica", 12), padding=10)
    style.configure("TLabel", foreground="black", background="lightgrey", font=("Helvetica", 12), padding=10)
    style.configure("TFrame", background="lightgrey")
    style.configure("TCombobox", foreground="black", background="white", font=("Helvetica", 12), padding=10)
    style.configure("Treeview", foreground="black", background="white", font=("Helvetica", 12), padding=10)
    style.configure("Treeview", foreground="black", background="white", font=("Helvetica", 12), padding=10)
    style.configure("TEntry", font=("Helvetica", 14))  # Increase font size for entry widgets


    labels = ["Trip duration", "Average speed", "Max acceleration", "Max angular speed",
            "Average pitch", "Average roll", "Average yaw", "No. of years exp.",
            "Gender", 'Driver rating', 'Driver age', "Car age"]
    
    # label_new = ['second_max', 'Speed_mean', 'net_acc_max', 'net_gyro_max', 'pitch_mean',
    #    'No_of_Years_driving_exp', 'gender', 'driver_rating', 'driver_age',
    #    'car_age', 'roll_yaw_mean']

    entries = {}
    gender_var = tkinter.StringVar(car_info_frame)

    for i, label in enumerate(labels):
        ttk.Label(car_info_frame, text=label, font=('Helvetica', 14)).grid(row=i, column=0, sticky=tkinter.W, padx=5, pady=5)

        # if is a gender entry, then will be a radio button instead of textbox
        if label == 'Gender':
            entry_1 = ttk.Radiobutton(car_info_frame, text="Male", variable=gender_var, value=1)
            entry_2 = ttk.Radiobutton(car_info_frame, text="Female", variable=gender_var, value=0)
            entries[label] = gender_var
            entry_1.grid(row=i, column=1, sticky=tkinter.W, padx=2, pady=5)
            entry_2.grid(row=i, column=1, sticky=tkinter.E, padx=2, pady=5)

        else:
            entry = ttk.Entry(car_info_frame)
            change_entry_height(entry, 20)
            entries[label] = entry
            entry.grid(row=i, column=1, sticky=tkinter.E, padx=5, pady=5)
        
    # Buttons Frame
    buttons_frame = ttk.Frame(frame)
    buttons_frame.grid(row=1, column=0, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S), pady=10, columnspan=1, padx=100)  # Adjusted columnspan

    # Buttons
    predict1_button = ttk.Button(buttons_frame, text="Predict", command=lambda: predict(entries))

    predict1_button.grid(row=0, column=0, padx=5)