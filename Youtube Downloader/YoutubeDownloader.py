from pytube import YouTube
import PySimpleGUI as sg

sg.theme('DarkBlue14')
sg.set_options(font=('JetBrains Mono', 11))


def gui(layout1):
    window = sg.Window('Youtube Downloader', layout1)
    while True:
        event, values1 = window.read()

        if event in (sg.WINDOW_CLOSED, 'Cancel', 'Close'):
            exit()

        if event in ('Submit', 'Ok'):
            break
    window.close()

    return values1


layout = [[sg.Text('Paste the URL below')],
          [sg.InputText(key='url')],
          [sg.Text('Video or audio?')],
          [sg.Combo(['Video', 'Audio'], default_value='Video', key='format', readonly=True)],
          [sg.Button('Submit'), sg.Button('Cancel')]]

values = gui(layout)
file_format = values['format']

# noinspection PyBroadException
try:
    yt = YouTube(values['url'])
except:
    print('Connection Error!')
    exit()

layout = [[sg.Text(f'Title: {yt.title}')],
          [sg.Text(f'Number of views: {yt.views}')],
          [sg.Text(f'Length of video: {yt.length} seconds')],
          [sg.Button('Ok')]]

gui(layout)

if file_format == 'Video':
    ys = yt.streams.get_highest_resolution()
elif file_format == 'Audio':
    ys = yt.streams.get_audio_only()
else:
    print('Error!')
    exit()

ys.download()

layout = [[sg.Text('Done!')], [sg.Button('Close')]]
gui(layout)
