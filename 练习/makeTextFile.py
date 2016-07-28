#!/usr/bin/env python

'makeTextFile.py -- create text file'

import os

# get filename
while True:
    fname = raw_input('Enter file name: ')
    if os.path.exists(fname):
        print"*** ERROR: '%s' already exists" % fname
    else:
        break

# get file content (text) lines
all = []
print "\nEnter lines ('.' by itself to quit).\n"

# loop until user terminates input
while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with NEWLINE line terminator
fobj = open(fname,'w')
fobj.write('\n'.join(all))
fobj.close()
print 'DONE!'



'''1 ~ 3行
UNIX启动行之后是模块的文档字符串。应该坚持写简洁并有用的文档字符串。这里我们写的有点短，不过对这段代码已经够用了。（建议读者看一下标准库中cgi模块的文档字符串，那是一个很好的示例）。
5 ~ 6行
之后我们导入os模块，在第6行我们为os.linesep属性取了一个新别名。这样做一方面可以缩短变量名，另一方面也能改善访问该变量的性能。
核心提示：使用局部变量替换模块变量
类似os.linesep这样的名字需要解释器做两次查询：（1）查找os以确认它是一个模块， （2）在这个模块中查找linesep变量。&为模块也是全局变量，我们多消耗了系统资源。如果你在一个函数中像这样频繁使用一个属性，我们建议你为该属性取一个本地变量别名。变量查找速度将会快很多——在查找全局变量之前，总是先查找本地变量。这也是一个让你的程序跑的更快的技巧：将经常用到的模块属性替换为一个本地引用。代码 “跑”得更快，而也不用老是敲那么长的变量名了。在我们的代码片段中，并没有定义函数，所以不能给你定义本地别名的示例。不过我们有一个全局别名，至少也减少了一次名字查询。
8 ~ 4行
显然这是一个无限循环，也就是说除非我们在while语句体中提供break语句，否则它会一直循环下去。
while语句根据后面的表达式决定是否进行下一次循环，而True则确保它一直循环下去。
10 ~ 14行
提示用户输入一个未使用的文件名。raw_input()内建函数接受一个“提示字符串”参数，作为对用户的提示信息。raw_input()返回用户输入的字符串，也就是为fname赋值。如果用户不小心输入了一个已经存在的文件的¿字，我们要提示这个用户重新输入另一个名字。os.path.exists()是os模块中一个有用的函数，帮助我们确认这一点。当有输入一个不存在的文件名时，os.path.exists()才会返回False,这时我们中断循环继续下面的代码。
16 ~ 26行
这部分代码提供用户指令，引导用户输入文件内容，一次一行。我们在第17行初始化了列表all，它用来保存每一行文本。第21行开始另一个无限循环，提示用户输入每一行文本，一行仅输入一个句点 （.）表示输入结束。23~26行的if-else语句判断是否满足结束条件以中止循环（24行），否则就再添加新的一行（26行）。
28 ~ 32行
现在所有内容都保存在内存当中，我们需要将它们保存到文件。第29行打开文件准备进行写操作，第30行将内存中的内容逐行写入文件。每个文件都需要一个行结束符（或文件结束字符）。第30行的结构称为列表解析，它进行以下工作：对我们文件的每一行，根据程序运行平台添加一个合适的行结束符。 ‘％s%s’为每一行添加行结束符，（x，ls）表示每一行及其行结束符，对Unix平台，是‘\n’,对DOS或win32平台，则是‘\r\n’。通过使用os.lineseq,我们不必关心程序运行在什么平台，也不必要根据不同的平台决定使用哪种行结束符。文件对象的writelines()方法接收包含行结束符的结果列表，并将它写入文件。'''
