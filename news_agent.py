import feedparser
# Fonti italiane di news tech
def get_tech_news():
    feeds = [
        "https://www.hdblog.it/rss/",
        "https://www.smartworld.it/feed",
        "https://rss.hwupgrade.it/news.xml",
        "https://www.tomshw.it/feed/",
        "https://www.everyeye.it/feed/notizie/",
        "https://www.wired.it/feed/tech/"
    ]

    news_list = []
# Aggiunge alla lista le 10 notizie ricavate da ogni fonte
    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:10]:
            news_list.append(f"• {entry.title}\n{entry.link}")

    return "\n\n".join(news_list)

if __name__ == "__main__":
    print(get_tech_news())
