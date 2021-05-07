import sys
import json as json


def read_file_to_string(filename):
    f = open(filename, 'rt')
    s = f.read()
    f.close()
    return s

files_train = read_file_to_string('programs_training.txt').split("\n")
files_train = files_train[:len(files_train)//8]
with open('/content/drive/MyDrive/test_task/js_train_light.txt', 'at') as f:
    for path in files_train:
        try:
            f_js = read_file_to_string(path)
            f.write('<s>' + f_js + '</s>')
        except:
            pass