# Дипломная работа к профессии Python-разработчик «API Сервис заказа товаров для розничных сетей».


## Описание

Приложение предназначено для автоматизации закупок в розничной сети. Пользователи сервиса — покупатель (менеджер торговой сети, который закупает товары для продажи в магазине) и поставщик товаров.

**Клиент (покупатель):**

- Менеджер закупок через API делает ежедневные закупки по каталогу, в котором
  представлены товары от нескольких поставщиков.
- В одном заказе можно указать товары от разных поставщиков — это
  повлияет на стоимость доставки.
- Пользователь может авторизироваться, регистрироваться и восстанавливать пароль через API.
    
**Поставщик:**

- Регистрируется через отдельную точку входа, далее (после утверждения администратором) может авторизоваться и восстанавливать пароль как обычный клиент.
- Через API информирует сервис об обновлении прайса.
- Может включать и отключать прием заказов.
- Может получать список оформленных заказов (с товарами из его прайса).

**Администратор, через панель администратора Django:**

- Активирует впервые зарегистрировавшегося поставщика.
- Может изменить статус заказа, при этом клиент получает информационное письмо.
- Обновляет прайс, полученный от поставщика.

===================================================================


### Запуск приложения

**Установка  зависимостей:**
sudo pip3 install -r requirements.txt


**Создание миграций:**  
python3 manage.py makemigrations  
**Применение миграций:**  
python3 manage.py migrate  
**Запуск сервера:**  
python3 manage.py runserver  
**Создание суперпользователя:**  
python3 manage.py createsuperuser   


**Примеры запросов**
файл - apitesttest.http