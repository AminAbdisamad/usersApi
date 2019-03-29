from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=200)
