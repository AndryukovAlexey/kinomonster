import requests
import tempfile
from django.core import files

def soc_auth(backend, response, user=None, *args, **kwargs):
     
    url = None
    email = None
 
    if backend.name == 'google-oauth2':
        email = response.get('email', '')
        url = response.get('picture', '')
    
    if backend.name == 'vk-oauth2':
        email = response.get('screen_name', '')
        url = response.get('photo', '')

    if email:
        user.username = str(email).split('@')[0].replace('.', '')
        user.save()

    if url:
        response = requests.get(url, stream=True)
        if response.status_code == requests.codes.ok:
            file_name = url.split('/')[-1]
            lf = tempfile.NamedTemporaryFile()
            for block in response.iter_content(1024 * 8):
                if block:                
                    lf.write(block)
            user.profile.avatar.save(file_name, files.File(lf))
