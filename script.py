import sys
# import urllib.request
import requests

def fetch(url):
    responce = requests.get(url)
    print(strip_tags(responce.text))
    # with urllib.request.urlopen(url) as responce:
    #     contents = responce.read()
	# do something with contents

def strip_tags(html):
    def f():
        b = 0
        for x in html:
            if x == '<':
                b += 1
            elif x == '>':
                b -= 1
            else:
                if b is 0:
                    yield x
    return ''.join(f())

if __name__ == '__main__':
    fetch(sys.argv[1])

