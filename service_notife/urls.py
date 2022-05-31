from django.urls import path

from . import views, api

urlpatterns = [
    path('', views.index),
    # добаляем клиента
    path('api/clients', api.ClientListAPIView.as_view()),
    # добаляем клиента
    path('api/client', api.ClientCreateAPIView.as_view()),
    # обновления данных атрибутов клиента
    path('api/client/update/<int:pk>', api.ClientUpdateAPIView.as_view()),
    # удаления клиента из справочника
    path('api/client/remove/<int:pk>', api.ClientRemoveAPIView.as_view()),
    # добавления новой рассылки со всеми её атрибутами
    path('api/mailing', api.MailingCreateAPIView.as_view()),
    # получения общей статистики по созданным рассылкам и количеству отправленных сообщений по ним с группировкой по статусам
    path('api/mailings', api.MailingListAPIView.as_view()),
    # получения детальной статистики отправленных сообщений по конкретной рассылке
    path('api/mailing/<int:pk>', api.MailingDetailAPIView.as_view()),
    # обновления атрибутов рассылки
    path('api/mailing/update/<int:pk>', api.MailingUpdateAPIView.as_view()),
    # удаления рассылки
    path('api/mailing/remove/<int:pk>', api.MailingRemoveAPIView.as_view()),
    # обработки активных рассылок и отправки сообщений клиентам
    path('api/mailing/start/<int:pk>', views.index),

    # тест для запрос API
    path('api/test/', views.test_request_api),
    path('api/start/', views.chec_start_message),
]
