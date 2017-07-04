# coding=utf-8

feeds = [
    ("Все так", "http://www.echo.msk.ru/programs/vsetak/rss-audio.xml"),
    ("Все так +", "http://www.echo.msk.ru/programs/vsetakplus/rss-audio.xml"),
    ("Вот так", "http://echo.msk.ru/programs/vottak/rss-audio.xml"),
    ("Дилентанты", "http://echo.msk.ru/programs/Diletanti/rss-audio.xml"),
    ("Разбор полета", "http://www.echo.msk.ru/programs/razbor_poleta/rss-audio.xml"),
    ("48 минут", "http://www.echo.msk.ru/programs/48minut/rss-audio.xml"),
    ("A-Team", "http://www.echo.msk.ru/programs/a_team/rss-audio.xml")
]

settings = {
    "info": {
        "title": u"Эхо Москвы - Потом",
        "description": u"Правильный, комбинированный фид избранных передач (версия 2)",
        "link": "http://echo.msk.ru",
        "image": "http://burdukov.by/echo-later.jpg"
    },
    "language": "ru-ru",
    "max_items_per_feed": 10,  # how many episoded to keep per feed
    "max_items_total": 200,    # total number of episodes in common feed
    "table": "feed-master-history"
}
