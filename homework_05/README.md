### Домашнее задание "Веб-приложение на Flask"
#### Задача:
+ скопируйте папку `homework_05` для этой домашки (Памятка: https://github.com/OtusTeam/BasePython/tree/homeworks-new)
+ используйте следующие пакеты:
  +Flask
+ в модуле `app` создайте базовое приложение на Flask
+ создайте index view `/`
+ добавьте страницу `/about/`, добавьте туда текст
+ создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
+ в базовый шаблон подключите статику Bootstrap 5 (подключите стили), примените стили Bootstrap
+ в базовый шаблон добавьте навигационную панель `nav` (https://getbootstrap.com/docs/5.0/components/navbar/)
- в навигационную панель добавьте ссылки на главную страницу `/` и на страницу `/about/` при помощи `url_for`
- добавьте новые зависимости в файл `requirements.txt` в корне проекта 
  (лучше вручную, но можно командой `pip freeze > requirements.txt`, тогда обязательно проверьте, что туда попало, и удалите лишнее)
#### Критерии оценки:
- создано Flask приложение в `app.py`
- добавлены вьюшки `/` и `/about/`
- подключены и применены стили Bootstrap
- в базовый шаблон добавлена навигационная панель
- автоматический тест `test_homework_05` проходит
