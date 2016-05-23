#! python3
# BeautifulSoup.py - example usage of BeautifulSoup.py and web scraping with Python

import bs4

example_file = open("example.html")
example_soup = bs4.BeautifulSoup(example_file.read())

# The select method will return a list of Tag objects
# The list wil contain one Tag object for every match
elems = example_soup.select("#author")

# class 'list
print(type(elems))

# 1
print(len(elems))

# class 'bs4.element.Tag'
print(type(elems[0]))

# Al Sweigart
elems[0].getText()

# '<span id="author">Al Sweigart</span>'
print(str(elems[0]))

# {'id': 'author'}
print(elems[0].attrs)

# Pull all the <p> elements from the BeautifulSoup object
pElems = example_soup.select('p')

# '<p>Download my <strong>Python</strong> book from <a href="http:// inventwithpython.com">my website</a>.</p>'
print(str(pElems[0]))

# 'Download my Python book from my website.'
pElems[0].getText()

# '<p class="slogan">Learn Python the easy way!</p>'
print(str(pElems[1]))

# 'Learn Python the easy way!'
pElems[1].getText()

# '<p>By <span id="author">Al Sweigart</span></p>'
print(str(pElems[2]))

# 'By Al Sweigart'
pElems[2].getText()

# The get method for Tag objects makes it simple to access attribute values from an element
# The method is passed a string of an attribute name and returns that attribute's value
soup = bs4.BeautifulSoup(open('example.html'))
spam_elem = soup.select('span')[0]

# '<span id="author">Al Sweigart</span>'
print(str(spam_elem))

# 'author'
spam_elem.get('id')

# None
print(spam_elem.get('some_nonexistent_addr'))

# {'id: 'author'}
print(spam_elem.attrs)
