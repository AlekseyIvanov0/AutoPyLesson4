### AutoPyLesson4
тестовое задание по курсе Автоматизация на Python
### Установка
Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:AlekseyIvanov0/AutoPyLesson4.git
```

```
cd AutoPyLesson4
```

Создать и активировать виртуальное окружение:

```
python3 -m venv venv
```


* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

```


```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запуск автотестов на ревью:

```
pytest -v --tb=line --language=en -m need_review
```