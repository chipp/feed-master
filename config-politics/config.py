# coding=utf-8

feeds = [
    ("Персонально ваш", "http://echo.msk.ru/programs/personalnovash/rss-audio.xml"),
    ("Ганапольское", "http://www.echo.msk.ru/programs/ganapolskoe_itogi/rss-audio.xml"),
    ("Кейс", "http://www.echo.msk.ru/programs/keys/rss-audio.xml"),
    ("Альбац", "http://echo.msk.ru/programs/albac/rss-audio.xml"),
    ("Код доступа", "http://www.echo.msk.ru/programs/code/rss-audio.xml"),
    ("Особое мнение", "http://echo.msk.ru/programs/personalno/rss-audio.xml"),
    ("2017", "http://www.echo.msk.ru/programs/year2017/rss-audio.xml"),
    ("Интервью", "http://www.echo.msk.ru/programs/beseda/rss-audio.xml"),
    ("Невзоровские среды", "http://echo.msk.ru/programs/nevsredy/rss-audio.xml")
]

settings = {
    "info": {
        "title": u"Эхо Москвы",
        "description": u"Правильный, комбинированный фид избранных передач (версия 2)",
        "link": "http://echo.msk.ru"
    },
    "language": "ru-ru",
    "max_items_per_feed": 10,  # how many episoded to keep per feed
    "max_items_total": 200,    # total number of episodes in common feed
    "table": "feed-master-politics"
}
