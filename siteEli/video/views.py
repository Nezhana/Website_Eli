from django.shortcuts import render
from .models import Video
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    allVideos = Video.objects.all()
    paginator = Paginator(allVideos, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'video/video.html', {'allVideos': allVideos, 'page_obj': page_obj})
