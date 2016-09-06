# -* - coding: UTF-8 -* -
# 许多 Flask 扩展需要大量的配置，因此我们将要在 microblog 文件夹的根目录下创建一个配置文件以至于容易被编辑。(文件 config.py):

CSRF_ENABLED = True
SECRET_KEY = 'TIANCE'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
