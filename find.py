import requests

def find():
    urlInput = input('Weblist: ')
    url = open(urlInput, 'r')
    print('\nContoh file: /wso.php, /up.php, /mini.php, /idx.php')
    shellext = input('Nama File Shell: ')
    print('\nContoh Judul: WebOrbShell, Uploader By, Indoxploit Shell')
    shelltitle = input('Judul Shell: ')
    for a in url.readlines():
        urla = a.replace('\n', '')
        print(' '+urla+shellext)
        r = requests.get(urla+shellext)
        if shelltitle in r.text:
            print(' {} --> Shell Found [{}]'.format(urla, shellext))
            saveshell = open('shell.txt', 'a')
            saveshell.write(urla+shellext+'\n')

find()
