import gdshortener
import PySimpleGUI as sg
import requests

sg.theme('DarkBlue14')

def GUIButton(layout):
    global values
    window = sg.Window('URL Shortener', layout)
    while True:
        event, values = window.read()

        if event in (None, 'Cancel'):
            exit()

        if event == 'Submit':
            break
    window.close()

layout = [[sg.Text('Select a service to use below')],
          [sg.Combo(['shrtcode', 'is.gd', 'v.gd'], default_value='shrtcode', key='service', readonly=True)],
          [sg.Button('Submit'), sg.Button('Cancel')]]

GUIButton(layout)

service = values['service']

if service == 'is.gd' or service == 'v.gd':
    layout = [[sg.Text('Paste the URL below')],
              [sg.InputText(key='url')],
              [sg.Text('Enter the custom URL below')],
              [sg.InputText(key='custom_url')],
              [sg.Button('Submit'), sg.Button('Cancel')]]
elif service == 'shrtcode':
    layout = [[sg.Text('Paste the URL below')],
              [sg.InputText(key='url')],
              [sg.Button('Submit'), sg.Button('Cancel')]]
else:
    print('Error!')
    exit()

GUIButton(layout)

if service == 'is.gd' or service == 'v.gd':
    if service == 'is.gd':
        s = gdshortener.ISGDShortener()
    elif service == 'v.gd':
        s = gdshortener.VGDShortener()
    else:
        print('Error!')
        exit()
    
    s.shorten(values['url'], values['custom_url'])

    layout = [[sg.Text('Your shorter URL:'),
               sg.InputText(service+'/'+values['custom_url'], readonly=True)],
              [sg.Button('Close')]]
    window = sg.Window('URL Shortener', layout)
    event, values = window.read()
    window.close()
elif service == 'shrtcode':
    x = requests.post('https://api.shrtco.de/v2/shorten', params = {'url': values['url']})
    data = x.json()

    layout = [[sg.Text('Your shorter URL:')],
              [sg.InputText(data['result']['short_link'], readonly=True)],
              [sg.InputText(data['result']['short_link2'], readonly=True)],
              [sg.Button('Close')]]
    window = sg.Window('URL Shortener', layout)
    event, values = window.read()
    window.close()
else:
    print('Error!')