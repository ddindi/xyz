
import urllib2
import json

def download_json(query = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc',
				 max_repos = 5): 
	response = urllib2.urlopen(query)
	json_string = response.read()
	data = json.loads(json_string)
	for i, item in enumerate(data['items']):
		if i == max_repos: 
			break
		yield item['name'], item['clone_url']

def main():
	for name, clone_url in download_json(): 
		print name, clone_url

if __name__ == '__main__':
    main()