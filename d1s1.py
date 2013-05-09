txt = '<112,76><90,76><112,34><90,34><112,90><76,34>'

def num1():
  a = tuple(filter(None, txt.split('>')))
	b = []
	for i in a:
		b.append('(' + i[1:] + ')')
	print b
#split txt into a list which looks like: ['<112,76', '<90,76', '<112,34', '<90,34', '<112,90', '<76,34', '']

def num2():qa = txt.split('>')
	b = []
  #remove '<' from list a and add parentheses to each item
	for x in a:
		b.append('(' + x[1:] + ')')

	#remove last item of list
	c = b[:b.__len__() -1]
