
from fetch.extract_files as ef

def get_counts(): 
	file_list = ef()
	character_count = {}
	for f in file_list: 
		count_characters(chracter_count,f)
	return chracter_count

def count_characters(character_count,f): 
	with open(f,'rb') as f: 
		for line in f: 
			for ch in line: 
				if ch not in chracter_count: 
					character_count[ch] = 0
				chracter_count[ch] += 1
def main():
	get_counts()

if __name__ == '__main__':
    main()