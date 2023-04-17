# Сервис "Куда пойти"

Интерактивная карта Москвы для поиска мест активного отдыха с подробными описаниями и комментариями.

![image](https://user-images.githubusercontent.com/67222917/232372815-357224c2-cac0-46bc-aea2-d3beb217f8eb.png)

## Запуск

Для запуска у вас уже должен быть установлен Python 3.

1. Скачайте код
2. Установите зависимости командой `pip install -r requirements.txt`
3. Настройте переменные окружения:

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.
Доступны следущие переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
- `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).

4. Создайте базу данных SQLite командой `python3 manage.py migrate`
5. Запустите сервер командой `python3 manage.py runserver`

После этого переходите по ссылке [127.0.0.1:8000](http://127.0.0.1:8000), вы увидите главную страницу.

## Настройки сайта

Внизу справа на странице можно включить отладочный режим логгирования.

![image](https://user-images.githubusercontent.com/67222917/232372973-6eeb3c41-cfa7-491e-b9fa-516fd3ef9cf0.png)

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки, удалите ключи из Local Storage с помощью Chrome Dev Tools —> Вкладка Application —> Local Storage.

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логгирования.
