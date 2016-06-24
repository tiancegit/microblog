Web表单是在任何一个Web应用程序中最基本的一部分。将使用表单允许用户写文章，以及登录到应用程序中。  
为了能够处理表单，将使用 Flask_WTF模块。该扩展封装了WTForms，并且恰当的集成到了Flask中。  
Flask 扩展需要大量的配置，所以在根目录创建了一个配置文件（config.py）。以至于容易编辑，重点的设置也可以集成在其中，以免被上传到github导致信息泄露。  
(文件 config.py):
```python
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
```
Flask_WTF扩展需要两个配置。
CSRF_ENABLED配置是为了激活‘跨站点请求伪造’保护，激活该配置可以是的应用程序更安全些。
SECRET_KEY配置，仅仅当CSRF激活的时候才需要，它是用来建立一个加密的令牌，用于验证表单，编写程序是，请务必设置难以猜测到的密钥。  
既然有了配置文件。需要告诉 Flask去读取和使用这个配置，可以在Flask应用被创建后去做，方式如下：  
（文件app/__init__.py）
```
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views

```


在 Flask-WTF 中，表单是表示成对象，Form 类的子类。一个表单子类简单地把表单的域定义成类的变量。  
我们将要创建一个登录表单，用户用于认证系统。在我们应用程序中支持的登录机制不是标准的用户名/密码类型，我们将使用 OpenID。  
OpenIDs 的好处就是认证是由 OpenID 的提供者完成的，因此我们不需要验证密码，这会让我们的网站对用户而言更加安全。OpenID 登录仅仅需要一个字符串，被称为 OpenID。  
我们将在表单上提供一个 ‘remember me’ 的选择框，以至于用户可以选择在他们的网页浏览器上种植 cookie ，当他们再次访问的时候，浏览器能够记住他们的登录。
所以让我们编写第一个表单
(文件 app/forms.py):
```python
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
```
