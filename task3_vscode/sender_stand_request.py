# Валерия Куликова, 49-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

def post_new_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        headers=data.HEADERS
    )
def get_order_by_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params={"t": track}
    )
