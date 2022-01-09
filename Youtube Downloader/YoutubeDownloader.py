from pytube import YouTube

formatcont = input('Video or Audio: ')

if ((formatcont == 'Video') or (formatcont == 'video')):
    link = input('Enter the link: ')
    yt = YouTube(link)
    print('')
    print('Title: '+yt.title)
    print('Lenght: ',yt.length)
    print('')
    print('Download started!')
    ys = yt.streams.get_highest_resolution()
    ys.download('C:/Users/Dell/Desktop')
    print('')
    print('Download complete!')
elif ((formatcont == 'Audio') or (formatcont == 'audio')):
    link = input('Enter the link: ')
    yt = YouTube(link)
    print('')
    print('Title: '+yt.title)
    print('Lenght: ',yt.length)
    print('')
    print('Download started!')
    ys = yt.streams.get_audio_only()
    ys.download('C:/Users/Dell/Desktop')
    print('')
    print('Download complete!')
else:
    exit()