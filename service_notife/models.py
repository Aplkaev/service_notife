from django.db import models

# Create your models here.

from django.db import models



class Mailing(models.Model):
    # уникальный id рассылки
    id = models.BigAutoField(primary_key=True)
    # дата и время запуска рассылки
    start_time = models.DateTimeField(auto_now=True)
    # текст сообщения для доставки клиенту
    message = models.TextField('Текст рассылки')
    # фильтр свойств клиентов, на которых должна быть произведена рассылка(код мобильного оператора, тег)
    tag = models.TextField('Тэг')
    # дата и время окончания рассылки: если по каким - то причина мне успели разослать все сообщения - никакие
    # сообщения клиентам после этого времени доставляться не должны
    end_time = models.DateTimeField(auto_now=True)


class Client(models.Model):
    # уникальный id клиента
    id = models.BigAutoField(primary_key=True)
    # номер телефона клиента в формате
    # 7XXXXXXXXXX (X - цифра от 0 до 9)
    phone = models.IntegerField()
    # код мобильного оператора
    code = models.IntegerField()
    # тег (произвольная метка)
    tag = models.TextField('Тэг')
    # часовой пояс
    time_zone = models.DateTimeField(auto_now=True)


class Message(models.Model):
    # уникальный id сообщения
    id = models.BigAutoField(primary_key=True)
    # дата и время создания (отправки)
    time = models.DateTimeField(auto_now=True)
    # статус отправки
    status = models.IntegerField()
    # id рассылки, в рамках которой было отправлено сообщение
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='+')
    # id клиента, которому отправили
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='+')
