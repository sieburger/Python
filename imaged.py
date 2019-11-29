#!/usr/bin/python3

import argparse
import os


def path():
    parse = argparse.ArgumentParser(
        add_help=True, description="Organiza seus arquivos em diferentes pastas de acordo com o tipo.")
    parse.add_argument('directory_path', type=str, default='./',
                       help="O caminho absoluto para a pasta.")
    return parse.parse_args().directory_path


imagens = ['.png', '.nef']
imagens1 = ['.jpg']
imagens2 = ['.jpeg']
imagens3 = ['.bmp']
videos = ['.mp4', '.3gp']
#videos1 = ['.3gp', '.avi']
#videos2 = ['.mov']


directories = [path() + '/Imagens', path() + '/Imagens1', path() + '/Imagens2', path() + '/Imagens3', path() + '/Videos',]
# path() + '/Videos1', path() + '/Videos2',
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
            if files[dot:].lower() in imagens:
                os.rename(path() + '/' + files, path() + '/Imagens/' + files)
            if files[dot:].lower() in imagens:
                os.rename(path() + '/' + files, path() + '/Imagens1/' + files)
            if files[dot:].lower() in imagens:
                os.rename(path() + '/' + files, path() + '/Imagens2/' + files)
            if files[dot:].lower() in imagens:
                os.rename(path() + '/' + files, path() + '/Imagens3/' + files)
            if files[dot:].lower() in videos:
                os.rename(path() + '/' + files, path() + '/Videos/' + files)
#            if files[dot:].lower() in videos:
#                os.rename(path() + '/' + files, path() + '/Videos1/' + files)
#            if files[dot:].lower() in videos:
#                os.rename(path() + '/' + files, path() + '/Videos2/' + files)
            

    for d in directories:
        if os.listdir(d) is None:
            os.removedirs(d)
else:
    print("Exiting")
    os.sys.exit(0)
