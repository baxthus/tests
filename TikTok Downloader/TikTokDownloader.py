import os
import platform
import subprocess
import PySimpleGUI as sg
from TikTokApi import TikTokApi

sg.theme('DarkBlue14')
sg.set_options(font=('JetBrains Mono', 11))


def gui(layout1):
    window = sg.Window('TikTok Downloader', layout1)
    while True:
        event, values1 = window.read()

        if event in (sg.WINDOW_CLOSED, 'Cancel', 'Close'):
            exit()

        if event == 'Submit':
            break

        if event == 'Open file':
            if platform.system() == 'Darwin':  # macOS
                subprocess.call(('open', 'video.mp4'))
            elif platform.system() == 'Windows':  # Windows
                os.startfile('video.mp4')
            else:  # Linux variants
                subprocess.call(('xdg-open', 'video.mp4'))
            exit()
    window.close()

    return values1


layout = [[sg.Text('Paste the URL below')],
          [sg.InputText(key='url')],
          [sg.Button('Submit'), sg.Button('Cancel')]]

values = gui(layout)

api = TikTokApi.get_instance()
video = api.get_video_by_url(values['url'])

with open('video.mp4', 'wb') as out:
    out.write(video)

layout = [[sg.Text('Done!')], [sg.Button('Open file'), sg.Button('Close')]]
gui(layout)
