def loadData():
    import pandas as pd
    data = pd.read_csv("data/Diamonds Prices2022.csv")
    data = data.drop(["Unnamed: 0"], axis=1)
    return data

def preprocessingData(data):
    from sklearn import preprocessing

    le = preprocessing.LabelEncoder()

    data["cut"] = le.fit_transform(data["cut"])
    data["color"] = le.fit_transform(data["color"])
    data["clarity"] = le.fit_transform(data["clarity"])
    
    X = data.iloc[:, [0, 1, 2, 3, 4, 5, 7, 8, 9]]

    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(missing_values = 0.0, strategy ='mean')
    data['x'] = imputer.fit_transform(data[['x']])
    data['y'] = imputer.fit_transform(data[['y']])
    data['z'] = imputer.fit_transform(data[['z']])
    
    X = imputer.fit_transform(X)

    min_max_scaler = preprocessing.MinMaxScaler()
    X = min_max_scaler.fit_transform(X)

    y = data.price
    return X, y

def trainModel(X, y):
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.model_selection import train_test_split
    import sklearn.metrics as sm
    import numpy as np

    result = {
        'r2' : [],
        'mse' : [],
        'mae' : [],
    }

    model = DecisionTreeRegressor()
    model.fit(X, y)

    #y_pred = model.predict(X_test)

    #result['r2'].append(sm.r2_score(y_test, y_pred))
    #result['mse'].append(sm.mean_squared_error(y_test, y_pred))
    #result['mae'].append(sm.mean_absolute_error(y_test, y_pred))
    return model, result

cut_val = {
    'Fair' : 0,
    'Good' : 1,
    'Ideal' : 2,
    'Premium' : 3,
    'Very good' : 4
}

color_val = {
    'D' : 0,
    'E' : 1,
    'F' : 2,
    'G' : 3,
    'H' : 4,
    'I' : 5,
    'J' : 6
}

clarity_val = {
    'I1' : 0,
    'IF' : 1,
    'SI1' : 2,
    'SI2' : 3,
    'VS1' : 4,
    'VS2' : 5,
    'VVS1' : 6,
    'VVS2' : 7
}

data = loadData()
X, y = preprocessingData(data)
model, training_result = trainModel(X, y)

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()

root.option_add('*Dialog.msg.font', 'Helvetica 20')

import tkinter.font as tkFont
bigfont = tkFont.Font(family="Helvetica",size=18)
root.option_add("*TCombobox*Listbox*Font", bigfont)

cbb = ttk.Combobox(root, justify='center')
cbb.option_add('*TCombobox*Listbox.Justify', 'center')

window_width = 1280
window_height = 720

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.columnconfigure(6, weight=1)
root.columnconfigure(7, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)
root.rowconfigure(8, weight=1)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.title('Diamonds Price Prediction')

carat = tk.StringVar()
carat.set(0.0)
carat_entry = ttk.Entry(root, textvariable=carat, font=("Helvetica", 15), justify='center')

depth = tk.StringVar()
depth.set(0.0)
depth_entry = ttk.Entry(root, textvariable=depth, font=("Helvetica", 15), justify='center')

table = tk.StringVar()
table.set(0.0)
table_entry = ttk.Entry(root, textvariable=table, font=("Helvetica", 15), justify='center')

x = tk.StringVar()
x.set(0.0)
x_entry = ttk.Entry(root, textvariable=x, font=("Helvetica", 15), justify='center')

y = tk.StringVar()
y.set(0.0)
y_entry = ttk.Entry(root, textvariable=y, font=("Helvetica", 15), justify='center')

z = tk.StringVar()
z.set(0.0)
z_entry = ttk.Entry(root, textvariable=z, font=("Helvetica", 15), justify='center')

cut = tk.StringVar()
cut_cb = ttk.Combobox(root, textvariable=cut, font=("Helvetica", 15), justify='center')
cut_cb['values'] = ['Fair', 'Good', 'Very good', 'Premium', 'Ideal']
cut_cb['state'] = 'readonly'
cut_cb.set('Fair')

color = tk.StringVar()
color_cb = ttk.Combobox(root, textvariable=color, font=("Helvetica", 15), justify='center')
color_cb['values'] = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
color_cb['state'] = 'readonly'
color_cb.set('D')

clarity = tk.StringVar()
clarity_cb = ttk.Combobox(root, textvariable=clarity, font=("Helvetica", 15), justify='center')
clarity_cb['values'] = ['I1', 'IF', 'SI1', 'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2']
clarity_cb.config(font=("Helvetica", 15))
clarity_cb['state'] = 'readonly'
clarity_cb.set('I1')

title_label = ttk.Label(root, text='DIAMONDS PRICE PREDICTION')
title_label.config(font=("Helvetica", 50))

owner_label = ttk.Label(root, text='A product of Nguyen Phuc Vinh An (B2007167) and Tran Quang Vinh (B2007218)')
owner_font = tkFont.Font(family='Helvetica', size=18)
owner_label.config(font=owner_font)

carat_label = ttk.Label(root, text='Carat')
carat_label.config(font=("Helvetica", 15))

cut_label = ttk.Label(root, text='Cut')
cut_label.config(font=("Helvetica", 15))

color_label = ttk.Label(root, text='Color')
color_label.config(font=("Helvetica", 15))

clarity_label = ttk.Label(root, text='Clarity')
clarity_label.config(font=("Helvetica", 15))

depth_label = ttk.Label(root, text='Depth')
depth_label.config(font=("Helvetica", 15))

table_label = ttk.Label(root, text='Table')
table_label.config(font=("Helvetica", 15))

x_label = ttk.Label(root, text='X')
x_label.config(font=("Helvetica", 15))

y_label = ttk.Label(root, text='Y')
y_label.config(font=("Helvetica", 15))

z_label = ttk.Label(root, text='Z')
z_label.config(font=("Helvetica", 15))

def callErrorMessageBox(text):
    from tkinter import Message
    msg = Message(text=text, font=('Helvetica', 14))
    msg.config(justify='center', width=600, background='red', fg='white')
    msg.grid(column=1, columnspan=4, row=7, sticky=tk.NSEW, padx=(170,0))

def callMessageBox(text):
    from tkinter import Message
    msg = Message(text=text, font=('Helvetica', 14))
    msg.config(justify='center', width=600)
    msg.grid(column=1, columnspan=4, row=7, sticky=tk.NSEW, padx=(170,0))

def showError(name, reason):
    warning = "\u26A0"
    msg = f'{warning} {name.capitalize()} has invalid value. {reason}.'
    callErrorMessageBox(text=msg)
    #showinfo(title='Error', message=msg)

def preprocessingInput(name, value):
    try:
        _value = float(value)
    except:
        showError(name, 'Value is not a number')
        return   
    return (_value - data[name].min())/(data[name].max() - data[name].min())

def checkValid():
    try:
        if carat.get() == '' or float(carat.get()) <= 0 :
            showError('carat', 'Value is 0, empty or negative')
            return False
        if depth.get() == '' or float(depth.get()) <= 0:
            showError('depth', 'Value is 0, empty or negative')
            return False
        if table.get() == '' or float(table.get()) <= 0:
            showError('table', 'Value is 0, empty or negative')
            return False
        if x.get() == '' or float(x.get()) <= 0:
            showError('x', 'Value is 0, empty or negative')
            return False
        if y.get() == '' or float(y.get()) <= 0:
            showError('y', 'Value is 0, empty or negative')
            return False
        if z.get() == '' or float(z.get()) <= 0:
            showError('z', 'Value is 0, empty or negative')
            return False
    except:
        showError('A field(s)', 'Input must be a number')
        return False
    return True

def getInput():
    if (checkValid()):
        try:
            _carat = preprocessingInput('carat', carat.get())
            _cut = preprocessingInput('cut', cut_val[cut.get()])
            _color = preprocessingInput('color', color_val[color.get()])
            _clarity = preprocessingInput('clarity', clarity_val[clarity.get()])
            _depth = preprocessingInput('depth', depth.get())
            _table = preprocessingInput('table', table.get())
            _x = preprocessingInput('x', x.get())
            _y = preprocessingInput('y', y.get())
            _z = preprocessingInput('z', z.get())
        
            print([_carat, _cut, _color, _clarity, _depth, _table, _x, _y, _z])

        except:
            showError('Some field', 'unknow')
            return [], False
    else:
        return [], False
    
    import numpy as np
    return np.array([_carat, _cut, _color, _clarity, _depth, _table, _x, _y, _z]), True

def submit_clicked():
    input, status = getInput()
    
    if (not(status)):
        return
        
    price = model.predict([input])

    msg = f'Predicted price: {price[0]}$.'
    callMessageBox(msg)
    
def reset_clicked():
    carat.set(0.0)
    cut.set('Fair')
    color.set('D')
    clarity.set('I1')
    depth.set(0.0)
    table.set(0.0)
    x.set(0.0)
    y.set(0.0)
    z.set(0.0)
    
    callMessageBox('')



title_label.grid(column=1, columnspan=6, row=1, sticky=tk.S)
owner_label.grid(column=1, columnspan=6, row=2, sticky=tk.N)

carat_label.grid(column=1, row=3, padx=(100, 0), pady=(0, 10))
carat_entry.grid(column=2, columnspan=5, row=3, padx=(0, 100), sticky=tk.NSEW, pady=(0, 10))

cut_label.grid(column=1, row=4, padx=(100, 0), pady=(0, 10))
cut_cb.grid(column=2, row=4, sticky=tk.NSEW, pady=(0, 10))
color_label.grid(column=3, row=4, pady=(0, 10))
color_cb.grid(column=4, row=4, sticky=tk.NSEW, pady=(0, 10))
clarity_label.grid(column=5, row=4, pady=(0, 10))
clarity_cb.grid(column=6, row=4, padx=(0, 100), sticky=tk.NSEW, pady=(0, 10))

depth_label.grid(column=1, row=5, padx=(100, 0), pady=(0, 10))
depth_entry.grid(column=2, columnspan=2, row=5, sticky=tk.NSEW, pady=(0, 10))
table_label.grid(column=4, row=5, pady=(0, 10))
table_entry.grid(column=5, columnspan=2, row=5, padx=(0, 100), sticky=tk.NSEW, pady=(0, 10))

x_label.grid(column=1, row=6, padx=(100, 0), pady=(0, 10))
x_entry.grid(column=2, row=6, sticky=tk.NSEW, pady=(0, 10))
y_label.grid(column=3, row=6, pady=(0, 10))
y_entry.grid(column=4, row=6, sticky=tk.NSEW, pady=(0, 10))
z_label.grid(column=5, row=6, pady=(0, 10))
z_entry.grid(column=6, row=6, sticky=tk.NSEW, padx=(0,100), pady=(0, 10))

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 15))

reset_btn = ttk.Button(root, text='Reset', command=reset_clicked, style='my.TButton')
reset_btn.grid(column=5, row=7, sticky=tk.NSEW, padx=(5,10))

submit_btn = ttk.Button(root, text='Submit', command=submit_clicked, style='my.TButton')
submit_btn.grid(column=6, row=7, sticky=tk.NSEW, padx=(0, 100))

root.mainloop()