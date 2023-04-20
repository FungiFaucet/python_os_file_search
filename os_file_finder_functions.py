import os
import time
from tqdm import tqdm

def find_by_file_size(file_size, directory):
    files_over_file_size = 0
    files_under_file_size = 0
    bytes_in_gig = 1073741824
    file_size = file_size * bytes_in_gig # converting gigabytes to bytes for filesize comparison
    total_big_files_size_combined = 0
    found_files_over_size = []

    for dir_path, dir_names, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dir_path, filename)
            size = os.path.getsize(filepath)
            if size >= file_size:
                #print(f'{filename} : {size / bytes_in_gig:.2f} Gigabytes ')
                found_files_over_size
                files_over_file_size += 1
                total_big_files_size_combined += size
            else:
                files_under_file_size += 1

    total_files = files_over_file_size + files_under_file_size
    print(f'Total files checked: {total_files}')
    print(f'Total files over size limit: {files_over_file_size}')
    print(f'Total storage saved if 100% of files over size limit are deleted: {total_big_files_size_combined / bytes_in_gig:.2f} Gigabytes')