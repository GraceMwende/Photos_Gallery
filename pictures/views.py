from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Location,Category,Image
# Create your views here.

def all_img(request):
  images = Image.display_images()
  return render(request, 'all.html',{"images":images,})

def image(request,image_id):
  try:
    image = Image.objects.get(id = image_id)

  except DoesNotExist:
    raise Http404()
  return render(request, '',{"image":image,})

def search_results(request):

  if 'category' in request.GET and request.GET['category']:
    search_term  = request.GET.get("category")
    searched_categories = Image.search_by_category(search_term)
    message = f'{search_term}'

    return render(request,'search.html',{'message':message,'categories':searched_categories})

  else:
    message = "You have searched for any item"
    return render(request, 'search.html',{'message':message})