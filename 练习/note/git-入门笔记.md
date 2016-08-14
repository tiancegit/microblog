##安装git
Linux 安装 git：  
* sudo apt-get install git

windows 安装 git：  
* “https://git-for-windows.github.io/”，下载git-for-windows

安装完成之后，还要进行相对应的配置：  
* $ git config --global user.name "Your Name"
* $ git config --global user.email "email@example.com"

注意git config命令的--global参数，用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置.
当然也可以对某个仓库指定不同的用户名和Email地址。


##命令：
git init : 把当前的目录初始化为git可以管理的仓库
git config : 进行git仓库相对应设置的设定。





##注意事项
明确一下，所有的版本控制系统，其实只能跟踪文本文件的改动，比如TXT文件，网页，所有的程序代码等等，Git也不例外。
版本控制系统可以告诉你每次的改动，比如在第5行加了一个单词“Linux”，在第8行删了一个单词“Windows”。
而图片、视频这些二进制文件，虽然也能由版本控制系统管理，但没法跟踪文件的变化，只能把二进制文件每次改动串起来，
也就是只知道图片从100KB改成了120KB，但到底改了啥，版本控制系统不知道，也没法知道。

不幸的是，Microsoft的Word格式是二进制格式，因此，版本控制系统是没法跟踪Word文件的改动的，前面我们举的例子只是为了演示，
如果要真正使用版本控制系统，就要以纯文本方式编写文件。

因为文本是有编码的，比如中文有常用的GBK编码，日文有Shift_JIS编码，
如果没有历史遗留问题，强烈建议使用标准的UTF-8编码，所有语言使用同一种编码，既没有冲突，又被所有平台所支持。

    print 'hello'
    if a = 1:
    