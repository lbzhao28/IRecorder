__author__ = 'zhuangkun'
import web

urls = (
    '/Login', 'Login.Login',
    '/ReccemSearch/(.*)', 'ReccemSearch.ReccemSelect',
    '/ReccemSearch', 'ReccemSearch.SearchReccem'
    )
app = web.application(urls, locals())

if __name__ == "__main__":
    app.run()

