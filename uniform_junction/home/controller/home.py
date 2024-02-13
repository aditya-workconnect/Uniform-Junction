from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse

class HomeController(viewsets.ModelViewSet):

    def __init__(self):
        pass

    def home(self, request):
        response_data = {'data':'data'}
        return JsonResponse(response_data, status=201)
        

