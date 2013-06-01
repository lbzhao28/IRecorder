__author__ = 'zhuangkun'
import urls
import web
import urls
import json
import ReccemClient;
from web.contrib.template import render_mako

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
        if logged():
            render = create_render(urls.session.is_superuser)
            return  u"重复登录！"
        else:
            render = create_render(urls.session.is_superuser)
            return  render.login(msg=u'')

    def POST(self):
        name, passwd = web.input().username, web.input().password
        rtvalue = db.select('auth_user', where='username=$name', vars=locals())
        urls.session.loginInfo = {'UserId': '', 'DispalyName': ''}
        #数据库无返回则报错
        if rtvalue == None or rtvalue == []:
            urls.session.login = 0
            urls.session.is_superuser = 0
            render = create_render(urls.session.is_superuser)
            #todo 需要改成读取配置
            return render.login(msg=u'密码错误！请重新输入！')
        else:
            ident = rtvalue[0]
            #密码偏离值最可以通过配置定义
        if hashlib.md5("sAlT754-" + passwd).hexdigest().decode() == ident['Password']:
            urls.session.login = 1
            urls.session.is_superuser = ident['IsSuperuser']
            urls.session.loginInfo['UserId'] = ident['UserId']
            urls.session.loginInfo['DispalyName'] = ident['FirstName'] + ident['LastName'] + ''
            #根据Dean要求追加用户名称。
            urls.session.username = name
            #render = create_render(urls.session.is_superuser)
            raise web.seeother('/home')
        else:
            urls.session.login = 0
            urls.session.is_superuser = 0
            render = create_render(urls.session.is_superuser)
            #todo 需要改成读取配置
            return render.login(msg=u'密码错误！请重新输入！')


class Reset:
    def GET(self):
        urls.session.login = 0
        urls.session.kill()
        render = create_render(urls.session.is_superuser)
        return  render.login(msg=u'请重新登录！')


