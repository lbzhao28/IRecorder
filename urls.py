__author__ = 'zhuangkun'
import web

urls = (
    '/', 'login.Login',
    '/login', 'login.Login',
    '/RecSearch/(.*)', 'RecSearch.RecSelect',
    '/RecSearch', 'RecSearch.SearchRec',

    '/ReccemSearch', 'ReccemClient.GetRaccemSearchUrl',
    '/ReccemSearch/(.*)', 'ReccemSearch.ReccemSelect',
    '/ReccemSearch', 'ReccemSearch.SearchReccem'
    )
app = web.application(urls, locals())

if __name__ == "__main__":
    app.run()

