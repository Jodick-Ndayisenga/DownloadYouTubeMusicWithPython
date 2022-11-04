from pytube import YouTube

from sys import argv

name = str(input('Hi, what is your name, please? '))

while True:

    argv = input('drope the link of the video you want to download here: ')

    link = argv

    Video = YouTube(link)
    print('')
    print('The title of the song you are trying to download is: ', Video.title)

    print('This song has ', Video.views, 'views.')

    The_quality_to_download = Video.streams.get_highest_resolution()
    print('')
    print('wait for a while, your song is now downloading...')

    The_quality_to_download.download(
        'c:/Users/PC/Desktop/USB Drive/Programming/Youtube download.py')
    print('')
    print('the video has been successfully downloaded. Please find it in c:/Users/PC/Desktop/USB Drive/Programming/Youtube download')

    print('Thank you', name, 'for using our program. Wanna download again?')
    print('')
    continue
