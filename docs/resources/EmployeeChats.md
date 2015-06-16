# EmployeeChats
## Описание ресурса
EmployeeChats
# Методы
## list
### Описание метода
EmployeeChats.list
Возвращает список межоператорских чатов.
Межоператорским чатом считается набор сообщений между двумя операторами в пределах указанного периода времени.
Параметры
Результат
Массив объектов со следующими полями:

Пример
curl https://api.livetex.ru/v2/employeechats \
-H "Authorization: Bearer ACCESS_TOKEN"

{
    "total": 1,
    "results": [
        {
            "last_message_at": "2012-12-07T09:14:57+04:00",
            "last_message_text": "Спасибо за консультацию. Пока!",
            "employees":[
                {
                    "id": "123456",
                    "first_name": "Иван",
                    "last_name": "Давыдов"
                },
                {
                    "id": "123457",
                    "first_name": "Елена",
                    "last_name": "Изосимова"
                }
            ],
            message_count: 10
        }
    ]
}

Уровень доступа для ролей


### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|string|Критерий поиска.<br/>Доступные поля:<br/>employee_ids – idlist, список ID сотрудников – участников чата. Чат удовлетворяет условию поиска, если хотя бы один его участник указан в этом списке.<br/>text – ключевое слово в тексте чата.<br/>created_at – datetime, максимум 30 дней.<br/>Если не указано, то фильтр устанавливается в значение, соответствующее последним 30 дням.<br/>|
|fields|False|string|Список через запятую возвращаемых полей сотрудников.<br/>Например: employee(first_name).<br/>|
|limit|False|numeric|По умолчанию – 50.<br/>|
|offset|False|numeric|По умолчанию – 0.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner