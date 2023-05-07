import serial
import pandas as pd

serialCom = serial.Serial(port='COM4', baudrate=9600, timeout=1)

dataFrame = pd.DataFrame()

def getData():
    serialCom.write(b'g')
    data = serialCom.readline().decode()
    return data.strip()

while 1:
    file = pd.read_excel('glove2.xlsx')
    col = file.shape[0]
    if col > 0:
        dataFrame = file
    user_input = input('Enter your input please: ')
    if user_input == 'del':
        last_input = dataFrame.index.stop - 1
        print(f'{dataFrame.iloc[-1, :]} Deleted')
        dataFrame = dataFrame.drop(index=last_input)
    elif user_input == 'show':
        print(dataFrame)
    else:
        data = f'{getData()},{user_input}'.split(',')
        print(data)
        new_data = pd.DataFrame({
        'Flex1': [data[0]],
        'Flex2': [data[1]],
        'Flex3': [data[2]],
        'Flex4': [data[3]],
        'Flex5': [data[4]],
        'gx': [data[5]],
        'gy': [data[6]],
        'gz': [data[7]],
        'ax': [data[8]],
        'ay': [data[9]],
        'az': [data[10]],
        'letter': [data[11]],
        })
        dataFrame = dataFrame.append(new_data, ignore_index=True)

    with pd.ExcelWriter('glove.xlsx') as xls:
        dataFrame.to_excel(xls, sheet_name='glove', index=False)