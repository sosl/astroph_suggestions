#!/usr/bin/python
'''
Written by Stefan Oslowski (stefanoslowski@swin.edu.au)
'''

import ads
import datetime
from get_most_read_and_cited_papers_lib import insert_list_to_db

time_span = 3 # in months
date_str = datetime.date.today() - datetime.timedelta(3*365/12 + 1)

most_read_papers_astro = ads.SearchQuery(q='* +database:astronomy +pubdate:[%s TO *]' % date_str, sort = 'read_count desc', rows=25)
most_cited_papers_astro = ads.SearchQuery(q='* +database:astronomy +pubdate:[%s TO *]' % date_str, sort = 'citation_count desc', rows=25)
most_read_papers = ads.SearchQuery(q='* +pubdate:[%s TO *]' % date_str, sort = 'read_count desc', rows=25)
most_cited_papers = ads.SearchQuery(q='* +pubdate:[%s TO *]' % date_str, sort = 'citation_count desc', rows=25)

info_read_astro = []
info_cited_astro = []
info_read = []
info_cited = []

for paper in most_read_papers_astro:
    info_read_astro.append([paper.title, paper.bibcode, paper.read_count,
        paper.citation_count])

for paper in most_cited_papers_astro:
    info_cited_astro.append([paper.title, paper.bibcode, paper.read_count, paper.citation_count])

for paper in most_read_papers:
    info_read.append([paper.title, paper.bibcode, paper.read_count, paper.citation_count])

for paper in most_cited_papers:
    info_cited.append([paper.title, paper.bibcode, paper.read_count, paper.citation_count])

all_lists = {"dbs/astro_read": info_read_astro, "dbs/astro_cited":info_cited_astro,
"dbs/all_read": info_read, "dbs/all_cited":info_cited}

for name, list in all_lists.iteritems():
    insert_list_to_db(list, name)
