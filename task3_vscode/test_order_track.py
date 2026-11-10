# Валерия Куликова, 49-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data
def test_get_order_by_track_success_response():
    # 1 Выполнить запрос на создание заказа.
    order_response = sender_stand_request.post_new_order(data.order_body)

    # 2 Сохранение номера трека заказа
    track_number = order_response.json()["track"]

    # 3 Выполнение запроса на получение заказа по треку заказа
    get_response = sender_stand_request.get_order_by_track(track_number)

      # 4 Проверка, что код ответа равен 200
    assert get_response.status_code == 200