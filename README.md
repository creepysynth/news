# news

**1. Router**

1. Получаем URI и ищем первое совпадение с описанными в файле routes.conf маршрутами;
2. Возвращаем маршрут (Route), соответствующий URI;
3. Если маршрут не найден — бросить NotFoundError

Пример файла routes.conf:

    /
    /news/
    /news/[category]/
    /news/[category]/[article]/
   
Интерфейс роутера:

    class Route(object):
        def __init__(self, route_str)
        def matches_uri(self, uri)    // return bool
        @property
        def template(self)

    class Router(object):
        def __init__(self, route_strings)
        def route_for_uri(self, uri)

**2. TemplateEngine**

1. Взять готовый шаблонизатор;
2. Сверстать пару простейших HTML-шаблонов (news.tpl, news-[category].tpl, news-[category]-[article].tpl);
3. Захардкодить в шаблонах массивы данных для отображения;
4. Покурить мануалы и научиться рендерить шаблоны.

**3. FrontController**

1. Получить URI, запрошенный клиентом (DOCUMENT_URI);
2. По DOCUMENT_URI определить маршрут с помощью роутера;
3. Получить имя шаблона по полученному маршруту;
4. Отрендерить шаблон и вернуть пользователю готовый документ;
5. Обрабатываем только GET;
6. Возвращаем правильные HTTP Response codes.
