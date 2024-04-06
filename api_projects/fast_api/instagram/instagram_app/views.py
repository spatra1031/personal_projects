from django.shortcuts import render
import requests

def get_media(request):
    token = 'your token'
    url = 'https://graph.instagram.com/me/media?fields=id,caption&access_token='+token
    
   #response = requests.get(url,)
   # data = response.json()
    all_media = []
   # output = []
    """for media in all_media:
        media_id = media["id"]
        media_uri = 'https://graph.instagram.com/'+media_id+'?fields=id,media_type,media_url,username,timestamp&access_token='+token
        response = requests.get(media_uri,)
        media_data = response.json()
        media["url"] = media_data["media_url"]
        media["type"] = media_data["media_type"]
        media["username"] = media_data["username"]
        media["timestamp"] = media_data["timestamp"]"""

    
    return render (request, 'instagram.html', { "all_media": all_media} )
