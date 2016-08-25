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

```python
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views

```

---

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

我相信这个类不言而明。我们导入 Form 类，接着导入两个我们需要的字段类，TextField 和 BooleanField。  
DataRequired 验证器只是简单地检查相应域提交的数据是否是空。  
在 Flask-WTF 中有许多的验证器，我们将会在以后看到它们。

---

我们同样需要一个包含生成表单的 HTML 的模板。好消息是我们刚刚创建的 LoginForm 类知道如何呈现为 HTML 表单字段，  
所以我们只需要集中精力在布局上。这里就是我们登录的模板
(文件 app/templates/login.html):
```html
<!-- extend from base layout -->
{% extends "base.html" %}

{% block content %}
<h1>Sign In</h1>
<form action="" method="post" name="login">
    {{form.hidden_tag()}}
    <p>
        Please enter your OpenID:<br>
        {{form.openid(size=80)}}<br>
    </p>
    <p>{{form.remember_me}} Remember Me</p>
    <p><input type="submit" value="Sign In"></p>
</form>
{% endblock %}

```


通过了extends模板声明语句，我们重用了base模板。  
在所有模板中做到这一点，将确保所以网页的布局的一致性，
这个模板和常规的html模板有一些有意思的不同之处，模板希望实例化刚创建的表单类的  
表单对象，来储存成一个模板参数，称为form。当我们编写渲染这个模板的视图函数的时候，  
将会特别注意传送模板参数到模板中。  

####重要且必备
form.hidden_tag() 模板参数将会被替换成一个隐藏字段，是用来实现在配置中激活的   
CSRF保护。如果你已经激活了CSRF，这个字段需要出现在你的所有表单中。

我们表单中实际的字段也将会被表单对象渲染，你只必须在字段应该被插入的地方指明一个   
{{form.field_name}} 模板参数。某些字段是可以带参数的。  
在我们的例子中，我们要求表单生成一个 80 个字符宽度的 openid 字段。

因为我们并没有在表单中定义提交按钮，我们必须按照普通的字段来定义。  
提交字段实际并不携带数据因此没有必要在表单类中定义。


###表单视图


编写渲染模板的视图函数的代码。  
只需要吧一个表单对象传入到模板中。这就是我们新的视图函数：
文件(app/views.py):
```pythons
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# index view function suppressed for brevity

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
        title = 'Sign In',
        form = form)
```















