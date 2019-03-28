from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class Welcome(APIView):
    def get(self, request, format=None):
        text = [
            "Welcome to Django rest framework",
            "This framework allows you to write rest apis very simply",
        ]
        return Response({"message": text})


class ListAll(APIView):
    def get(self, request, format=None):
        text = {
            "You have to prepare something",
            "you have to cook something",
            "you have to make dirnks",
        }
        return Response({"Info": text})
