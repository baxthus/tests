from TikTokApi import TikTokApi

api = TikTokApi.get_instance()

print("") # Opcional

url = input("Digite a url do video: ")

if url == 'sair':
    exit()

video = api.get_video_by_url(url)

with open("video.mp4", "wb") as out:
    out.write(video)

print("") # Opcional

print("Video salvo")

