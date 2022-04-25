from itertools import count
from pydoc import describe
from django.shortcuts import render
from .models import Video
from .forms import Videoform
import moviepy.editor
from django.shortcuts import render
import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests
import os
from django.conf import settings
def videos(request):

    searchvalue=''

    form= Videoform(request.POST or None)
    if form.is_valid():
        searchvalue= form.cleaned_data.get("search")

    searchresults= Video.objects.filter(name__icontains= searchvalue)
    desc = Video.objects.filter(description__contains = searchvalue)
    timestamp = []
    result = zip(searchresults,timestamp)
    res = zip(desc,timestamp)
    if (len(searchvalue) > 0):
        for deal in searchresults:
            # if count == total:  

                path = os.path.join(settings.MEDIA_ROOT,str(deal.videofile))
                # path = path.split('/')
                # path = (path[-1])
                video = moviepy.editor.VideoFileClip(path)
                audio = video.audio
                audio.write_audiofile("PMD.mp3")
                print("Completed!")
                apikey = "4NJsFT-Ld-x_0DTd1gQuN2XZmQHM3dAH0nQWPCZJzX2h"
                url = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/1f389e2e-d71f-43e4-8f83-a32b55337335"
                authenticator = IAMAuthenticator(apikey)
                stt = SpeechToTextV1(authenticator=authenticator)
                stt.set_service_url(url)
                with open("././PMD.mp3","rb") as f:
                    res=stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', inactivity_timeout=-1, timestamps=True).get_result()
                    print(res)
                    timestamp.append(res)
                os.remove("././PMD.mp3")

                    
            # print(res)
            # data=res  
        
    #     return render(request,'home.html',{'data':data})
      
    context= {'form': form,
              'searchresults': searchresults,
              'desc' : desc,
              'timestamp': timestamp,
              'result' : result,
              'res' : res,
              }
    return render(request, 'base.html', context)

# def timestamp(request):
#     searchvalue=''
#     form= Videoform(request.POST or None)
#     if form.is_valid():
#         searchvalue= form.cleaned_data.get("search")
#     searchresults= Video.objects.filter(name__icontains= searchvalue)
#     desc = Video.objects.filter(description__contains = searchvalue)
#     print(searchresults)
#     for deal in searchresults:
#         path = str(deal.videofile)
#         # path = path.split('/')
#         # path = (path[-1])
#         video = moviepy.editor.VideoFileClip(path)
#         audio = video.audio
#         audio.write_audiofile("PMD.mp3")
#         print("Completed!")
#         apikey = "4NJsFT-Ld-x_0DTd1gQuN2XZmQHM3dAH0nQWPCZJzX2h"
#         url = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/1f389e2e-d71f-43e4-8f83-a32b55337335"
#         authenticator = IAMAuthenticator(apikey)
#         stt = SpeechToTextV1(authenticator=authenticator)
#         stt.set_service_url(url)
#         with open("E:\search\PMD.mp3","rb") as f:
#             res=stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', inactivity_timeout=-1, timestamps=True).get_result()
#             print(res)
#         os.remove("ChangedFile.csv")
#             data=res  
        
        # return render(request,'home.html',{'data':data})