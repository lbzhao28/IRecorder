__author__ = 'zhuangkun'
import web

urls = (
    '/Login/(.*)', 'Login.LoginInfo',
    '/RecSearch/(.*)', 'RecSearch.RecSelect',
    '/RecSearch', 'RecSearch.SearchRec',

    '/rqscoscr/(.*)','RecorderScore_Stone.rqscoscr',
    '/Saverqscoscr/(.*)','RacorderClient.RacorderSave',

    )
app = web.application(urls, locals())

if __name__ == "__main__":
    app.run()

