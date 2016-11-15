

from fetch.clone import  clone
from fetch.download_json import download_json
from preprocess.count_characters import get_counts, get_count_test

def get_distribution(language = 'python', max_docs  = 1):
	directories = fetch_files(language, max_docs)
	character_count = get_counts(directories)
	print character_count

def fetch_files(language, max_docs):
	directories = []
	query = 'https://api.github.com/search/repositories?q=language:%s&sort=stars&order=desc' %(language)
	for name, url in download_json(query,max_docs):
		directories.append(clone(url,name))
	return directories

def main():
	#get_distribution()
	get_count_test


if __name__ == '__main__':
    main()