from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
    return Response(f"hello, {name}")