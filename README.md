# Сайт доставки еды Star Burger

Это сайт сети ресторанов Star Burger. Здесь можно заказать превосходные бургеры с доставкой на дом.

![Работающая версия сайта](https://rofloburger.fun/)


Сеть Star Burger объединяет несколько ресторанов, действующих под единой франшизой. У всех ресторанов одинаковое меню и одинаковые цены. Просто выберите блюдо из меню на сайте и укажите место доставки. Мы сами найдём ближайший к вам ресторан, всё приготовим и привезём.

На сайте есть три независимых интерфейса. Первый — это публичная часть, где можно выбрать блюда из меню, и быстро оформить заказ без регистрации и SMS.

Второй интерфейс предназначен для менеджера. Здесь происходит обработка заказов. Менеджер видит поступившие новые заказы и первым делом созванивается с клиентом, чтобы подтвердить заказ. После оператор выбирает ближайший ресторан и передаёт туда заказ на исполнение. Там всё приготовят и сами доставят еду клиенту.

Третий интерфейс — это админка. Преимущественно им пользуются программисты при разработке сайта. Также сюда заходит менеджер, чтобы обновить меню ресторанов Star Burger.

## Как запустить dev-версию сайта

### Скачать код с репозитория

```sh
git clone https://github.com/EshiNanase/dockerized_starburger.git
```
### Установить Docker CLI

```sh
https://github.com/docker/cli
```
### В каталоге создать .env файл со следующими переменными окружения:

- `DEBUG` — дебаг-режим. Для разработки - `False`, для продакшена - `True`.
- `SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. Например, им зашифрованы все пароли на вашем сайте.
- `YANDEX_API_TOKEN` — персональный токен HTTTP Геокодера от Яндекс. Получить можно [здесь](https://developer.tech.yandex.ru/services)
- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `ROLLBAR_TOKEN` — токен вашего проекта на [Rollbar](https://rollbar.com)
- `ROLLBAR_ENVIRONMENT` — development, если для разработки, или production, если сайт на продакшене
- `POSTGRES_DB` — название базы данных Postgres
- `POSTGRES_USER` — имя юзера для входа в базу данных Postgres
- `POSTGRES_PASSWORD` — пароль для входа под именем юзера сверху

### Запустить разработческую версию в консоли
```sh
docker-compose up --build
```
### Открыть запущенный сайт в браузере по ссылке
```sh
http://127.0.0.1:8000/
```

## Как запустить prod-версию сайта

### В папке nginx/prod создать nginx_prod.conf со следующим содержанием

```sh
server {
    listen 80;
    server_name {ВАШ ДОМЕН};
    server_tokens off;

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name {ВАШ ДОМЕН};
    server_tokens off;

    ssl_certificate /etc/letsencrypt/live/{ВАШ ДОМЕН}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/{ВАШ ДОМЕН}/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        proxy_pass http://web:8000/;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }

    location /media/ {
         alias /app/media/;
    }

    location /static/ {
         alias /app/static/;
    }
}
```

### Получить SSL Сертификат от Certbot'а на сервер
```sh
https://certbot.eff.org/
```

### Запустить prod-версию в консоли
```sh
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build --remove-orphans
```

### Как быстро задеплоить код на сервере
- Перейти в директорию /opt/devman/dockerized_starburger
- Запустить ./starburger_deploy
