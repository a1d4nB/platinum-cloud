import os
import re

def clean_filename(filename):
    pattern = r'(_[0-9]+)(\s+.+)?(?=\.)'
    cleaned_name = re.sub(pattern, '', filename)
    return cleaned_name

directory = 'Music'

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isdir(file_path):
        continue

    new_name = clean_filename(filename)
    new_file_path = os.path.join(directory, new_name)

    os.rename(file_path, new_file_path)
    print(f'Renamed "{filename}" to "{new_name}"')