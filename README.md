# TICKER - тестовое задание
![график](https://drive.google.com/file/d/1Yp4b5TPOZFAE6BDrC8I-hgWBWSeEp-3U/view?usp=sharing "график")

Проект состоит из 3х модулей:
- ticker — каждую секунду обновляет в базе данных цены
- web — веб приложение на Dash, отображает в реальном времени изменение цен каждого инструмента
- db — общий модуль для работы с PostgreSQL

## Демо
Проверить работу проекта можно по ссылке https://208d-188-64-165-219.ngrok.io \
Там от ngrok есть предупреждение, нужно просто нажать "Visit site". \ 
Если не открывается, то также записал видео работы https://drive.google.com/file/d/1xBTkjw8QePb5cvyH1-Tm-IjrmNaV8CaD/view?usp=sharing

## Запуск
Все завернуто в Docker контейнеры. Чтобы запустить локально
```docker-compose up -d --build ```, в браузере http://localhost:8000
