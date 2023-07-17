from lxml import etree

text = """
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
"""

html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('UTF-8'))
# 也可以用参数让etree.HTML()方法不补全代码
# html = etree.HTML(text,etree.HTMLParser())

