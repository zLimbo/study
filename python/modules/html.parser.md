#### [HTMLParser](https://docs.python.org/zh-cn/3/library/html.parser.html?highlight=html)

```python
rom html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()
```

解析一个文档类型声明:

```python
>>> parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
...             '"http://www.w3.org/TR/html4/strict.dtd">')
Decl     : DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"
```

解析一个具有一些属性和标题的元素:

```python
>>> parser.feed('<img src="python-logo.png" alt="The Python logo">')
Start tag: img
     attr: ('src', 'python-logo.png')
     attr: ('alt', 'The Python logo')
>>>
>>> parser.feed('<h1>Python</h1>')
Start tag: h1
Data     : Python
End tag  : h1
```

`script` 和 `style` 元素中的内容原样返回，无需进一步解析:

```python
>>> parser.feed('<style type="text/css">#python { color: green }</style>')
Start tag: style
     attr: ('type', 'text/css')
Data     : #python { color: green }
End tag  : style

>>> parser.feed('<script type="text/javascript">'
...             'alert("<strong>hello!</strong>");</script>')
Start tag: script
     attr: ('type', 'text/javascript')
Data     : alert("<strong>hello!</strong>");
End tag  : script
```

解析注释:

```python
>>> parser.feed('<!-- a comment -->'
...             '<!--[if IE 9]>IE-specific content<![endif]-->')
Comment  :  a comment
Comment  : [if IE 9]>IE-specific content<![endif]
```

解析命名或数字形式的字符引用，并把他们转换到正确的字符（注意：这 3 种转义都是 `'>'` ）:

```python
>>> parser.feed('&gt;&#62;&#x3E;')
Named ent: >
Num ent  : >
Num ent  : >
```

填充不完整的块给 [`feed()`](https://docs.python.org/zh-cn/3/library/html.parser.html?highlight=html#html.parser.HTMLParser.feed) 执行，[`handle_data()`](https://docs.python.org/zh-cn/3/library/html.parser.html?highlight=html#html.parser.HTMLParser.handle_data) 可能会多次调用（除非 *convert_charrefs* 被设置为 `True` ）:

```python
>>> for chunk in ['<sp', 'an>buff', 'ered ', 'text</s', 'pan>']:
...     parser.feed(chunk)
...
Start tag: span
Data     : buff
Data     : ered
Data     : text
End tag  : span
```

解析无效的 HTML (例如：未引用的属性）也能正常运行:

```python
>>> parser.feed('<p><a class=link href=#main>tag soup</p ></a>')
Start tag: p
Start tag: a
     attr: ('class', 'link')
     attr: ('href', '#main')
Data     : tag soup
End tag  : p
End tag  : a
```



## [`HTMLParser`](https://docs.python.org/zh-cn/3/library/html.parser.html?highlight=html#html.parser.HTMLParser) 方法

[`HTMLParser`](https://docs.python.org/zh-cn/3/library/html.parser.html?highlight=html#html.parser.HTMLParser) 实例有下列方法：

- `HTMLParser.``feed`(*data*)

  填充一些文本到解析器中。如果包含完整的元素，则被处理；如果数据不完整，将被缓冲直到更多的数据被填充，或者 [`close()`](https://docs.python.org/zh-cn/3/library/html.parser.html?highlight=html#html.parser.HTMLParser.close) 被调用。*data* 必须为 [`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 类型。

- `HTMLParser.``close`()

  如同后面跟着一个文件结束标记一样，强制处理所有缓冲数据。这个方法能被派生类重新定义，用于在输入的末尾定义附加处理，但是重定义的版本应当始终调用基类 [`HTMLParser`](https://docs.python.org/zh-cn/3/library/html.parser.html?highlight=html#html.parser.HTMLParser) 的 [`close()`](https://docs.python.org/zh-cn/3/library/html.parser.html?highlight=html#html.parser.HTMLParser.close) 方法。

- `HTMLParser.``reset`()

  重置实例。丢失所有未处理的数据。在实例化阶段被隐式调用。

- `HTMLParser.``getpos`()

  返回当前行号和偏移值。

- `HTMLParser.``get_starttag_text`()

  返回最近打开的开始标记中的文本。 结构化处理时通常应该不需要这个，但在处理“已部署”的 HTML 或是在以最小改变来重新生成输入时可能会有用处（例如可以保留属性间的空格等）。

下列方法将在遇到数据或者标记元素的时候被调用。他们需要在子类中重载。基类的实现中没有任何实际操作（除了 [`handle_startendtag()`](https://docs.python.org/zh-cn/3/library/html.parser.html?highlight=html#html.parser.HTMLParser.handle_startendtag) ）：

- `HTMLParser.``handle_starttag`(*tag*, *attrs*)

  这个方法在标签开始的时候被调用（例如： `<div id="main">` ）。*tag* 参数是小写的标记名。*attrs* 参数是一个 `(name, value)` 形式的列表，包含了所有在标记的 `<>` 括号中找到的属性。*name* 转换为小写，*value* 的引号被去除，字符和实体引用都会被替换。实例中，对于标签 `<A HREF="https://www.cwi.nl/">`，这个方法将以下列形式被调用 `handle_starttag('a', [('href', 'https://www.cwi.nl/')])` 。[`html.entities`](https://docs.python.org/zh-cn/3/library/html.entities.html#module-html.entities) 中的所有实体引用，会被替换为属性值。

- `HTMLParser.``handle_endtag`(*tag*)

  此方法被用来处理元素的结束标记（例如： `</div>` ）。*tag* 参数是小写的标签名。

- `HTMLParser.``handle_startendtag`(*tag*, *attrs*)

  类似于 [`handle_starttag()`](https://docs.python.org/zh-cn/3/library/html.parser.html?highlight=html#html.parser.HTMLParser.handle_starttag), 只是在解析器遇到 XHTML 样式的空标记时被调用（ `<img ... />`）。这个方法能被需要这种特殊词法信息的子类重载；默认实现仅简单调用 [`handle_starttag()`](https://docs.python.org/zh-cn/3/library/html.parser.html?highlight=html#html.parser.HTMLParser.handle_starttag) 和 [`handle_endtag()`](https://docs.python.org/zh-cn/3/library/html.parser.html?highlight=html#html.parser.HTMLParser.handle_endtag) 。

- `HTMLParser.``handle_data`(*data*)

  这个方法被用来处理任意数据（例如：文本节点和 `<script>...</script>` 以及 `<style>...</style>` 中的内容）。

- `HTMLParser.``handle_entityref`(*name*)

  这个方法被用于处理 `&name;` 形式的命名字符引用（例如 `>`），其中 *name* 是通用的实体引用（例如： `'gt'`）。如果 *convert_charrefs* 为 `True`，该方法永远不会被调用。

- `HTMLParser.``handle_charref`(*name*)

  这个方法被用来处理 `&#NNN;` 和 `&#xNNN;` 形式的十进制和十六进制字符引用。例如，`>` 等效的十进制形式为 `>` ，而十六进制形式为 `>` ；在这种情况下，方法将收到 `'62'` 或 `'x3E'` 。如果 *convert_charrefs* 为 `True` ，则该方法永远不会被调用。

- `HTMLParser.``handle_comment`(*data*)

  这个方法在遇到注释的时候被调用（例如： `<!--comment-->` ）。例如， `<!-- comment -->` 这个注释会用 `' comment '` 作为参数调用此方法。Internet Explorer 条件注释（condcoms）的内容也被发送到这个方法，因此，对于 `<!--[if IE 9]>IE9-specific content<![endif]-->` ，这个方法将接收到 `'[if IE 9]>IE9-specific content<![endif]'` 。

- `HTMLParser.``handle_decl`(*decl*)

  这个方法用来处理 HTML doctype 申明（例如 `<!DOCTYPE html>` ）。*decl* 形参为 `<!...>` 标记中的所有内容（例如： `'DOCTYPE html'` ）。

- `HTMLParser.``handle_pi`(*data*)

  此方法在遇到处理指令的时候被调用。*data* 形参将包含整个处理指令。例如，对于处理指令 `<?proc color='red'>` ，这个方法将以 `handle_pi("proc color='red'")` 形式被调用。它旨在被派生类重载；基类实现中无任何实际操作。注解 [`HTMLParser`](https://docs.python.org/zh-cn/3/library/html.parser.html?highlight=html#html.parser.HTMLParser) 类使用 SGML 语法规则处理指令。使用 `'?'` 结尾的 XHTML 处理指令将导致 `'?'` 包含在 *data* 中。

- `HTMLParser.``unknown_decl`(*data*)

  当解析器读到无法识别的声明时，此方法被调用。*data* 形参为 `<![...]>` 标记中的所有内容。某些时候对派生类的重载很有用。基类实现中无任何实际操作。