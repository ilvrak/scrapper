from sys import argv
import requests
from bs4 import BeautifulSoup
import csv

def get_soup(url):
    '''getting soup, if requests failed - returns None'''
    responce = requests.get(url)
    print('checking', url, responce.status_code)
    if responce.status_code == 200:
        return BeautifulSoup(responce.content, 'html.parser')
    return None

def wfile(content):
    '''for testing'''
    with open('soup.txt', 'w', encoding='utf-8') as f:
        f.write(str(content))
    return None

def write_csv(dict, filename='output.csv'):
    '''at the end - writes data to csv'''
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames = ['Name', 'Version'],
            delimiter = ',',
            extrasaction='ignore',
            lineterminator='\r',
            escapechar=' ',
            quoting=csv.QUOTE_NONE
            )

        writer.writeheader()
        for name, version in dict.items():
            writer.writerow({'Name': name, 'Version': version})
    return None

urls = {'chrome'       :'https://omahaproxy.appspot.com/win',
        'edge'         :'https://www.microsoft.com/ru-ru/edge/business/download',
        'yandex'       :'https://browser.yandex.ru/constructor/',
        'firefox'      :'https://www.mozilla.org/en-US/firefox/releases/',
        'reader'       :'https://www.adobe.com/devnet-docs/acrobatetk/tools/ReleaseNotesDC/index.html',
        'xmind'        :'https://www.xmind.net/download/xmind8',
        'java'         :'https://www.oracle.com/java/technologies/',
        'far'          :'https://www.farmanager.com/download.php?l=ru',
        'powerbi'      :'https://www.microsoft.com/ru-RU/download/details.aspx?id=58494',
        'notepad'      :'https://notepad-plus-plus.org/downloads/',
        'bitrix'       :'https://bitrix24.ru.malavida.com/windows/#gref',
	    'microsip'     :'https://www.microsip.org/downloads',
	    'skype'        :'https://www.techspot.com/downloads/50-skype.html',
	    'openshell'    :'https://github.com/Open-Shell/Open-Shell-Menu/tags',
	    'aimp'         :'https://www.aimp.ru/?do=download&os=windows',
	    'freecommander':'https://freecommander.com/ru/%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8/',
        'rdm'          :'https://remotedesktopmanager.com/home/downloadenterprise',
        '7zip'         :'https://www.7-zip.org/',
        'winrar'       :'https://www.rarlab.com/download.htm',
        'vlc'          :'https://www.videolan.org/vlc/index.ru.html',
        'freecam'      :'https://www.ispring.ru/ispring-free-cam/thanks-for-download?said=1683793&type=static',
        'lightshot'    :'https://community.chocolatey.org/packages/lightshot.install',
        'paintnet'     :'https://github.com/paintdotnet/release/releases/latest',
        'fsvrecorder'  :'https://www.dvdvideosoft.com/ru/products/dvd/Free-Screen-Video-Recorder.htm',
        'itunes'       :'https://community.chocolatey.org/packages/iTunes',
        'joplin'       :'https://github.com/laurent22/joplin/releases/latest',
        'joxi'         :'https://softobase.com/ru/joxi',
        'keepassxc'    :'https://keepassxc.org/download/#windows'
        }


versions = {}


def scrapper():

    app = 'chrome'
    soup = get_soup(urls[app])
    version = str(soup)
    versions[app] = version

    app = 'edge'
    soup = get_soup(urls[app])
    version = soup.find(class_='m-product-placement-item f-size-large').find(class_='build-version').text[1:-1]
    versions[app] = version
    
    app = 'yandex'
    soup = get_soup(urls[app])
    version = soup.find(class_='lc-styled-text__text lc-styled-text__text_align_initial').text.split()[-1]
    versions[app] = version

    app = 'firefox'
    soup = get_soup(urls[app])
    version = soup.find(class_='c-release-list').find('li').find('a').text
    versions[app] = version

    app = 'reader'
    soup = get_soup(urls[app])
    version = soup.find(class_='std std-ref').text.split()[0]
    versions[app] = version

    app = 'xmind'
    soup = get_soup(urls[app])
    preversion = ' '.join(soup.find('a', text='Window (exe)').get('href').split('/')[-1].split('-')[1:3])
    versions[app] = version

    app = 'java'
    soup = get_soup(urls[app])
    version = soup.find(href='/java/technologies/downloads/#java8').text.split()[-1]
    versions[app] = version

    app = 'far'
    soup = get_soup(urls[app])
    preversion = soup.find('b').text.split()
    version = preversion[2][1:] + '.' + preversion[4]
    versions[app] = version

    app = 'powerbi'
    soup = get_soup(urls[app])
    version = soup.find(class_='fileinfo').find('p').text
    versions[app] = version

    app = 'notepad'
    soup = get_soup(urls[app])
    version = soup.find(class_='patterns-list').find('a').text.split()[1]
    versions[app] = version

    app = 'bitrix'
    soup = get_soup(urls[app])
    version = soup.find(class_='ver').text
    versions[app] = version

    app = 'microsip'
    soup = get_soup(urls[app])
    version = soup.find(class_='box-inner').find('a').text.split('-')[-1][:-4]
    versions[app] = version

    app = 'skype'
    soup = get_soup(urls[app])
    version = soup.find(itemprop='softwareVersion').text
    versions[app] = version

    app = 'openshell'
    soup = get_soup(urls[app])
    version = soup.find(class_='Box-row position-relative d-flex').find('a').text.strip()
    versions[app] = version

    app = 'aimp'
    soup = get_soup(urls[app])
    version = '.'.join(soup.find(class_='button_download_text').text.split()[::2])[1:]
    versions[app] = version

    app = 'freecommander'
    soup = get_soup(urls[app])
    version = ' '.join(soup.find(class_='entry-content').find('span').text.split()[2:-2])
    versions[app] = version

    app = 'rdm'
    soup = get_soup(urls[app])
    version = soup.find(class_='compare-editions-right').find(class_='compare-editions-link').text.split()[1]
    versions[app] = version

    app = '7zip'
    soup = get_soup(urls[app])
    version = soup.find(class_='NewsTitle').text.split()[-1]
    versions[app] = version

    app = 'winrar'
    soup = get_soup(urls[app])
    version = soup.find(class_='headtbl').find('a').find('b').text.split()[-1]
    versions[app] = version

    app = 'vlc'
    soup = get_soup(urls[app])
    version = soup.find(id='downloadDetails').find(id='downloadVersion').text.strip()
    versions[app] = version

    app = 'freecam'
    soup = get_soup(urls[app])
    version = soup.find(id='downloadItemLink').get('href').split('/')[-1][-9:-4]
    versions[app] = version

    app = 'lightshot'
    soup = get_soup(urls[app])
    version = soup.find('title').text.split('|')[-1].split()[-1]
    versions[app] = version

    app = 'paintnet'
    soup = get_soup(urls[app])
    version = soup.find(class_='d-inline mr-3').text
    versions[app] = version

    app = 'fsvrecorder'
    soup = get_soup(urls[app])
    version = soup.find(class_='spec_table_padding1 spec_table_content_1').text.split()[-1]
    versions[app] = version

    app = 'itunes'
    soup = get_soup(urls[app])
    version = soup.find('title').text.split('|')[-1].split()[-1]
    versions[app] = version

    app = 'joplin'
    soup = get_soup(urls[app])
    version = soup.find(class_='d-inline mr-3').text[1:]
    versions[app] = version

    app = 'joxi'
    soup = get_soup(urls[app])
    version = soup.find(itemprop='softwareVersion').text.strip()
    versions[app] = version

    app = 'keepassxc'
    soup = get_soup(urls[app])
    version = soup.find(class_='label label-success').text[1:]
    versions[app] = version


if __name__ == '__main__':
    scrapper()
    write_csv(versions)
    print('done')