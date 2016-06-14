import requests
from pyquery import PyQuery


def get_url(url):
    response = requests.get(url)
    doc = PyQuery(response.text)
    for article in doc('article'):
        h = PyQuery(article)
        print h.find('h1.entry-title').text().encode('utf-8')
        print h.find('div.entry-content p').text().encode('utf-8')


def get_month(monthly_url):
    get_url(monthly_url)
    for page in xrange(5):
        get_url("{}page/{}/".format(monthly_url, page + 2))


URLS = [
    'http://timosoini.fi/2016/06/',
    'http://timosoini.fi/2016/05/',
    'http://timosoini.fi/2016/04/',
    'http://timosoini.fi/2016/03/',
    'http://timosoini.fi/2016/02/',
    'http://timosoini.fi/2016/01/',
    'http://timosoini.fi/2015/12/',
    'http://timosoini.fi/2015/11/',
    'http://timosoini.fi/2015/10/',
    'http://timosoini.fi/2015/09/',
    'http://timosoini.fi/2015/08/',
    'http://timosoini.fi/2015/07/',
    'http://timosoini.fi/2015/06/',
    'http://timosoini.fi/2015/05/',
    'http://timosoini.fi/2015/04/',
    'http://timosoini.fi/2015/03/',
    'http://timosoini.fi/2015/02/',
    'http://timosoini.fi/2015/01/',
    'http://timosoini.fi/2014/12/',
    'http://timosoini.fi/2014/11/',
    'http://timosoini.fi/2014/10/',
    'http://timosoini.fi/2014/09/',
    'http://timosoini.fi/2014/08/',
    'http://timosoini.fi/2014/07/',
    'http://timosoini.fi/2014/06/',
    'http://timosoini.fi/2014/05/',
    'http://timosoini.fi/2014/04/',
    'http://timosoini.fi/2014/03/',
    'http://timosoini.fi/2014/02/',
    'http://timosoini.fi/2014/01/',
    'http://timosoini.fi/2013/12/',
    'http://timosoini.fi/2013/11/',
    'http://timosoini.fi/2013/10/',
    'http://timosoini.fi/2013/09/',
    'http://timosoini.fi/2013/08/',
    'http://timosoini.fi/2013/07/',
    'http://timosoini.fi/2013/06/',
    'http://timosoini.fi/2013/05/',
    'http://timosoini.fi/2013/04/',
    'http://timosoini.fi/2013/03/',
    'http://timosoini.fi/2013/02/',
    'http://timosoini.fi/2013/01/',
    'http://timosoini.fi/2012/12/',
    'http://timosoini.fi/2012/11/',
    'http://timosoini.fi/2012/10/',
    'http://timosoini.fi/2012/09/',
    'http://timosoini.fi/2012/08/',
    'http://timosoini.fi/2012/07/',
    'http://timosoini.fi/2012/06/',
    'http://timosoini.fi/2012/05/',
    'http://timosoini.fi/2012/04/',
    'http://timosoini.fi/2012/03/',
    'http://timosoini.fi/2012/02/',
    'http://timosoini.fi/2012/01/',
    'http://timosoini.fi/2011/12/',
    'http://timosoini.fi/2011/11/',
    'http://timosoini.fi/2011/10/',
    'http://timosoini.fi/2011/09/',
    'http://timosoini.fi/2011/08/',
    'http://timosoini.fi/2011/07/',
    'http://timosoini.fi/2011/06/',
    'http://timosoini.fi/2011/05/',
    'http://timosoini.fi/2011/04/',
    'http://timosoini.fi/2011/03/',
    'http://timosoini.fi/2011/02/',
    'http://timosoini.fi/2011/01/',
    'http://timosoini.fi/2010/12/',
    'http://timosoini.fi/2010/11/',
    'http://timosoini.fi/2010/10/',
    'http://timosoini.fi/2010/09/',
    'http://timosoini.fi/2010/08/',
    'http://timosoini.fi/2010/07/',
    'http://timosoini.fi/2010/06/',
    'http://timosoini.fi/2010/05/',
    'http://timosoini.fi/2010/04/',
    'http://timosoini.fi/2010/03/',
    'http://timosoini.fi/2010/02/',
    'http://timosoini.fi/2010/01/',
    'http://timosoini.fi/2009/12/',
    'http://timosoini.fi/2009/11/',
    'http://timosoini.fi/2009/10/',
    'http://timosoini.fi/2009/09/',
    'http://timosoini.fi/2009/08/',
    'http://timosoini.fi/2009/07/',
    'http://timosoini.fi/2009/06/',
    'http://timosoini.fi/2009/05/',
    'http://timosoini.fi/2009/04/',
    'http://timosoini.fi/2009/03/',
    'http://timosoini.fi/2009/02/',
    'http://timosoini.fi/2009/01/',
    'http://timosoini.fi/2008/12/',
    'http://timosoini.fi/2008/11/',
    'http://timosoini.fi/2008/10/',
    'http://timosoini.fi/2008/09/',
    'http://timosoini.fi/2008/08/',
    'http://timosoini.fi/2008/07/',
    'http://timosoini.fi/2008/06/',
    'http://timosoini.fi/2008/05/',
    'http://timosoini.fi/2008/04/',
    'http://timosoini.fi/2008/03/',
    'http://timosoini.fi/2008/02/',
    'http://timosoini.fi/2008/01/',
    'http://timosoini.fi/2007/12/',
    'http://timosoini.fi/2007/11/',
    'http://timosoini.fi/2007/10/',
    'http://timosoini.fi/2007/09/',
    'http://timosoini.fi/2007/08/',
    'http://timosoini.fi/2007/06/',
    'http://timosoini.fi/2007/05/',
    'http://timosoini.fi/2007/04/',
    'http://timosoini.fi/2007/03/',
    'http://timosoini.fi/2007/02/',
    'http://timosoini.fi/2007/01/',
]
[get_month(url) for url in URLS]
