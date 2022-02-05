# Abysmal - abysmal26.github.io
# HyPeRiS Group

import gdshortener

servico = input('is.gd ou v.gd: ')

if servico == 'is.gd':
    url = input('Digite a url: ')
    custom_url = input('Digite a url customizada: ')
    s = gdshortener.ISGDShortener()
    s.shorten(url, custom_url)
    print('is.gd/' + custom_url)
elif servico == 'v.gd':
    url = input('Digite a url: ')
    custom_url = input('Digite a url customizada: ')
    s = gdshortener.VGDShortener()
    s.shorten(url, custom_url)
    print('v.gd/' + custom_url)
else:
    print('ERRO!')
    exit()