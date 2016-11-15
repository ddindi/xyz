import os

def is_python_file(file_name):
    PYTHON_EXTENSIONS = ['.py']
    
    for extension in PYTHON_EXTENSIONS:
        if file_name[-len(extension):] == extension:
            return True
    
    return False


def get_python_files(directory):
    walk = os.walk(directory)
    return ('{}/{}'.format(dir_path, file_name) for dir_path, _, file_names in walk for file_name in file_names
        if is_python_file(file_name))
