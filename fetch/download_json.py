
import urllib2
import json

def download_json(input_link = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc',
				 max_repos = 5): 
	response = urllib2.urlopen(input_link)
	json_string = response.read()
	data = json.loads(json_string)
	for i, item in enumerate(data['items']):
		if i == max_repos: 
			break
		yield item['clone_url']

def main():
	for link in download_json(): 
		print link

if __name__ == '__main__':
    main()