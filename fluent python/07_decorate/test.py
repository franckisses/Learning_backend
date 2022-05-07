

import html
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

'''
>>> htmlize({1, 2, 3})
'<pre>{1, 2, 3}</pre>'
>>> htmlize(abs)
'<pre>&lt;built-in function abs&gt;</pre>'
>>> htmlize('Heimlich & Co.\n -a game')
'<pre>&#x27;Heimlich &amp; Co.\\n -a game&#x27;</pre>'
>>> htmlize(42)
'<pre>42</pre>'
>>> print(htmlize(['alpha', 66, {3, 2, 1}]))
<pre>[&#x27;alpha&#x27;, 66, {1, 2, 3}]</pre>
'''
