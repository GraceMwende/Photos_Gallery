from django.shortcuts import render
from django.http import HttpResponse,Http404
# Create your views here.

def welcome(request):
  return HttpResponse('Welcome to gallery')

def test(request):
  test1 = 'grace'
  html = f'''
        <html>
        <body>
        <h1>Hi {test1}</h1>
        </body>
        </html>
        
  '''
  return HttpResponse(html)

def amazing(request):
  test2 = 'Mwesh'
  html = f'''
        <html>
        <body>
        <h1>Hi {test2}</h1>
        </body>
        </html>
        
  '''
  return HttpResponse(html)

def wuueh(request):
  try:
    t = 'hello'

  except ValueError:
    #raise 404 when valueError is thrown
    raise Http404()