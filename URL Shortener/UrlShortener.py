import gdshortener
import PySimpleGUI as sg

sg.theme('DarkBlue14')

layout = [[sg.Text('Select a service to use below')],
          [sg.Combo(['is.gd', 'v.gd'], default_value='is.gd', key='service', readonly=True)],
          [sg.Text('Paste the URL below')],
          [sg.InputText(key='url')],
          [sg.Text('Enter the custom URL below')],
          [sg.InputText(key='custom_url')],
          [sg.Button('Submit'), sg.Button('Cancel')]]

window = sg.Window('URL Shortener', layout)
while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        exit()

    if event == 'Submit':
        break
window.close()

if (values['service'] == 'is.gd'):
    s = gdshortener.ISGDShortener()
elif (values['service'] == 'v.gd'):
    s = gdshortener.VGDShortener()
else:
    print('Error!')

s.shorten(values['url'], values['custom_url'])

layout = [[sg.Text('Your shorter URL:'),
           sg.InputText(values['service']+'/'+values['custom_url'], readonly=True)],
          [sg.Button('Close')]]
window = sg.Window('URL Shortener', layout)
event, values = window.read()
window.close()