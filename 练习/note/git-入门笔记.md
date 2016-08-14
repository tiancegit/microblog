## 安装git
Linux 安装 git：  
* sudo apt-get install git

windows 安装 git：  
* “https://git-for-windows.github.io/”，下载git-for-windows

安装完成之后，还要进行相对应的配置：  
* $ git config --global user.name "Your Name"
* $ git config --global user.email "email@example.com"

注意git config命令的--global参数，用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置.
当然也可以对某个仓库指定不同的用户名和Email地址。


## 命令：
git init : 把当前的目录初始化为git可以管理的仓库。  
git config : 进行git仓库相对应设置的设定。  
git add : 添加文件到git仓库内。  
git commit : 把文件提交到git仓库内。 -m 'new file'  参数m后面的是本次提交的说明，-最好是有意义的。  
git status : status 命令可以时刻掌握仓库的动态。可以看到那些文件进行修改，尚未提交到仓库！  
git diff : diff顾名思义，是查看difference（差异）；显示的是Unix通用的diff格式，用于比较修改前后的差异。  
git log : log 可以看到git仓库的提交历史。加上--pretty=oneline参数,可以简化输出信息.





注意事项
---
###git的适用范围
明确一下，所有的版本控制系统，其实只能跟踪文本文件的改动，比如TXT文件，网页，所有的程序代码等等，Git也不例外。
版本控制系统可以告诉你每次的改动，比如在第5行加了一个单词“Linux”，在第8行删了一个单词“Windows”。
而图片、视频这些二进制文件，虽然也能由版本控制系统管理，但没法跟踪文件的变化，只能把二进制文件每次改动串起来，
也就是只知道图片从100KB改成了120KB，但到底改了啥，版本控制系统不知道，也没法知道。

不幸的是，Microsoft的Word格式是二进制格式，因此，版本控制系统是没法跟踪Word文件的改动的，前面我们举的例子只是为了演示，
如果要真正使用版本控制系统，就要以纯文本方式编写文件。

因为文本是有编码的，比如中文有常用的GBK编码，日文有Shift_JIS编码，
如果没有历史遗留问题，强烈建议使用标准的UTF-8编码，所有语言使用同一种编码，既没有冲突，又被所有平台所支持。


### 添加文件到Git仓库，分两步：

* 第一步，使用命令git add <file>，注意，可反复多次使用，添加多个文件；

* 第二步，使用命令git commit，完成。


###git log 中的commit 版本号问题

```commit 5a79abaaca6fa6ad7b8d7cb59790e117f8ee3482
Author: mail.com<mail.com>
Date:   Sun Aug 14 16:33:15 2016 +0800
```


commit 5a79abaaca6fa6ad7b8d7cb59790e117f8ee3482  
这一串十六进制的数字是commit(版本号)，和SVN不一样，git的commit id不是以1,2,3...递增的数字。  
而是一个SHA1计算出来的一个非常大的数字，用十六进制表示。每次提交的commit id 都是不一样的，以记录为准。
因为git是分布式的版本控制系统，多人在同一个版本库内工作，要是以1,2,3..作为版本号,将会互相冲突。 

需要友情提示的是，你看到的一大串类似3628164...882e1e0的是commit id（版本号），和SVN不一样，Git的commit id不是1，2，3……递增的数字，
而是一个SHA1计算出来的一个非常大的数字，用十六进制表示，而且你看到的commit id和我的肯定不一样，以你自己的为准。为什么commit id需要用这么一大串数字表示呢
？因为Git是分布式的版本控制系统，后面我们还要研究多人在同一个版本库里工作，如果大家都用1，2，3……作为版本号，那肯定就冲突了。




