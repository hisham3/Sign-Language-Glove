import pandas as pd
from sklearn.svm import SVC
import serial
import numpy as np
import time
import pyttsx3

serialCom = serial.Serial(port='COM6', baudrate=9600, timeout=1)

def getData():
    serialCom.write(b'g')
    data = serialCom.readline().decode()
    return data.strip()

file = pd.read_excel('glove.xlsx')
X = file.iloc[:, :4].values
y = file.iloc[:, -1].values

last = 1

while 1:
    data = getData().split(',')
    if len(data) == 4 and last:
        data = np.array(list(map(int, data))).reshape(1,-1)

        SVCModel = SVC(C=1, kernel='linear', gamma=1, shrinking=True)
        SVCModel.fit(X, y)

        predicted_svc = SVCModel.predict(data)

        if last != predicted_svc:
            print(f'\r{predicted_svc[0]}', end='')
            engine = pyttsx3.init()
            engine.say(predicted_svc)
            engine.runAndWait()
            last = predicted_svc
            time.sleep(0.3)



