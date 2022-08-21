import PySimpleGUI as sg
import os
import platform
import qrcode
import subprocess

sg.theme('DarkBlue14')
sg.set_options(font=('JetBrains Mono', 11))


def gui(layout1):
    window = sg.Window('URL Shortener', layout1)
    while True:
        event, values1 = window.read()

        if event in ('Cancel', 'Close', sg.WINDOW_CLOSED):
            exit()

        if event == 'Submit':
            break

        if event == 'Open file':
            if platform.system() == 'Darwin':  # macOS
                subprocess.call(('open', 'QRCode.png'))
            elif platform.system() == 'Windows':  # Windows
                os.startfile('QRCode.png')
            else:  # Linux variants
                subprocess.call(('xdg-open', 'QRCode.png'))
            exit()
    window.close()

    return values1


layout = [[sg.Text('Type the version below (1 to 10 that control the size)')],
          [sg.Combo(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], default_value='1', key='version',
                    readonly=True)],
          [sg.Text('Select the QR Code color')],
          [sg.Combo(['Normal', 'Inverted'], default_value='Normal', key='color', readonly=True)],
          [sg.Text('Enter the data below')],
          [sg.InputText(key='data')],
          [sg.Button('Submit'), sg.Button('Cancel')]]

values = gui(layout)

qr = qrcode.QRCode(version=values['version'])
qr.add_data(values['data'])
qr.make(fit=True)

if values['color'] == 'Normal':
    img = qr.make_image(fill_color='black', back_color='white')
elif values['color'] == 'Inverted':
    img = qr.make_image(fill_color='white', back_color='black')

img.save('QRCode.png')

layout = [[sg.Text('Done!')],
          [sg.Button('Open file'), sg.Button('Close')]]

gui(layout)
