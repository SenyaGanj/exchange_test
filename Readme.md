## Exchange сервис

Приложение написано с помощью фреймфорка flask. 
В качестве БД ипользуется PostgreSQL. 
Для обращения к БД используется Flask-SQLAlchemy, 
для миграций Flask-Migrate. Для dev запуска используется Docker.

Для фронта используется шаблонизатор flask Bootstrap и js библиотеку plotly (js аналог Plotly-Dash).

### Логика работы

Контейнер deamon запускает скрипт, который раз в секунду обновляет цену для всех инструментов в БД.
Для простоты решения было решено не использовать celery beat, но при работате с большим количеством воркеров, взял бы его.

Контейнер flask запускает dev сервер. 
На фронте каждую секунду опрашивается сервер для получаения актуальной цены интрумента.

### Запуск

docker-compose build - собираем контейнеры
docker-compose run backend pipenv run flask db update - применяем миграции
docker-compose up -d - запускаем контейнеры