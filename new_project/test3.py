import requests


url = 'http://www.baidu.com/'

resp = requests.get(url=url)


print(resp.text)