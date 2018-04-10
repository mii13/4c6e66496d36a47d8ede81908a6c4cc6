###System story
____________
 Приложение состоит из трех сервисов:
1. Сервис1 - админка, отвечает за взаимодействие с пользователем, хранение и отображение пользователю информации о введенных функциях и сгенерированных графиках.
2. Сервис2 - генератор данных, отвечает за генерацию данных для графика. Принимает текстовое описание функции, генерирует по ним массив [(x, y)].
3. Сервис3 - генератор изображений, генерирует изображение по подготовленным данным.

###Установка и Запуск (DEV)
____________
 - Установка программ (Ubuntu ):
 
     ```bash
        sudo apt update && apt install -y git apt docker.io docker-compose
     ```
        
 - Клонируем приложежение:
 
     ```bash
        git clone https://github.com/mii13/4c6e66496d36a47d8ede81908a6c4cc6.git project
      ```
        
 - Запуск:
    ```bash    
        cd project
        docker-compose up --build
    ```       
 - Доступ до админки:  
     ```bash
       docker-compose run admin-panel python manage.py createsuperuser
     ``` 
     ```
       url: http://localhost:8000/admin/
     ```  
     
 
 
 docker-compose environments:
 * POSTGRES_USER - Пользователь в Postgres
 * POSTGRES_PASSWORD - Пароль для пользователя POSTGRES_USER в Postgres
 * POSTGRES_DB - Бада в Postgres
 * RABBITMQ_DEFAULT_USER - Пользователь в RABBITMQ
 * RABBITMQ_DEFAULT_PASS - Пароль
 * RABBITMQ_DEFAULT_VHOST - Хост
 * COORDINATE_GENERATE_API_URL - url для генерации координат
 * IMAGE_GENERATE_API_URL - url для генерации графика
 * MEDIA_ROOT - MEDIA_ROOT для django
 * AMQP_CELERY_URL - url до amq
 * REDIS_CELERY_URL - url до redis
 * DATABASE_URL - url до postgress
        
 