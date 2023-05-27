Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
git clone git@github.com:aten88/create_order.git
cd create_order

Cоздать и активировать виртуальное окружение установить Python 3.9:
py -3.9 -m venv venv
source venv/Scripts/activate

Обновить pip
python.exe -m pip install --upgrade pip

Установить зависимости из файла requirements.txt:
pip install -r requirements.txt

Создать конфигурационный файл в головном каталоге проекта с ключами API secrets.cfg
Поместить в константы: API_KEY и API_SECRET токены

Запустить проект:
app.run локально или используя серверы приложений, такие как Gunicorn или uWSGI

Запустить тесты:
python -m unittest tests.py