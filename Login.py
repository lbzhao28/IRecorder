__author__ = 'zhuangkun'
#encoding:utf-8
import urls
import web
import urls
import json
import ReccemClient;
from web.contrib.template import render_mako
import  RacorderClient
render = render_mako(
    directories=['templates'],
    input_encoding='utf-8',
    output_encoding='utf-8',
)

#根据权限来控制登录
def create_render(is_superuser):
    render = None
    if logged():
        if is_superuser == 1:
            render = render_mako(
                directories=['templates'],
                input_encoding='utf-8',
                output_encoding='utf-8',
            )
        else:
            render = render_mako(
                directories=['templates'],
                input_encoding='utf-8',
                output_encoding='utf-8',
            )
    else:
        render = render_mako(
            directories=['templates'],
            input_encoding='utf-8',
            output_encoding='utf-8',
        )
    return render


class Login:
    def GET(self):
        return render.login(msg=u'');
    def POST(self):
        name, passwd = web.input().username, web.input().password
        ret = RacorderClient.Login(name,passwd);
        if ret:
            web.ctx.session.user_UserName = name;
            web.seeother('/RecSearch/')
        else:
            return render.login(msg=u'用户名或密码错误！请重新输入！')

class Reset:
    def GET(self):
        urls.session.login = 0
        urls.session.kill()
        render = create_render(urls.session.is_superuser)
        return  render.login(msg=u'请重新登录！')


