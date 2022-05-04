# Abysmal - abysmal26.github.io - ayo.so/abysmal26
# HyPeRiS Group

from TikTokApi import TikTokApi

api = TikTokApi.get_instance()

print('') # Opcional

url = input('Digite a url do video: ')

video = api.get_video_by_url(url)

with open('video.mp4', 'wb') as out:
    out.write(video)

print('') # Opcional

print('Video salvo')
