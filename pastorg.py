#!/usr/bin/python3

import argparse
import os


def path():
    parse = argparse.ArgumentParser(
        add_help=True, description="Organiza seus arquivos em diferentes pastas de acordo com o tipo.")
    parse.add_argument('directory_path', type=str, default='./',
                       help="O caminho absoluto para a pasta.")
    return parse.parse_args().directory_path


textos = ['.log', '.txt', '.doc', '.docx', '.md', '.pdf', '.wps', '.odt', '.xps']
imagens = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.nef', '.wmf']
audios = ['.mp3', '.wav', '.amr', '.wma', '.aac', '.opus']
comprimidos = ['.zip', '.rar', '.tar', '.gz', '.bz2', '.xz', '.war']
videos = ['.3gp', '.mov', '.mp4', '.mkv', '.srt', '.avi']
web = ['.html', '.css', '.js', '.phar']
planilhas = ['.csv', '.cpp', '.xlsx', '.xls']


directories = [path() + '/Comprimidos', path() + '/Textos',
               path() + '/Imagens', path() + '/Audios', path() + '/Videos', path() + '/Web', path() + '/Planilhas',]

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
            if files[dot:].lower() in audios:
                os.rename(path() + '/' + files, path() + '/Audios/' + files)
            if files[dot:].lower() in imagens:
                os.rename(path() + '/' + files, path() + '/Imagens/' + files)
            if files[dot:].lower() in textos:
                os.rename(path() + '/' + files, path() + '/Textos/' + files)
            if files[dot:].lower() in comprimidos:
                os.rename(path() + '/' + files, path() +
                          '/Comprimidos/' + files)
            if files[dot:].lower() in videos:
                os.rename(path() + '/' + files, path() + '/Videos/' + files)
            if files[dot:].lower() in web:
                os.rename(path() + '/' + files, path() + '/Web/' + files)
            if files[dot:].lower() in planilhas:
                os.rename(path() + '/' + files, path() + '/Planilhas/' + files)    

    for d in directories:
        if os.listdir(d) is None:
            os.removedirs(d)
else:
    print("Exiting")
    os.sys.exit(0)
