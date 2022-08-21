import PySimpleGUI as sg
import requests
import webbrowser

sg.theme('DarkBlue14')
sg.set_options(font=('JetBrains Mono', 11))
sg.set_options()

x = requests.get('https://disease.sh/v3/covid-19/all')
data = x.json()

cases = data['cases']
today_cases = data['todayCases']
deaths = data['deaths']
today_deaths = data['todayDeaths']
recovered = data['recovered']
today_recovered = data['todayRecovered']

layout = [[sg.Text('Covid-19 Data')],
          [sg.Text('Data provided by'), sg.Text('disease.sh', click_submits=True, key='-LINK-')],
          [sg.HorizontalSeparator()],
          [sg.Text(f'Cases:           {cases}')],
          [sg.Text(f'Today cases:     {today_cases}')],
          [sg.Text(f'Deaths:          {deaths}')],
          [sg.Text(f'Today deaths:    {today_deaths}')],
          [sg.Text(f'Recovered:       {recovered}')],
          [sg.Text(f'Today recovered: {today_recovered}')],
          [sg.Button('Close')]]

window = sg.Window('Covid-19 Data', layout)
while True:
    event, values = window.read()

    if event == '-LINK-':
        webbrowser.open('https://disease.sh')

    if event in ('Close', sg.WINDOW_CLOSED):
        exit()
