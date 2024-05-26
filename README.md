1.Проект "Автотесты".
 2.В файл "sender_stand_request.py" импортируем модули (requests,configuration,data).
 3.Создаем файл для всех теста (create_order_test.py).
 4.Создаем заказ в файле "sender_stand_request.py"
 5.В файле configuration.py
 7.Устанавливаем pytest, requests
 6.Запускаем тест:
 -В поле выбора конфигурации выбери пункт Edit Configurations.
 -В открывшемся окне нажми значок «+» (Add New Configuration).
 -В списке конфигураций выбери Python tests → pytest.
 -По умолчанию в строке Target выбрано Script path. Оставь выбор без изменений.
 -В поле под строкой Target выбери файл с твоими тестами.
 -Нажми кнопку Apply, а затем OK.
 -Запусти созданную конфигурацию с помощью зелёной стрелки и посмотри результат: