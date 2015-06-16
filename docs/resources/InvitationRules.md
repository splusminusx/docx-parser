# InvitationRules
## Описание ресурса
InvitationRules
# Методы
## add
### Описание метода
InvitationRules.add
Добавляет новый сценарий вовлечения.
Параметры
Результат
Объект типа «InvitationRule».
Пример вызова
curl "https://api.livetex.ru/v2/invitationrules" \
-H "Authorization: Bearer ACCESS_TOKEN" \
	-d "title=Первое посещение из России" \
	-d "action=chat" \
	-d "welcome=Могу ли я вам чем-то помочь?" \
	-d "is_active=true" \
	-d "is_new_visitor=true" \
	-d "locations[0][country][id]=123" \
	-d "locations[0][city][id]=3245" \
	-d "site_bindings[0][site_id]=6789" \
	-d "site_bindings[0][department_id]=65432"
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|site_bindings|False|Array.<InvitationRuleSiteBinding>|Массив связей сценария вовлечения с сайтами.<br/>Состав полей объектов в массиве точно такой же, как и состав параметров метода  InvitationRuleSiteBinding.add, за исключением поля invitation_rule_id. В данном контексте оно игнорируется.<br/>|
|page_title|False|string|Показывать приглашение на странице с указанной подстрокой в названии (тег «title»).<br/>Если page_type=specified, то одно из двух полей page_url или page_title должно быть указано.<br/>|
|is_new_visitor|True|boolean|Показывать приглашение только новым посетителям.<br/>True – показывать только новым, false – показывать всем.<br/>|
|site_time|False|numeric|Время в секундах, проведенное на сайте посетителем, после которого ему необходимо показывать приглашение.<br/>|
|title|True|string|Название сценария.<br/>|
|is_once_per_day|False|boolean|Показывать приглашение только один раз в сутки.<br/>True – один раз, вне зависимости от значения max_count, false – в соответствии со значением max_count.<br/>|
|welcome_chat|False|string|Текст приглашения, если есть доступные операторы.<br/>Максимум 300 символов.<br/>Обязательно для action = chat или vary.<br/>|
|confirmation_mobile|False|string|Подтверждающее сообщение для мобильных устройств.<br/>Обязательно для action имеет значение vary или lead.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|page_count|False|numeric|Количество просмотренных страниц посетителем, при котором ему необходимо показывать приглашение.<br/>|
|is_active|True|boolean|Признак активности сценария.<br/>|
|welcome_lead|False|string|Текст приглашения, если нет доступных операторов.<br/>Максимум 300 символов.<br/>Обязательно для action = lead или vary.<br/>|
|locations|False|Array.<Location>|Массив географических расположений.<br/>|
|page_type|True|string|Тип страницы.<br/>Возможные значения:<br/>specified – показывать приглашение на странице, соответствующей критериям page_url и page_title.<br/>home – показывать приглашение на главной страницы;<br/>internal – показывать приглашение на внутренней странице;<br/>any – показывать приглашение на любой странице.<br/>|
|page_time|False|numeric|Время, проведенное на странице посетителем, после которого ему необходимо показывать приглашение.<br/>|
|welcome_mobile|True|string|Текст приглашения для мобильных устройств.<br/>Максимум 130 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|action|True|string|Действие, которое следует выполнить, если ситуация подпадает под настройки сценария.<br/>Возможные значения:<br/>vary – показать приглашение в чат, если есть доступные операторы или форму генератора лидов, если доступных операторов нет.<br/>chat – показать приглашение в чат, если есть активные операторы. В противном случае ничего не показывать;<br/>lead – показать форму генератора лида, если нет активных операторов. В противном случае ничего не показывать.<br/>|
|confirmation_lead|False|string|Подтверждающее сообщение, которое показывается посетителю после отправки формы лида.<br/>Максимум 180 символов.<br/>Обязательно для action = lead или vary.<br/>|
|max_count|False|numeric|Максимальное количество показов конкретному посетителю приглашений по данному сценарию в течение календарных суток.<br/>Счетчик показов обнуляется по истечению суток с момента последнего показа.<br/>Отсутствие значения или 0 – ограничения нет.<br/>|
|page_url|False|string|Показывать приглашение на странице с указанным адресом.<br/>Адрес указывается без приставки «http://» или «https://», например:<br/>www.mycompany.ru/about/contacts<br/>Если page_type=specified, то одно из двух полей page_url или page_title должно быть указано.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## show
### Описание метода
InvitationRules.show
Возвращает данные указанного сценария вовлечения.
Параметры
Результат
Объект типа «InvitationRule».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|id|True|numeric|ID сценария вовлечения.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## list
### Описание метода
InvitationRules.list
Возвращает список сценариев вовлечения.
Параметры
Результат
Массив объектов типа «InvitationRule».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|string|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID сценариев вовлечения.<br/>site_ids – idlist, список ID сайтов.<br/>text – поиск по текстам полей welcome, welcome_mobile, confirmation, confirmation_mobile;<br/>action – enum, список возможных значение поля action;<br/>title;<br/>is_active.<br/>|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|limit|False|numeric|По умолчанию – 50.<br/>|
|sort|False|string|Сортировка результатов.<br/>Возможные значение:<br/>title:a – по умолчанию;<br/>created_at:d.<br/>|
|offset|False|numeric|По умолчанию – 0.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## update
### Описание метода
InvitationRules.update
Изменяет указанный сценарий вовлечения.
Параметры
Результат
Метод ничего не возвращает.
Пример вызова
curl "https://api.livetex.ru/v2/invitationrules/12345" \
	-H "Authorization: Bearer ACCESS_TOKEN" \
	–X PATCH \
	-d "title=Первое посещение из России" \
	-d "locations[0][country][id]=123" \
	-d "locations[0][city][id]=3245" \
	-d "site_bindings[0][site_id]=6789" \
	-d "site_bindings[0][department_id]=65432"
	-d "site_bindings[1][site_id]=6785"

Уровень доступа для ролей


### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|site_bindings|False|Array.<InvitationRuleSiteBinding>|Массив связей сценария вовлечения с сайтами.<br/>Состав полей объектов в массиве точно такой же, как и состав параметров метода  InvitationRuleSiteBinding.add, за исключением поля invitation_rule_id. В данном контексте оно игнорируется.<br/>ВНИМАНИЕ!<br/>Значение этого параметра полностью замещает текущие связи сценария с сайтами, как если бы старые связи были удалены и созданы новые.<br/>Указание пустого массива приведет к удалению всех связей сценария с сайтами.<br/>|
|page_title|False|string|Показывать приглашение на странице с указанной подстрокой в названии (тег «title»).<br/>Если page_type=specified, то одно из двух полей page_url или page_title должно быть указано.<br/>|
|is_new_visitor|False|boolean|Показывать приглашение только новым посетителям.<br/>True – показывать только новым, false – показывать всем.<br/>|
|site_time|False|numeric|Время в секундах, проведенное на сайте посетителем, после которого ему необходимо показывать приглашение.<br/>|
|title|False|string|Название сценария.<br/>|
|is_once_per_day|False|boolean|Показывать приглашение только один раз в сутки.<br/>True – один раз, вне зависимости от значения max_count, false – в соответствии со значением max_count.<br/>|
|welcome_chat|False|string|Текст приглашения, если есть доступные операторы.<br/>Максимум 300 символов.<br/>Обязательно для action = chat или vary.<br/>|
|confirmation_mobile|False|string|Подтверждающее сообщение для мобильных устройств.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|page_count|False|numeric|Количество просмотренных страниц посетителем, при котором ему необходимо показывать приглашение.<br/>|
|is_active|False|boolean|Признак активности сценария.<br/>|
|welcome_lead|False|string|Текст приглашения, если нет доступных операторов.<br/>Максимум 300 символов.<br/>Обязательно для action = lead или vary.<br/>|
|locations|False|Array.<Location>|Массив географических расположений.<br/>|
|page_type|False|string|Тип страницы.<br/>Возможные значения:<br/>specified – показывать приглашение на странице, соответствующей критериям page_url и page_title.<br/>home – показывать приглашение на главной страницы;<br/>internal – показывать приглашение на внутренней странице;<br/>any – показывать приглашение на любой странице.<br/>|
|page_time|False|numeric|Время, проведенное на странице посетителем, после которого ему необходимо показывать приглашение.<br/>|
|welcome_mobile|False|string|Текст приглашения для мобильных устройств.<br/>Максимум 130 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|action|False|string|Действие, которое следует выполнить, если ситуация подпадает под настройки сценария.<br/>Возможные значения:<br/>vary – показать приглашение в чат, если есть доступные операторы или форму генератора лидов, если доступных операторов нет.<br/>chat – показать приглашение в чат, если есть активные операторы. В противном случае ничего не показывать;<br/>lead – показать форму генератора лида, если нет активных операторов. В противном случае ничего не показывать.<br/>|
|confirmation_lead|False|string|Подтверждающее сообщение, которое показывается посетителю после отправки формы лида.<br/>Максимум 180 символов.<br/>Обязательно для action = lead или vary.<br/>|
|max_count|False|numeric|Максимальное количество показов конкретному посетителю приглашений по данному сценарию в течение календарных суток.<br/>Счетчик показов обнуляется по истечению суток с момента последнего показа.<br/>Отсутствие значения или 0 – ограничения нет.<br/>|
|id|True|numeric|ID сценария вовлечения.<br/>|
|page_url|False|string|Показывать приглашение на странице с указанным адресом.<br/>Адрес указывается без приставки «http://» или «https://», например:<br/>www.mycompany.ru/about/contacts<br/>Если page_type=specified, то одно из двух полей page_url или page_title должно быть указано.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## delete
### Описание метода
InvitationRules.delete
Удаляет указанный сценария вовлечения.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID сценария вовлечения.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner