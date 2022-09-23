import PySimpleGUI as sg
import requests


def gui(layout1):
    window = sg.Window('Covid Stats', layout1)
    while True:
        event, values1 = window.read()

        if event in ('Close', 'Cancel', sg.WINDOW_CLOSED):
            exit()

        if event == 'Submit':
            break
    window.close()

    return values1


sg.theme('DarkBlue14')
sg.set_options(font=('Inter', 11))

layout = [[sg.Text('Type the country below (leave in blank for worldwide)')],
          [sg.InputText(key='country')],
          [sg.Button('Submit'), sg.Button('Cancel')]]

values = gui(layout)
country = values['country']

if values['country'] != '':
    requests = requests.get(f'https://disease.sh/v3/covid-19/countries/{country}')
else:
    country = 'worldwide'
    requests = requests.get('https://disease.sh/v3/covid-19/all')

data = requests.json()

if 'message' in data:
    layout = [[sg.Text(f'{data["message"]}')],
              [sg.Button('Close')]]
    gui(layout)
else:
    layout = [[sg.Text(f'{country.capitalize()}')],
              [sg.HorizontalSeparator()],
              [sg.Text(f'Cases: {data["cases"]}')],
              [sg.Text(f'Today Cases: {data["todayCases"]}')],
              [sg.Text(f'Deaths: {data["deaths"]}')],
              [sg.Text(f'Today Deaths: {data["todayDeaths"]}')],
              [sg.Text(f'Recovered: {data["recovered"]}')],
              [sg.Text(f'Today Recovered: {data["todayRecovered"]}')],
              [sg.Button('Close')]]
    gui(layout)
