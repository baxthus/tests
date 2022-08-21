import json

import PySimpleGUI as sg
import requests
import pyperclip

sg.theme('DarkBlue14')
sg.set_options(font=('JetBrains Mono', 11))


def gui(layout1, url, url2):
    window = sg.Window('URL Shortener', layout1)
    while True:
        event, values1 = window.read()

        if event == 'Cancel' or event == 'Close' or event == sg.WINDOW_CLOSED:
            exit()

        if event == 'Submit':
            break

        if event == 'Copy' or event == 'Copy URL 1':
            pyperclip.copy(url)
        if event == 'Copy URL 2':
            pyperclip.copy(url2)
    window.close()

    return values1


def layout_final(final_url1):
    layout2 = [[sg.Text('Your shorter URL: '),
                sg.InputText(final_url1, readonly=True)],
               [sg.Button('Copy'), sg.Button('Close')]]

    return layout2


layout = [[sg.Text('Select a service to use below')],
          [sg.Combo(['is.gd', 'v.gd', 'shrtcode', 'da.gd', 'ttm.sh', 'envs.sh', 'ulvis.net', 'gotiny.css'],
                    default_value='is.gd', key='service', readonly=True)],
          [sg.Button('Submit'), sg.Button('Cancel')]]

values = gui(layout, None, None)
service = values['service']

service_type1 = ['is.gd', 'v.gd', 'da.gd', 'ulvis.net', 'gotiny.css']
service_type2 = ['shrtcode', 'ttm.sh', 'envs.sh']

if service in service_type1:
    layout = [[sg.Text('Paste the URL below')],
              [sg.InputText(key='url')],
              [sg.Text('Enter the custom URL below (leave in blank to random)')],
              [sg.InputText(key='custom_url')],
              [sg.Button('Submit'), sg.Button('Cancel')]]
elif service in service_type2:
    layout = [[sg.Text('Paste the URL below')],
              [sg.InputText(key='url')],
              [sg.Button('Submit'), sg.Button('Cancel')]]
else:
    print('Error!'); exit()

values = gui(layout, None, None)

if service in ('is.gd', 'v.gd'):
    if values['custom_url'] == '':
        x = requests.get(f'https://{service}/create.php', params={'format': 'simple', 'url': values['url']})
    else:
        x = requests.get(f'https://{service}/create.php', params={'format': 'simple', 'url': values['url'],
                                                                  'shorturl': values['custom_url']})

    final_url = x.text

    layout = layout_final(final_url)
    gui(layout, final_url, None)
elif service == 'shrtcode':
    x = requests.post('https://api.shrtco.de/v2/shorten', params={'url': values['url']})
    data = x.json()

    final_url = data['result']['short_link']
    final_url2 = data['result']['short_link2']

    layout = [[sg.Text('Your shorter URL:')],
              [sg.Text('URL 1: '), sg.InputText(final_url, readonly=True)],
              [sg.Text('URL 2: '), sg.InputText(final_url2, readonly=True)],
              [sg.Button('Copy URL 1'), sg.Button('Copy URL 2'), sg.Button('Close')]]

    gui(layout, final_url, final_url2)
elif service in ('ttm.sh', 'envs.sh'):
    x = requests.post(f'https://{service}', data={'shorten': values['url']})
    final_url = x.text

    layout = layout_final(final_url)
    gui(layout, final_url, None)
elif service == 'da.gd':
    if values['custom_url'] == '':
        x = requests.get('https://da.gd/s', params={'url': values['url']})
    else:
        x = requests.get('https://da.gd/s', params={'url': values['url'], 'shorturl': values['custom_url']})

    final_url = x.text

    layout = layout_final(final_url)
    gui(layout, final_url, None)
elif service == 'ulvis.net':
    if values['custom_url'] == '':
        x = requests.get('https://ulvis.net/api.php', params={'url': values['url'], 'private': 1})
    else:
        x = requests.get('https://ulvis.net/api.php', params={'url': values['url'], 'custom': values['custom_url'],
                                                              'private': 1})

    final_url = x.text

    layout = layout_final(final_url)
    gui(layout, final_url, None)
elif service == 'gotiny.css':
    if values['custom_url'] == '':
        x = requests.post('https://gotiny.cc/api', headers={'Content-Type': 'application/json'},
                          json={'long': values['url']})
        data = x.json()
        for entry in data:
            final_url = 'gotiny.cc/' + entry['code']
    else:
        x = requests.post('https://gotiny.cc/api', headers={'Content-Type': 'application/json'},
                          json={'long': values['url'], 'custom': values['custom_url']})
        final_url = 'gotiny.cc/' + values['custom_url']

    layout = layout_final(final_url)
    gui(layout, final_url, None)
