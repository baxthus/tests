from pytube import YouTube

videoLink = input('Enter the link: ')

try:
    yt = YouTube(videoLink)
except:
    print('Connection Error')

print('')
print('Title: ', yt.title)
print('Number of views: ', yt.views)
print('Length of video: ', yt.length)

print('')
downType = input('Video or audio: ')

if (downType == 'Video' or downType == 'video'):
    ys = yt.streams.get_highest_resolution()
elif (downType == 'Audio' or downType == 'audio'):
    ys = yt.streams.get_audio_only()
else:
    print('Invalid input')

print()
print('Downloading...')
ys.download()
print('Download completed!')