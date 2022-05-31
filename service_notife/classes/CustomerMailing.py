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
            response = requests.post("ttps://probe.fbrq.cloud/v1/send/", data={
                'id': '',
                'phone': client.phone,
                'text': self._mailing.message
            }, headers={
                'Authorization': 'access_token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODUwMjcwNjAsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkBhcGxrYWV2In0.mgmUkRQwY8sQbjeOXKwpgx1GeWAAj6-JQOAlOq_8v3Y'})
        except Exception as e:
            print('error response', e)
            return {}
        # если ответ не 200, то идем дальше
        if response.status_code != 200:
            return {}

        # получаем статус и id сообщения
        message = json.loads(response.text)
        message['code'] = response.status_code
        return message

    def _save_message(self, client: Client) -> bool:
        """
            Сохраняем письмо
        :param client:
        :return: результат сохранения
        """
        message = Message(
            time=datetime.now(),
            mailing=self._mailing,
            status=-1,
            client=client
        )
        message.save()
        return message

    def _update_message(self, message: Message, code: int) -> bool:
        """
        Обновляем код сообщения
        :param message:
        :param code:
        :return:
        """
        Message.objects.get(pk=message.id).update(status=code)

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
            message = self._save_message(client)
            result = self._request_message(client)
            if 'code' in result:
                self._update_message(message, result['code'])

    def get_mailing(self):
        """
        Вернем mailing
        :return: mailing
        """
        return self._mailing
