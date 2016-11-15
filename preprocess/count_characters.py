
from fetch.get_python_files import get_python_files
def get_counts(directories): 
	file_list = [file_name for directory in directories for file_name in get_python_files(directory)]
	character_count = {}
	for f in file_list: 
		count_characters(character_count,f)
	return character_count

def get_count_test(): 
	file_list = ['/Users/daviddindi/xyz/sample.py']
	character_count = {}
	for f in file_list: 
		count_characters(character_count,f)
	print character_count

def count_characters(character_count,f): 
	with open(f,'rb') as f: 
		for line in f: 
			for ch in line: 
				if ch not in character_count: 
					character_count[ch] = 0
				character_count[ch] += 1
def main():
	get_count_test()

if __name__ == '__main__':
    main()