#### Здесь предаставлено несколько простых автотестов для сайта https://telega.in/
###### Все тесты реализованы с использованием шаблона <i>PageObject</i>
###### Разработаны на <i>Python</i>
###### Запускаются из <i>Jenkins</i>
###### Для запуска браузера используется <i>Selenoid</i>
###### В результате генерируется отчет при помощи <i>Allure</i> и отправляется нотифкация в <i>Telegram</i>

<h2>Description</h2>
<li><a href="#tools">Инструменты</a></li>
<li><a href="#tests">Тесты</a></li>
<li><a href="#run-tests">Запуск тестов</a></li>
<li><a href="#test-example">Примеры</a></li>

---

<h2 id="tools">Инструменты</h2>
<div align="center">
    <img title="Python" width="40" src="resources/images/python-original.svg">
    <img title="Pytest" width="40" src="resources/images/pytest-original-wordmark.svg">    
    <img title="PyCharm" width="40" src="resources/images/pycharm-original.svg">
    <img title="Selenium" width="40" src="resources/images/selenium.png">
    <img title="Selene" width="40" src="resources/images/selene.png">
    <img title="Jenkins" width="40" height="40" src="resources/images/jenkins-original.svg">
    <img title="Selenoid" width="40" src="resources/images/selenoid.png">
    <img title="Allure" width="40" src="resources/images/allure.png">
    <img title="Github" width="40" src="resources/images/github-original-wordmark.svg">
    <img title="Telegram" width="40" src="resources/images/telegram.png">
</div>

---

<h2 id="tests">Тесты</h2>
<ul>
<li>Попытка регистрации с неправильным email</li>
<li>Попытка входа без логина и пароля</li>
<li>Поиск по базе знаний</li>
<li>Фильтрация в разделе Аналитика</li>
<li>Попытка добавления канала без ссылки</li>
</ul>

---

<h2 id="run-tests">Запуск тестов</h2>

<pre>
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest ${TESTS_FOLDER}
</pre>

---

<h2 id="run-tests">Примеры запуска</h2>

#### История запусков тестового набора
<img src="resources/images/history_of_runs.jpg" height="300">

#### Пример выполнения одного теста
<img src="resources/images/example_of_run.jpg" height="300">

#### Сообщение в телеграмм 
<img src="resources/images/tg_notifications.jpg" height="300">

---