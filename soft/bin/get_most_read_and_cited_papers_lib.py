'''
Written by Stefan Oslowski (stefanoslowski@swin.edu.au)
'''

import sqlite3

def print_list(papers):
    i = 0
    for p in papers:
        print i, p[0], p[1], p[2], p[3]
        i += 1

def create_db(name):
    """
    Create a database to store a list of papers

    Keyword arguments:
    name -- string, name of the db
    """
    conn = sqlite3.connect(name + '.sqlite')
    cur = conn.cursor()
    cur.executescript('''
    DROP TABLE IF EXISTS papers;

    CREATE TABLE papers (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT, 
        summary TEXT default "",
        url TEXT,
        read_count INTEGER,
        cite_count INTEGER
    );
    ''')
    return 0

def create_news_db(name):
    """
    Create a database to store a list of papers

    Keyword arguments:
    name -- string, name of the db
    """
    conn = sqlite3.connect(name + '.sqlite')
    cur = conn.cursor()
    cur.executescript('''
    DROP TABLE IF EXISTS papers;

    CREATE TABLE papers (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT, 
        summary TEXT,
        url TEXT,
        author TEXT,
        read_count INTEGER DEFAULT 0,
        cite_count INTEGER DEFAULT 0
    );
    ''')
    return 0

def insert_news_to_db(news, name, author=""):
    create_news_db(name)
    conn = sqlite3.connect(name + '.sqlite')
    cur = conn.cursor()

    author_insert=""
    print "news: ", type(news)
    for article in news:
        #print article["author"]
        try:
            author_insert = article["author"]
        except:
            author_insert = author
        cur.execute('''INSERT INTO papers (title, summary, url, author)
            VALUES ( ?, ?, ?, ?)''', ( article["title"], article["summary"],
                article["link"], author_insert ))
    conn.commit()
    return 0

def insert_list_to_db_old(papers, name):
    """
    Populate a database with papers

    Keyword arguments:
    papers -- list of papers to insert into the db
              the list should contain, in order:
              title, bibcode, read count, cite count
    name -- name of database to insert into
    """
    create_db(name)
    conn = sqlite3.connect(name + '.sqlite')
    cur = conn.cursor()

    for paper in papers:
        cur.execute('''INSERT INTO papers (title, bibcode, read_count, cite_count)
            VALUES ( ?, ?, ?, ?)''', ( paper[0][0], unicode(paper[1]),
            unicode(paper[2]), unicode(paper[3]) ))
    conn.commit()
    return 0


def insert_list_to_db(papers, name):
    """
    Populate a database with papers

    Keyword arguments:
    papers -- list of papers to insert into the db
              the list should contain, in order:
              title, bibcode, read count, cite count
    name -- name of database to insert into
    """
    create_db(name)
    conn = sqlite3.connect(name + '.sqlite')
    cur = conn.cursor()

    for paper in papers:
        url = unicode("http://adsabs.harvard.edu/abs/"+paper[1])
        cur.execute('''INSERT INTO papers (title, url, read_count, cite_count)
            VALUES ( ?, ?, ?, ?)''', ( paper[0][0], url,
            unicode(paper[2]), unicode(paper[3]) ))
    conn.commit()
    return 0


