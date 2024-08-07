# Проект Онлайн Обучения (Django REST framework)
В мире развивается тренд на онлайн-обучение.
В данном проекте представлена LMS-система, в которой каждый желающий может размещать свои полезные материалы или курсы.

Данный проект написан не фрейморке Django REST framework, с подключением реляционной базы данных "PostgreSQL"
Использовалось вирутальное окружение venv В проекте построено 3 модели БД:

1. Таблица "Users";
2. Таблица "Course";
3. Таблица "Lesson" прямая связь с "Course";
4. Таблица "Payments" прямая связь с "Course", "Lesson", "User";

В проекте Описан CRUD для моделей курса и урока.
Для реализации CRUD для курса (Course) и пользователей (User) использутся Viewsets, а для урока (Lesson) - Generic-классы,
Для работы с приложением использовалась программа "Postman"
Для запуска проекта необходимо сделать

1. Git clone репозитория
```
https://github.com/VadimPokhabov/DRF_project_24.git
```
2. Установить виртуальное окружение venv
```
python3 -m venv venv для MacOS и Linux систем

python -m venv venv для windows
```
3. Активировать виртуальное окружение
```
source venv/bin/activate для MasOs и Linux систем
venv\Scripts\activate.bat для windows
```
4. Установить файл с зависимостями
```
pip install -r requirements.txt
```
5. Создать базу данных в PgAdmin, либо через терминал. Необходимо дать название в файле settings.py в каталоге 'base' в константе (словаре) 'DATABASES'

6. Создать файл .env в корне проекта и заполнить следующие данные:
```
#Django
SECRET_KEY=

#DB_Settings
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

#API_KEY
STRIPE_API_KEY=

#message
EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER_MAIL=
EMAIL_HOST_PASSWORD_MAIL=

#celery
CELERY_BROKER_URL=
CELERY_BACKEND_URL=
```
Запуск приложения через Docker:

1. Повторить шаги 1-3
2. Запустить Docker локально на машине
3. Выполнить команду в терминале
```
docker compose up -d --build
```
Данная команда сразу создаст образ, и сбилдит его, т.е. запустит локально в Docker

4. Переходим по ссылке http://localhost:8000/

Чтобы удалить контейнеры после работы с приложением используйте команду
```
docker-compose down 
```
