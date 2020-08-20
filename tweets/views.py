from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

def index(request, *args, **kwargs):
    context = {}
    template_name = 'index.html'
    return render(request, template_name, context)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    context = {
        "id": tweet_id,
        "content": obj.content,
        # "image_path": obj.image.url,

    }
    template_name = 'index.html'
    return JsonResponse(context)