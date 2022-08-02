from TikTokApi import TikTokApi
import PySimpleGUI as sg

sg.theme('DarkBlue14')

layout = [[sg.Text('Paste the URL below')],
          [sg.InputText(key='url')],
          [sg.Button('Submit'), sg.Button('Cancel')]]

window = sg.Window('TikTok Downloader', layout)
while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        exit()
    
    if event == 'Submit':
        break
window.close()

api = TikTokApi.get_instance()

video = api.get_video_by_url(values['url'])

with open('video.mp4', 'wb') as out:
    out.write(video)

window = sg.Window('', [[sg.Text('Done!')], [sg.Button('Close')]])
event, values = window.read()
window.close()