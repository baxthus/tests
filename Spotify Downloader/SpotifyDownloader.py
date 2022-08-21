import os
import PySimpleGUI as sg

sg.theme('DarkBlue14')
sg.set_options(font=('JetBrains Mono', 11))


def gui(layout1):
    window = sg.Window('Spotify Downloader', layout1)
    while True:
        event, values1 = window.read()

        if event in (sg.WINDOW_CLOSED, 'Cancel', 'Close'):
            exit()

        if event == 'Submit':
            break
    window.close()

    return values1


layout = [[sg.Text('Paste the URL below')],
          [sg.InputText(key='url')],
          [sg.Button('Submit'), sg.Button('Cancel')]]

values = gui(layout)

os.system(f'spotdl {values["url"]}')
os.remove('.spotdl-cache')

layout = [[sg.Text('Done!')], [sg.Button('Close')]]
gui(layout)
