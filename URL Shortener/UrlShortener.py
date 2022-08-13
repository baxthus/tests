import gdshortener
import PySimpleGUI as sg
import requests
import pyperclip

sg.theme('DarkBlue14')
sg.set_options(font=('JetBrans Mono', 11))

def GUIButton(layout):
    global values
    window = sg.Window('URL Shortener', layout)
    while True:
        event, values = window.read()

        if event == 'Cancel' or event == sg.WINDOW_CLOSED:
            exit()
        
        if event == 'Submit':
            break
    window.close()

def GUIButton2(layout, final_url, final_url2):
    window = sg.Window('URL Shortener', layout)
    while True:
        event, values = window.read()

        if event == 'Close' or event == sg.WINDOW_CLOSED:
            exit()

        if event == ('Copy') or event == ('Copy URL 1'):
            pyperclip.copy(final_url)
        
        if event == ('Copy URL 2'):
            pyperclip.copy(final_url2)

layout = [[sg.Text('Select a service to use below')],
          [sg.Combo(['shrtcode', 'ttm.sh', 'is.gd', 'v.gd'], default_value='shrtcode', key='service', readonly=True)],
          [sg.Button('Submit'), sg.Button('Cancel')]]

GUIButton(layout)

service = values['service']

if service == 'is.gd' or service == 'v.gd':
    layout = [[sg.Text('Paste the URL below')],
              [sg.InputText(key='url')],
              [sg.Text('Enter the custom URL below')],
              [sg.InputText(key='custom_url')],
              [sg.Button('Submit'), sg.Button('Cancel')]]
elif service == 'shrtcode' or service == 'ttm.sh':
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

    final_url = service+'/'+values['custom_url']

    layout = [[sg.Text('Your shorter URL:'),
               sg.InputText(final_url, readonly=True)],
              [sg.Button('Copy'), sg.Button('Close')]]
    
    GUIButton2(layout, final_url, None)
elif service == 'shrtcode':
    x = requests.post('https://api.shrtco.de/v2/shorten', params = {'url': values['url']})
    data = x.json()

    final_url = data['result']['short_link']
    final_url2 = data['result']['short_link2']

    layout = [[sg.Text('Your shorter URL:')],
              [sg.Text('URL 1: '), sg.InputText(final_url, readonly=True)],
              [sg.Text('URL 2: '), sg.InputText(final_url2, readonly=True)],
              [sg.Button('Copy URL 1'), sg.Button('Copy URL 2'), sg.Button('Close')]]
    
    GUIButton2(layout, final_url, final_url2)
elif service == 'ttm.sh':
    x = requests.post('https://ttm.sh', data={'shorten': values['url']})

    final_url = x.text

    layout = [[sg.Text('Your shorter URL: '),
               sg.InputText(final_url, readonly=True)],
              [sg.Button('Copy'), sg.Button('Close')]]
    
    GUIButton2(layout, final_url, None)
else:
    print('Error!')