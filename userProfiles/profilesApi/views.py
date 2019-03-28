from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers


# Create your views here.


class Welcome(APIView):
    # Serializer class
    serializer_class = serializers.TestSerializer

    def get(self, request, format=None):
        text = [
            "Welcome to Django rest framework",
            "This framework allows you to write rest apis very simply",
        ]
        return Response({"message": text})

    def post(self, request):
        serializer = serializers.TestSerializer(data=request.data)
        if serializer.is_valid:
            name = serializer.data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ListAll(APIView):
    def get(self, request, format=None):
        text = {
            "You have to prepare something",
            "you have to cook something",
            "you have to make dirnks",
        }
        return Response({"Info": text})
