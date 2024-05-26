# Наталья Бобылева, 16-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

#создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                            json=body)

#получение заказа по номеру трека
def get_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH, params=track)



