from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import utc

from .models import Mailing
from time import sleep
import random
from datetime import datetime

from .classes.CustomerMailing import CustomerMailing


# Create your views here.


def index(request):
    return redirect('/swagger/')


@csrf_exempt
def test_request_api(request):
    """
        Тестовый метод для эмулации работы внешнего сервиса
    """
    rol_rand = random.randint(1, 10)
    # 10% сервис будет долго отдавать данные
    if rol_rand == 5:
        print('sleep 60')
        sleep(60)
    # 10% сервис выдаст ошибку
    elif rol_rand == 1:
        print('error')
        return JsonResponse({'status': 'false'}, status=500)

    return JsonResponse({
        'status': 'success',
        'deliver': 1,
        'id': int(datetime.now().timestamp())
    })

@csrf_exempt
def chec_start_message(request):
    m = Mailing.objects.filter(start_time__lte=datetime.utcnow().replace(tzinfo=utc),
                               end_time__gte=datetime.utcnow().replace(tzinfo=utc))
    ids = []
    for i in m:
        # logger.info("send_mailing"+str(i.id))
        mailing = CustomerMailing(i.id)
        mailing.start()
        ids.append(i.id)
        del mailing
    return JsonResponse({
        'item': ids
    })
