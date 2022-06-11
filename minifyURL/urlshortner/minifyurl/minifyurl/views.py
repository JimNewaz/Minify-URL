from django.http import HttpResponse
from django.shortcuts import redirect, render
import uuid

from .models import url

def home(request):
    return render(request, 'minifyurl/index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = url(link=link,uid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = url.objects.get(uid=pk)
    return redirect(url_details.link)