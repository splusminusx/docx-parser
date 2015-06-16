## WARNING: Type is DEPRECATED
## LeadFormSettings
### Описание типа
LeadFormSettings - DEPRECATED
ВНИМАНИЕ! Сущность является устаревшей. Все переехало в WidgetSettings, SiteChatSettings с существенными изменениями.
Настройки формы генератора лидов.
Таблица 51. Настройки формы генератора лидов

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_department|True|boolean|Включение/выключение выбора отдела в форме лида.<br/>При создании сайта устанавливается в false.<br/>|
|photo_custom|False|file|Загруженная картинка приветствия для photo_type=custom.<br/>Изображение в формате JPEG, GIF или PNG с размерами 70x70px.<br/>Поле обязательно для photo_type = custom.<br/>|
|confirmation|True|string|Текст подтверждения по умолчанию. Максимум 180 символов.<br/>|
|confirmation_mobile|True|string|Текст подтверждения по умолчанию, который отобразится в мобильном браузере. Максимум 180 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|color|False|string|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>|
|color_type|True|string|Тип указания цветовой схемы.<br/>Возможные значения:<br/>preset – стандартная схема;<br/>custom – явное указание цветов.<br/>|
|welcome|True|string|Текст приветствия по умолчанию. Максимум 180 символов.<br/>|
|color_main|False|color|Основной цвет.<br/>Поле обязательно для color_type = custom.<br/>|
|banner_custom|False|file|Загруженный баннер для banner_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с шириной от 1 до 448 px и высотой 82 px.<br/>Поле обязательно для banner_type = custom.<br/>|
|updated_at|True|datetime|Дата последнего обновления.<br/>|
|banner_type|True|string|Тип баннера.<br/>Возможные значения:<br/>none – без баннера;<br/>default – стандартный баннер;<br/>custom – загружаемый баннер.<br/>|
|is_custom|True|boolean|Признак заказного дизайна формы генератора лидов.<br/>Если true, то изменение некоторых настроек может не иметь должного результата, поскольку соответствующий аспект внешнего вида переопределяются заказным дизайном.<br/>Это признак доступен только для чтения.<br/>|
|color_background|False|color|Цвет фона.<br/>Поле обязательно для color_type = custom.<br/>|
|banner_link|False|string|Ссылка, по которой будет направлен посетитель по клику на баннере.<br/>Поле обязательно для banner_type = custom.<br/>|
|welcome_mobile|True|string|Текст приветствия по умолчанию, который отобразиться в мобильном браузере. Максимум 180 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|lead_type|True|string|Запрашиваемые контактные данные.<br/>email -  запрашивается только email;<br/>phone – запрашивается только телефон;<br/>email_or_phone – запрашивается телефон или email;<br/>email_and_phone – запрашивается телефон и email.<br/>|
|photo_type|True|string|Тип картинки приветствия.<br/>Возможные значения:<br/>none – без картинки;<br/>default – стандартное фото;<br/>custom – загруженное фото.<br/>|
|label|True|string|Надпись на ярлыке.<br/>Возможные значения:<br/>question – «Задать вопрос»;<br/>action – «Внимание! Акция»;<br/>gift – «Внимание! Подарок»;<br/>help – «Обратитесь за помощью»;<br/>best – «Посоветуем лучшее»;<br/>waiting – «Ждем Ваших вопросов»;<br/>choice – «Поможем с выбором»;<br/>consulting – «Получить консультацию».<br/>|
|required_fields|False|string|Обязательность полей при lead_type=email_and_phone.<br/>Возможные значения:<br/>email – e-mail;<br/>phone – телефон;<br/>email_and_phone – email и телефон.<br/>Поле обязательно при lead_type=email_and_phone.<br/>|
|color_text|False|color|Цвет текста.<br/>Поле обязательно для color_type = custom.<br/>|