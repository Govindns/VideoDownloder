from django.shortcuts import render

from pytube import *

def youtube(request):
    if request.method=='POST':
        link=request.POST['link']
        video=YouTube(link)
        down=video.streams.get_highest_resolution()
        down.download()
        return render(request, 'testapp/downloader.html')
    return render(request, 'testapp/downloader.html')
