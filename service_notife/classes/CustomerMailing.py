from ..models import Mailing, Client, Message
import requests
from datetime import datetime
import json


class CustomerMailing:
    _mailing: Mailing = None
    _is_time = True
    error = ''

    def __init__(self, id: int):
        """
            Создаем расслку для клентов
        :param id: индентификатор рассылки
        """
        self._mailing = Mailing.objects.get(pk=id)

    def _check_time(self) -> bool:
        """
            Проверка можно сейчас отправлять
        :return: false - не время, true - можно отправлять
        """
        is_start = self._mailing.start_time.timestamp() > datetime.now().timestamp()
        is_end = self._mailing.end_time.timestamp() < datetime.now().timestamp()
        if is_start or is_end:
            return False

    def _get_clients(self) -> list:
        """
        Получаем список клиентов с таким же тэгом
        :return: список id
        """
        clients = Client.objects.filter(tag=self._mailing.tag)
        return clients

    def _request_message(self, client: Client) -> dict:
        """
            Делаем запрос на стороний сервис и ждем ответа
        :param client: модель клиента
        :return: результат от сервиса {id:int, status:int}
        """
        response = None
        try:
            # запрос на другой сервис
            response = requests.post("http://127.0.0.1:8000/api/test/", data={
                'phone': client.phone,
                'message': self._mailing.message
            })
        except Exception as e:
            print('error response', e)
            return {}
        # если ответ не 200, то идем дальше
        if response.status_code != 200:
            return {}

        # получаем статус и id сообщения
        message = json.loads(response.text)
        if message['status'] == 'success':
            return message
        return {}

    def _save_message(self, result: dict, client: Client) -> bool:
        """
            Сохраняем письмо
        :param result:  результат от сервиса {id:int, status:int}
        :param client:
        :return: результат сохранения
        """
        message = Message(
            time=datetime.now(),
            status=result['deliver'],
            mailing=self._mailing,
            client=client
        )
        message.save()

    def start(self) -> bool:
        """
        Запуск рассылки
        :return: результат запуска
        """
        if self._check_time():
            self.error = 'Не время запуска'
            return False

        clients = self._get_clients()
        for client in clients:
            result = self._request_message(client)
            # пришло теле результата
            if 'deliver' in result:
                self._save_message(result, client)

    def get_mailing(self):
        """
        Вернем mailing
        :return: mailing
        """
        return self._mailing
