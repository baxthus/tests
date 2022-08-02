import os
import PySimpleGUI as sg

sg.theme('DarkBlue14')

layout = [[sg.Text('Paste the URL below')],
          [sg.InputText(key='url')],
          [sg.Button('Submit'), sg.Button('Cancel')]]

window = sg.Window('Spotify Downloader', layout)
while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        exit()

    if event == 'Submit':
        break
window.close()

os.system(f'spotdl {values["url"]}')
os.remove('.spotdl-cache')

window = sg.Window('', [[sg.Text('Done!')], [sg.Button('Close')]])
event, values = window.read()
window.close()