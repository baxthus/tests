from pytube import YouTube
import PySimpleGUI as sg

sg.theme('DarkBlue14')

layout = [[sg.Text('Paste the URL below')],
          [sg.InputText(key='url')],
          [sg.Text('Video or audio?')],
          [sg.Combo(['Video', 'Audio'], key='format', readonly=True)],
          [sg.Button('Submit'), sg.Button('Cancel')]]

window = sg.Window('YouTube Downloader', layout)
while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        exit()

    if event == 'Submit':
        break
window.close()

format = values['format']

try:
    yt = YouTube(values['url'])
except:
    print('Connection Error!')
    exit()

layout = [[sg.Text(' '.join(['Title: ', str(yt.title)]))],
          [sg.Text(' '.join(['Number of views: ', str(yt.views)]))],
          [sg.Text(' '.join(['Length of video: ', str(yt.length), ' seconds']))],
          [sg.Button('Ok')]]  
window = sg.Window('YouTube Downloader', layout)
event, values = window.read()
window.close()

if (format == 'Video'):
    ys = yt.streams.get_highest_resolution()
elif (format == 'Audio'):
    ys = yt.streams.get_audio_only()
else:
    print('Error!')
    exit()

ys.download()

window = sg.Window('', [[sg.Text('Done!')], [sg.Button('Close')]])
event, values = window.read()
window.close()