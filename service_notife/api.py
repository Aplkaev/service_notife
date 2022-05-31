from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from . import serializers
from . import models
from rest_framework.parsers import FormParser, MultiPartParser


class MailingListAPIView(ListAPIView):
    # получения общей статистики по созданным рассылкам
    # и количеству отправленных сообщений по ним с группировкой по статусам
    serializer_class = serializers.MailingSerializer

    def get_queryset(self):
        return models.Mailing.objects.all()


class MailingCreateAPIView(CreateAPIView):
    # добавления новой рассылки со всеми её атрибутами
    serializer_class = serializers.MailingSerializer

    def get_queryset(self):
        return models.Mailing.objects


class MailingDetailAPIView(RetrieveAPIView):
    # получения детальной статистики отправленных сообщений по конкретной рассылке
    serializer_class = serializers.ClientSerializer

    def get_queryset(self):
        return models.Mailing.objects.filter(draft=False)


class MailingUpdateAPIView(UpdateAPIView):
    # обновления атрибутов рассылки
    serializer_class = serializers.ClientSerializer


class MailingRemoveAPIView(DestroyAPIView):
    # удаления рассылки
    serializer_class = serializers.ClientSerializer


class MailingStartAPIView(UpdateAPIView):
    # обработки активных рассылок и отправки сообщений клиентам
    serializer_class = serializers.ClientSerializer


# class MessageListAPIView(ListAPIView):
#     serializer_class = serializers.MessageSerializer
#
#     def get_queryset(self):
#         return models.Message.objects.all()
#
#
# class ClientListAPIView(ListAPIView):
#     serializer_class = serializers.ClientSerializer
#
#     def get_queryset(self):
#         return models.Client.objects.all()

class ClientListAPIView(ListAPIView):
    # список всех клиентов
    serializer_class = serializers.ClientSerializer

    def get_queryset(self):
        return models.Client.objects.all()


class ClientCreateAPIView(CreateAPIView):
    # добавления нового клиента в справочник со всеми его атрибутами
    serializer_class = serializers.ClientSerializer
    parser_classes = (FormParser, MultiPartParser)

    def get_queryset(self):
        return models.Client.objects


class ClientUpdateAPIView(UpdateAPIView):
    # обновления данных атрибутов клиента
    serializer_class = serializers.ClientSerializer

    def get_queryset(self):
        return models.Client.objects


class ClientRemoveAPIView(DestroyAPIView):
    # удаления клиента из справочника
    serializer_class = serializers.ClientSerializer

    def get_queryset(self):
        return models.Client.objects
