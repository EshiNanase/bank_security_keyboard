# Симулятор охранника в банке

Требуется установленный python3.9!

## Запуск

### Установите необходимые библиотеки

```shell-session
$ pip install -r requirements.txt
```

### Создайте .env со следующими переменными

`DATABASE_URL` -- адрес для подключения к базе данных PostgreSQL. [Формат записи](https://github.com/jacobian/dj-database-url#url-schema).

### Запустите сайт

```shell-session
$ python main.py
```

### Откройте его по ссылке

```shell-session
$ http://127.0.0.1:8000/
```
