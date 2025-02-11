# Проект YaTube API

YaTube API — это RESTful API для социальной сети YaTube, которая позволяет пользователям создавать посты, комментировать их, объединяться в группы и подписываться на других пользователей. API предоставляет удобный интерфейс для взаимодействия с основными функциями социальной сети.

---

## Возможности проекта

### 1. **Посты**
- **Создание постов:** Пользователи могут создавать посты с текстом и привязывать их к группам.
- **Просмотр постов:** Все пользователи могут просматривать посты, фильтруя их по тексту или группе.
- **Редактирование и удаление:** Авторы постов могут редактировать или удалять свои посты.

### 2. **Комментарии**
- **Добавление комментариев:** Пользователи могут оставлять комментарии к постам.
- **Просмотр комментариев:** Все пользователи могут просматривать комментарии к посту.
- **Редактирование и удаление:** Авторы комментариев могут редактировать или удалять свои комментарии.

### 3. **Группы**
- **Создание групп:** Пользователи могут создавать группы для объединения постов по темам.
- **Просмотр групп:** Все пользователи могут просматривать список групп и их детали.
- **Редактирование и удаление:** Авторы групп могут редактировать или удалять свои группы.

### 4. **Подписки**
- **Подписка на пользователей:** Пользователи могут подписываться на других пользователей.
- **Просмотр подписок:** Пользователи могут просматривать свои подписки и фильтровать их по имени пользователя.
- **Отмена подписки:** Пользователи могут отменять свои подписки.

---

## Как работает API

API предоставляет следующие эндпоинты для взаимодействия с социальной сетью YaTube:

### **Посты**
- `GET /api/posts/` — получить список всех постов.
- `POST /api/posts/` — создать новый пост.
- `GET /api/posts/{id}/` — получить детали поста по ID.
- `PUT /api/posts/{id}/` — обновить пост.
- `PATCH /api/posts/{id}/` — частично обновить пост.
- `DELETE /api/posts/{id}/` — удалить пост.

### **Комментарии**
- `GET /api/posts/{post_id}/comments/` — получить список комментариев к посту.
- `POST /api/posts/{post_id}/comments/` — создать новый комментарий.
- `GET /api/posts/{post_id}/comments/{id}/` — получить детали комментария.
- `PUT /api/posts/{post_id}/comments/{id}/` — обновить комментарий.
- `PATCH /api/posts/{post_id}/comments/{id}/` — частично обновить комментарий.
- `DELETE /api/posts/{post_id}/comments/{id}/` — удалить комментарий.

### **Группы**
- `GET /api/groups/` — получить список всех групп.
- `POST /api/groups/` — создать новую группу.
- `GET /api/groups/{id}/` — получить детали группы.
- `PUT /api/groups/{id}/` — обновить группу.
- `PATCH /api/groups/{id}/` — частично обновить группу.
- `DELETE /api/groups/{id}/` — удалить группу.

### **Подписки**
- `GET /api/follow/` — получить список подписок.
- `POST /api/follow/` — создать новую подписку.
- `DELETE /api/follow/{id}/` — удалить подписку.

---

## Как использовать API

1. **Регистрация и аутентификация:**  
   Для использования API необходимо зарегистрироваться и аутентифицироваться. API использует токен-аутентификацию. После регистрации получите токен и передавайте его в заголовке запроса:
   ```
   Authorization: Token <ваш_токен>
   ```

2. **Пример запроса:**
   - Создание поста:
     ```http
     POST /api/posts/
     Content-Type: application/json
     Authorization: Token <ваш_токен>

     {
       "text": "Привет, это мой первый пост!",
       "group": 1
     }
     ```

   - Получение списка постов:
     ```http
     GET /api/posts/
     Authorization: Token <ваш_токен>
     ```

---

## Как социальная сеть YaTube может работать с API

1. **Интеграция с фронтендом:**  
   Фронтенд-приложение (например, на React или Vue.js) может использовать API для отображения постов, комментариев, групп и подписок. Все данные будут загружаться через API.

2. **Мобильное приложение:**  
   Мобильное приложение может использовать API для предоставления пользователям доступа к функциям социальной сети.

3. **Автоматизация:**  
   Администраторы могут использовать API для автоматизации задач, таких как создание постов или управление группами.

4. **Аналитика:**  
   С помощью API можно собирать данные о постах, комментариях и подписках для дальнейшего анализа.

---

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-логин/api_yatube_final.git
   cd api_yatube_final
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Примените миграции:
   ```bash
   python manage.py migrate
   ```

4. Запустите сервер:
   ```bash
   python manage.py runserver
   ```

5. API будет доступно по адресу:
   ```
   http://127.0.0.1:8000/api/v1/
   ```

6. Redoc будет доступен по адресу:
   ```
   http://127.0.0.1:8000/redoc/
   ```

---

## Лицензия

Проект распространяется под лицензией BSD 3-Clause License. Подробнее см. в файле [LICENSE](LICENSE).

---

Этот проект предоставляет мощный инструмент для создания социальной сети с возможностью расширения и интеграции с другими сервисами.
