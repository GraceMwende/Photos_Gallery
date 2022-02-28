from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Location,Category,Image
# Create your views here.

def all_img(request):
  images = Image.display_images()
  return render(request, 'all.html',{"images":images,})

def test(request):
  test1 = 'grace'
  return render(request, 'location.html',{"test":test,})

def amazing(request):
  test2 = 'Mwesh'
  return render(request,'search.html',{"test":test2})
def wuueh(request):
  try:
    t = 'hello'

  except ValueError:
    #raise 404 when valueError is thrown
    raise Http404()