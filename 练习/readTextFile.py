#!/usr/bin/env python

'readTextFile.py -- read and display text file'

#get filename
fname = raw_input('Enter filename:')
print

#attmpt to open file for reading
try:
    fodj = open(fname, 'r')
except IOError, e:
    print '*** file open error', e
else:
    #display contents to the screen
    for eachline in fodj:
        print eachline,
    fodj.close()



'''脚本的剩余部分展示了一种新的Python结构，try-except-else语句。try子句是一段我们希望监测错误的代码块。
在第10〜11行代码，我们尝试打开用户输入的文件。except子句是我们处理错误的地方。在12〜13行，我们检查open()是否失败——通常是IOError类型的错误。
最后，14〜18行的else子句在try代码块运行无误时执行。我们在这儿将文件的每一行显示在屏幕上。
注意由于我们没有移除代表每行结束的行结束符，我们不得不抵制print语句自动生成的行结束符——通过在print语句的最后加一个逗号可以达到这一目的。
第18行关闭文件，从而结束这段脚本。最后要讲的一点是关于使用os.path.exists()和异常处理：一般程序员倾向于使用前者，
因为有一个现成的函数可以检查错误条件——并且很简单，这是个布尔函数，它会告你“是”还是“不是”（注意，这个函数内可能已经有异常处理代码）。
那你为什么还要重新发明一个轮子来干同样一件事？异常处理最适用的场合，是在没有合适的函数处理异常状况的时候。这时程序员必须识别这些非正常的错误，并做出相应处理。
对我们的例子来说，我们能够通过检查文件是否存在来避免异常发生，不过因为有可能因为其他原因造成文件打开失败，比如缺少权限，网络驱动器突然连接失败等等。
从更安全的角度来说，就不应该使用类似os.path.exists()之类的函数，而是使用异常处理，尤其是在没有合适函数的情况下更应如此。'''