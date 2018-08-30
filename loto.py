from requests_html import HTMLSession
from sys import argv


def loto(*number):
	r = HTMLSession().get('http://ketqua.net')
	result = []
	for i in range(0, 8):
		for x in range(0, 4):
			try:
				result.append(r.html.find('#rs_{}_{}'.format(i, x))[0].text[-2:])
			except:
				pass
	count = 0
	for n in number:
		if str(n) in result:
			count += 1
			print('number {}'.format(n)) 
	if count == 0:
		return result
	else:
		return('bingbong')


print(loto(*argv))