from django.shortcuts import render
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from . import models


class UserProfileView(APIView):
    # Serializer class
    serializer_class = serializers.UserProfileSerializer

    def get(self, request, format=None):
        query = models.UserProfile.objects.all()
        serializer = serializers.UserProfileSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     if serializer.is_valid():
    #         name = serializer.data.get("name")
    #         email = serializer.data.get("email")
    #         message = f"Hello {name}, we'll contact you at {email}"
    #         return Response({"message": message})
    #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserProfileDetial(APIView):
    serializer_class = serializers.UserProfileSerializer

    def create_object(self, pk):
        try:
            return models.UserProfile.objects.get(pk=pk)
        except models.UserProfile.DoesNotExist:
            raise Http404

    # getting one user
    def get(self, request, pk):
        userId = self.create_object(pk)
        serializer = serializers.UserProfileSerializer(userId)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # updating a user
    def put(self, request, pk):
        userId = self.create_object(pk)
        serializer = serializers.UserProfileSerializer(userId, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Deleting a user
    def delete(self, request, pk):
        useId = self.get_object(pk)
        useId.delete()
        return Response(
            {"Message": "Deleted Sucessfully"}, status=status.HTTP_204_NO_CONTENT
        )


class FeedView(APIView):

    serializer_class = serializers.FeedSerializer

    def get(self, request, format=None):
        query = models.Feed.objects.all()
        serializer = serializers.FeedSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.FeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpeakerView(APIView):
    serializer_class = serializers.SpeakerSerializer

    def get(self, request):
        query = models.Speaker.objects.all()
        serializer = serializers.SpeakerSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.SpeakerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Session(APIView):
    serializer_class = serializers.SessionSerializer

    def get(self, request):
        query = models.Session.objects.all()
        serializer = serializers.SessionSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SessionDetail(APIView):
    serializer_class = serializers.SessionSerializer

    def get_object(self, pk):
        try:
            return models.Session.objects.get(pk=pk)
        except models.Session.DoesNotExist:
            raise Http404

    # Getting one session
    def get(self, request, _id):
        id = self.get_object(_id)
        serializer = serializers.SessionSerializer(id)
        return Response(serializer.data)

    # update specific id
    def put(self, request, _id):
        sessionId = self.get_object(_id)
        serializer = serializers.SessionSerializer(sessionId, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, _id):
        sessionId = self.get_object(_id)
        sessionId.delete()
        return Response(
            {"Message": "Deleted Sucessfully"}, status=status.HTTP_204_NO_CONTENT
        )

