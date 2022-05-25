# Abysmal - abysmal26.github.io - ayo.so/abysmal26
# HyPeRiS Group

import gdshortener

servico = input('is.gd ou v.gd: ')

if servico == 'is.gd':
    url = input('Enter the URL: ')
    custom_url = input('Enter the custom URL: ')
    s = gdshortener.ISGDShortener()
    s.shorten(url, custom_url)
    print('is.gd/' + custom_url)
elif servico == 'v.gd':
    url = input('Enter the URL: ')
    custom_url = input('Enter the custom URL: ')
    s = gdshortener.VGDShortener()
    s.shorten(url, custom_url)
    print('v.gd/' + custom_url)
else:
    print('ERROR!')
    exit()