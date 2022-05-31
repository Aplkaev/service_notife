from . import models
from rest_framework import serializers


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mailing
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'
