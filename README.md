## Проект по django "Сайт для сотрудников"
### Руководство пользователя.
Проект представляет собой сайт из 3-х страниц с функцией добавление сотрудников. 
На главной странице отображается список сотрудников

<img width="1451" height="370" alt="image" src="https://github.com/user-attachments/assets/701c70eb-6e8c-4791-9537-edd48535464f" />


На странице "Распорядок" содержится информация о том, для чего нужны правила внутреннего трудового распорядка

<img width="1447" height="600" alt="image" src="https://github.com/user-attachments/assets/d3d75657-155d-480b-a292-46e37255164d" />


Для добавления нового сотрудника нужно нажать на кнопку "Добавить" и заполнить форму.

<img width="868" height="565" alt="image" src="https://github.com/user-attachments/assets/c37375c8-bbda-44bb-ae4a-259db91db03e" />


После заполнения и отправки формы сотрудник появится на главной странице.

<img width="1515" height="359" alt="image" src="https://github.com/user-attachments/assets/6ea06a5b-129f-4df5-87bb-18b3862fafb7" />


### Руководство программиста
> Django — это высокоуровневый, бесплатный фреймворк для веб-разработки на языке Python, который позволяет создавать безопасные и масштабируемые веб-сайты быстрее и проще, предоставляя готовые компоненты для типовых задач.
Начало работы со средой:
```
#  Создание вирт.среды
python -m venv .venv
# Активация вирт.среды
.venv\Scripts\activate
# Установка библиотеки
pip install django==5
# Создаю проект
djanho-admin startproject testdrive
# Перехожу
cd testdrive
# Создаю приложение
python manage.py startapp myapp
# Перейдите в файл settings.py и в разделе INSTALLED_APPS впишите(в конец) название приложения "myapp"
# Запускаю проект
python manage.py runserver 
```
