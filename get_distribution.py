

from fetch.clone import  clone
from fetch.download_json import download_json

def get_distribution(language = 'python', max_docs  = 5):
	fetch_files(language, max_docs)
	

def fetch_files(language, max_docs): 
	query = 'https://api.github.com/search/repositories?q=language:%s&sort=stars&order=desc' %(language)
	for name, url in download_json(query,max_docs):
	clone(url,name)



def main():
	get_distribution()

if __name__ == '__main__':
    main()