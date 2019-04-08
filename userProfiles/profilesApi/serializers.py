from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.Serializer):
    #  We can define the fields we'll use with our serializer but instead we'll take advantage of
    #   UserProfile model that we have already created
    class Meta:
        """ We'll define What fields we'll take from our model """

        models = models.UserProfile
        fields = ("id", "name", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return models.UserProfile.objects.create(**validated_data)
        # """Create user  """
        # user = models.UserProfile(
        #     name=validated_data["name"], email=validated_data["email"]
        # )
        # user.set_password(validated_data["password"])
        # user.save()
        # return user


class FeedSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    description = serializers.CharField()

    def create(self, validated_data):
        return models.Feed.objects.create(**validated_data)


class SpeakerSerializer(serializers.Serializer):
    firstName = serializers.CharField(max_length=100)
    lastName = serializers.CharField(max_length=100)
    photo = serializers.ImageField(upload_to="speaker_images", blank=True)
    job_title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    created = models.DateTimeField(auto_now_add=True)

    def create(self, validated_data):
        return models.Speaker.objects.create(**validated_data)

