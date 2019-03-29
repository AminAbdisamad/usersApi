from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers


# Create your views here.


class Welcome(APIView):
    def get(self, request, format=None):
        text = [
            "Welcome to Django rest framework",
            "This framework allows you to write rest apis very simply",
        ]
        return Response({"message": text})


class Add(APIView):
    # Serializer class
    serializer_class = serializers.TestSerializer

    def post(self, request):
        serializer = serializers.TestSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get("name")
            email = serializer.data.get("email")
            message = f"Hello {name}, we'll contact you at {email}"
            return Response({"message": message})
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
