import qrcode
import PySimpleGUI as sg

sg.theme('DarkBlue14')
sg.set_options(font=('JetBrains Mono', 11))

layout = [[sg.Text('Type the version below (1 to 10 that control the size)')],
          [sg.Combo(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], default_value='1', key='version', readonly=True)],
          [sg.Text('Select the QR Code color')],
          [sg.Combo(['Normal', 'Inverted'], default_value='Normal', key='color', readonly=True)],
          [sg.Text('Enter the data below')],
          [sg.InputText(key='data')],
          [sg.Button('Submit'), sg.Button('Cancel')]]

window = sg.Window('QR Code Generator', layout)
while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        exit()

    if event == 'Submit':
        break
window.close()

qr = qrcode.QRCode(version = values['version'])
qr.add_data(values['data'])
qr.make(fit = True)

if (values['color'] == 'Normal'):
    img = qr.make_image(fill_color = 'black', back_color = 'white')
elif (values['color'] == 'Inverted'):
    img = qr.make_image(fill_color = 'white', back_color = 'black')
else:
    print('Error!')
    exit()

img.save('QRCode.png')

window = sg.Window('', [[sg.Text('Done!')], [sg.Button('Close')]])
event, values = window.read()
window.close()