# Наталья Бобылева, 16-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request

def test_positive_assertion_code_200():
    order_response = sender_stand_request.post_new_order(data.order_body)
    track = {"t": order_response.json()["track"]}
    response_order_by_track = sender_stand_request.get_order_track(track)
    assert response_order_by_track.status_code == 200

