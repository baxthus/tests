import gdshortener

url = input('Enter the URL: ')
custom_url = input('Enter the custom URL: ')

service = input('is.gd or v.gd: ')

if (service == 'is.gd' or service == 'is'):
    s = gdshortener.ISGDShortener()
    s.shorten(url, custom_url)
    print('is.gd/' + custom_url)
elif (service == 'v.gd' or service == 'v'):
    s = gdshortener.VGDShortener()
    s.shorten(url, custom_url)
    print('v.gd/' + custom_url)
else:
    print('Invalid input')