import pandas as pd
from tkinter import messagebox
import pickle
from functions.tree_view import update_tree_view
from windows.prompt_win import messageWindow
import os
import sklearn
import sklearn.compose
HISTORY_PATH = './.data/history.csv'

# Load the trained model from the pickle file
model_filename = '../pickles/model.pkl'  # Replace with your actual model file
with open(model_filename, 'rb') as file:
    loaded_model = pickle.load(file)

encoder_filename = '../pickles/transform.pkl'
with open(encoder_filename, 'rb') as f:
    transformer = pickle.load(f)

def predict(entries):

    # actual features used for scaling and predicting
    actual_labels = ['second_max', 'Speed_mean', 'net_acc_max', 'net_gyro_max', 'pitch_mean',
       'No_of_Years_driving_exp', 'gender', 'driver_rating', 'driver_age',
       'car_age', 'yaw_mean', 'roll_mean']
    
    # map from the tkinter variables to the actual feature name
    mapped_label = {
        "Trip duration" : 'second_max',
        "Average speed" : 'Speed_mean', 
        "Max acceleration" : 'net_acc_max', 
        "Max angular speed" : 'net_gyro_max', 
        "Average pitch" : 'pitch_mean',
        'Average roll' : 'roll_mean',
        'Average yaw' : 'yaw_mean',
        "No. of years exp." : 'No_of_Years_driving_exp', 
        "Driver rating" : 'driver_rating', 
        "Driver age" : 'driver_age', 
        'Car age' : 'car_age',
        'Gender' : 'gender'
    }

    # swapped, because it should've been the other way round, oops
    mapped_label_swapped = {v: k for k, v in mapped_label.items()}

    values = {}
    try:
            # iterate through the actual labels, get the mapped column name to get the value and extract it
        for actual_label in actual_labels:
            values[actual_label] = float(entries[mapped_label_swapped[actual_label]].get())
        print(values)
        
        # turn into pandas dataframe, transform the roll and yaw, then scale and predict
        df_values = pd.DataFrame([values])

        df_values['roll_yaw_mean'] = (df_values['roll_mean']**2 + df_values['yaw_mean'] **2)**0.5
        df_values = df_values.drop(columns=['roll_mean', 'yaw_mean'])

        scaled_values = transformer.transform(df_values)
        prediction = loaded_model.predict(scaled_values)
    
    except Exception as e:
        print(e)
        messagebox.showinfo('Error', 'Invalid input(s)!')
        return
    
    # Display the prediction
    print(prediction)
    messagebox.showinfo("Prediction", f"This trip is predicted to be {'' if prediction else 'not '}dangerous.")

    # attempt concatenate the prediction and time stamp into df
    prediction = pd.Series(prediction, name='label')
    prediction = prediction.map({0: 'not dangerous', 1: 'dangerous'})
    pred_time = pd.Series([pd.to_datetime('now')], name='prediction_time')

    df = pd.concat([df_values, prediction, pred_time], axis=1)
    df.to_csv(HISTORY_PATH, mode='a', header=not os.path.exists(HISTORY_PATH), index=False)  # if history file doesn't exists, then add header, or else no need


def batch_predict(tree_view, file_path):
        
    if not file_path:
        messagebox.showerror("Invalid File", "Please select an Excel or CSV file.")
        return

    try:
        # Load the Excel file
        if file_path.split('.')[1] == 'csv':
            df = pd.read_csv(file_path)
        elif file_path.split('.')[1] == 'xlsx':
            df = pd.read_excel(file_path) 
        else:
            raise ValueError('Invalid file type, must be either csv or excel sheet.')
        
        # rearrange the columns as needed
        actual_labels = ['second_max', 'Speed_mean', 'net_acc_max', 'net_gyro_max', 'pitch_mean',
            'No_of_Years_driving_exp', 'gender', 'driver_rating', 'driver_age',
            'car_age', 'yaw_mean', 'roll_mean']
        
        df = df[actual_labels]

        df['roll_yaw_mean'] = (df['roll_mean']**2 + df['yaw_mean'] **2)**0.5
        df = df.drop(columns=['roll_mean', 'yaw_mean'])

        scaled_values = transformer.transform(df)
        predictions = pd.Series(loaded_model.predict(scaled_values), name='label')    # predict and then turn into a pandas series so it can combine with the data

        # Map 0 to "not dangerous" and 1 to "dangerous"
        predictions = predictions.map({0: 'not dangerous', 1: 'dangerous'})

        # get the current time and then concatenate to the dataset as well
        current_time_series = pd.Series([pd.to_datetime('now')] * len(predictions), name='prediction_time')

        # concatenate the data with the prediction, and then update tree view again with the results
        df_w_preds = pd.concat([df, predictions, current_time_series], axis=1)
        update_tree_view(tree_view, df_w_preds)

        # tell user about the successful prediction
        messagebox.showinfo('Batch Predictions successful', f'{len(predictions)} rows prediction made.')

        # and then ask user whether they want to save the whole dataset with the predictions
        messageWindow(df_w_preds, file_path)
        
        df_w_preds.to_csv(HISTORY_PATH, mode='a', header=not os.path.exists(HISTORY_PATH), index=False)


    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"An error occurred: {str(e)}")