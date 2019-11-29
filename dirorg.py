#!/usr/bin/python3

import argparse
import os


def path():
    parse = argparse.ArgumentParser(
        add_help=True, description="Organiza seus arquivos em diferentes pastas de acordo com o tipo.")
    parse.add_argument('directory_path', type=str, default='./',
                       help="O caminho absoluto para a pasta.")
    return parse.parse_args().directory_path


documents = ['.log', '.txt', '.doc', '.docx', '.md', '.pdf', '.wps', '.odt']
picture = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
music = ['.mp3', '.wav']
compressed = ['.zip', '.rar', '.tar', '.gz', '.bz2', '.xz', '.war']
video = ['.3gp', '.mov', '.mp4', '.mkv', '.srt', '.avi']
web = ['.html', '.css', '.js', '.phar']
source = ['.py', '.c', '.cpp', '.java', '.json']


directories = [path() + '/Compressed', path() + '/Documents',
               path() + '/Pictures', path() + '/Music', path() + '/Video', path() + '/Web', path() + '/Source-codes',]

print("Isto deve organizar seus arquivos em diferentes pastas de acordo com o tipo!!")
print("Tem certeza que quer continuar? (s/n)")
flag = input('>>>')
if flag.lower() == 's':
    try:
        for d in directories:
            os.mkdir(d)
    except FileExistsError:
        pass

    for files in os.listdir(path()):
        dot = (files.rfind('.'))
        if dot is not 0 and dot is not -1:
            if files[dot:].lower() in music:
                os.rename(path() + '/' + files, path() + '/Music/' + files)
            if files[dot:].lower() in picture:
                os.rename(path() + '/' + files, path() + '/Pictures/' + files)
            if files[dot:].lower() in documents:
                os.rename(path() + '/' + files, path() + '/Documents/' + files)
            if files[dot:].lower() in compressed:
                os.rename(path() + '/' + files, path() +
                          '/Compressed/' + files)
            if files[dot:].lower() in video:
                os.rename(path() + '/' + files, path() + '/Video/' + files)
            if files[dot:].lower() in web:
                os.rename(path() + '/' + files, path() + '/Web/' + files)
            if files[dot:].lower() in source:
                os.rename(path() + '/' + files, path() + '/Source-codes/' + files)    

    for d in directories:
        if os.listdir(d) is None:
            os.removedirs(d)
else:
    print("Exiting")
    os.sys.exit(0)
