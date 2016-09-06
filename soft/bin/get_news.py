import feedparser
from get_most_read_and_cited_papers_lib import *

nature_news_feed_url = "http://feeds.nature.com/NatureNewsComment"
feed = feedparser.parse( nature_news_feed_url )

nature_items = feed [ "items" ]

print len(nature_items)
insert_news_to_db(nature_items, "dbs/nature_news", author="Nature News")

astrobites_feed_url = "https://astrobites.org/feed/"
feed = feedparser.parse( astrobites_feed_url )

astrobites_items = feed [ "items" ]

insert_news_to_db(astrobites_items, "dbs/astrobites", author="Astrobites")

phys_org_featured_url = "http://phys.org/rss-feed/editorials/"
feed = feedparser.parse( phys_org_featured_url )

phys_org_items = feed ["items"]
if len(phys_org_items)>25:
    phys_org_items[0:25]

insert_news_to_db(phys_org_items, "dbs/phys_org_news", author="phys.org")
