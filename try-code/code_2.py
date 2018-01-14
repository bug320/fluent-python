# -*- coding: utf-8 -*-
"""
@author  : bug320
@purpose : learn&try Ch5: 一等函数: tag 函数
@date    : 2018-01-04
@note    : `learn&try` `流畅的python`
"""


def tag(name, *content, **attrs):
    """Generator one or more HTML tags 生成一个或者多个HTML标签 原文是python3 的，改写成立python2可用的"""
    if "cls" in attrs.keys():
        attrs['class'] = attrs['cls']
        del attrs['cls']
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                        (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)
    pass

print "1",tag('br') == "<br />"
print "2",tag("p", 'hello') == "<p>hello</p>"
print "3",tag("p","hello","word") == "<p>hello</p>\n<p>word</p>"
print "4",tag("p", 'hello',id=33) == '<p id="33">hello</p>'

print "5",tag("p", 'hello', 'world', cls='sidebar') == ('<p class="sidebar">hello</p>\n'
                                                    '<p class="sidebar">world</p>')
print "6",tag(content = 'testing', name='img') == '<img content="testing" />'
my_tag = {'name':'img','title':"Sunset Boulevard", 
          'src':'sunset.jpg','cls':'framed'}
print "7",tag(**my_tag) == '<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'

print "1",tag('br')
print "2",tag("p", 'hello') 
print "3",tag("p","hello","word") 
print "4",tag("p", 'hello',id=33) 

print "5",tag("p", 'hello', 'world', cls='sidebar') 
print "6",tag(content = 'testing', name='img') 
print "7",tag(**my_tag) 


