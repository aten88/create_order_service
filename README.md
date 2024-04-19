# Create Order Service
## Описание проекта:
Сервис формирования ордеров на покупку или продажу торговых пар Binance через API интрефейс
## Установка и запуск проекта:
- Клонировать репозиторий и перейти в него в командной строке:
  ```
  git clone git@github.com:aten88/create_order_service.git
  ```
  ```
  cd create_order_service
  ```

- Cоздать и активировать виртуальное окружение установить Python 3.9:
  ```
  py -3.9 -m venv venv
  ```
  ```
  source venv/Scripts/activate
  ```

- Обновить pip и установить зависимости из файла requirements.txt:
 ```
 python.exe -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

- Создать конфигурационный файл в головном каталоге проекта с ключами API secrets.cfg
  Поместить в константы: API_KEY и API_SECRET токены

- Запустить проект:
  ```
  app.run
  ```
  локально или используя серверы приложений, такие как Gunicorn или uWSGI

- Запустить тесты:
  ```
  python -m unittest tests.py
  ```
### Автор: Алексей Тен.
