import requests
from bs4 import BeautifulSoup
from sys import argv

def get_soup(url):
    try:
        resp = requests.get(url)
        return BeautifulSoup(resp.content, 'html.parser')
    except:
        return None

def wfile(content):
    '''использую для теста получения кода страницы'''
    with open('soup.txt', 'w', encoding='utf-8') as f:
        f.write(str(content))
    return None


def scrapper1():

    # Chrome
    soup = get_soup('https://omahaproxy.appspot.com/win')
    version = str(soup)
    print('Chrome:', version)

    # Edge
    soup = get_soup('https://www.microsoft.com/ru-ru/edge/business/download')
    version = soup.find(class_='m-product-placement-item f-size-large').find(class_='build-version').text[1:-1]
    print('Edge:', version)

    # Yandex
    soup = get_soup('https://browser.yandex.ru/constructor/')
    version = soup.find(class_='lc-styled-text__text lc-styled-text__text_align_initial').text.split()[-1]
    print('Yandex:', version)

    # Firefox
    soup = get_soup('https://www.mozilla.org/en-US/firefox/releases/')
    version = soup.find(class_='c-release-list').find('li').find('a').text
    print('Firefox:', version)

    # Adobe
    soup = get_soup('https://www.adobe.com/devnet-docs/acrobatetk/tools/ReleaseNotesDC/index.html')
    version = soup.find(class_='std std-ref').text.split()[0]
    print('Adobe:', version)

    return None

def scrapper2():

    # XMind8
    soup = get_soup('https://www.xmind.net/download/previous/')
    tagtext = soup.find(class_='container clearfix').find('p').text
    version = tagtext.split()[7][1:-2]
    print('XMind8:', version)

    # Java JRE
    # использую левую ссылку, потому что оригинальная страница динамическая и её нельзя получить парсером
    soup = get_soup('https://www.oracle.com/java/technologies/')
    version = soup.find(href='/java/technologies/downloads/#java8').text.split()[-1]
    print('Java 8:', version)

    # FAR Manager
    soup = get_soup('https://www.farmanager.com/download.php?l=ru')
    preversion = soup.find('b').text.split()
    version = preversion[2][1:] + '.' + preversion[4]
    print('Far:', version)

    # Power BI
    soup = get_soup('https://www.microsoft.com/ru-RU/download/details.aspx?id=58494')
    version = soup.find(class_='fileinfo').find('p').text
    print('PowerBI:', version)

    # Notepad++
    soup = get_soup('https://notepad-plus-plus.org/downloads/')
    version = soup.find(class_='patterns-list').find('a').text.split()[1]
    print('Notepad++:', version)

    return None

def scrapper3():
    
    # BitrixDesktop - проблема, нет версии на сайте
    soup = get_soup('https://bitrix24.ru.malavida.com/windows/#gref')
    version = soup.find(class_='ver').text
    print('Bitrix:', version)

    # MicroSIP Lite
    soup = get_soup('https://www.microsip.org/downloads')
    version = soup.find(class_='box-inner').find('a').text.split('-')[-1][:-4]
    print('MicroSIP:', version)

    # Skype
    # нет версии на сайте, поэтому использую левую ссылку
    soup = get_soup('https://www.techspot.com/downloads/50-skype.html')
    version = soup.find(itemprop='softwareVersion').text
    print('Skype:', version)
    
    # OpenShell
    soup = get_soup('https://github.com/Open-Shell/Open-Shell-Menu/tags')
    version = soup.find(class_='Box-row position-relative d-flex').find('a').text.strip()
    print('OpenShell:', version)
    
    # AIMP
    soup = get_soup('https://www.aimp.ru/?do=download&os=windows')
    version = '.'.join(soup.find(class_='button_download_text').text.split()[::2])[1:]
    print('AIMP:', version)
    
    # FreeCommander XE
    soup = get_soup('https://freecommander.com/ru/%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8/')
    version = ' '.join(soup.find(class_='entry-content').find('span').text.split()[2:-2])
    print('FreeCommander:', version)
    
def scrapper4():
    # RDM
    soup = get_soup('https://remotedesktopmanager.com/home/downloadenterprise')
    version = soup.find(class_='compare-editions-right').find(class_='compare-editions-link').text.split()[1]
    print('RDM:', version)

    # 7Zip
    soup = get_soup('https://www.7-zip.org/')
    if soup:
        version = soup.find(class_='NewsTitle').text.split()[-1]
        print('7Zip:', version)
    else:
        print('7Zip:', 'connection failed')

    # WinRAR
    soup = get_soup('https://www.rarlab.com/download.htm')
    version = soup.find(class_='headtbl').find('a').find('b').text.split()[-1]
    print('WinRAR:', version)

    # VLC
    soup = get_soup('https://www.videolan.org/vlc/index.ru.html')
    version = soup.find(id='downloadDetails').find(id='downloadVersion').text.strip()
    print('VLC:', version)

    # FreeCam
    soup = get_soup('https://www.ispring.ru/ispring-free-cam/thanks-for-download?said=1683793&type=static')
    version = soup.find(id='downloadItemLink').get('href').split('/')[-1][-9:-4]
    print('FreeCam:', version)

    # Lightshot - проблема, нет версии на сайте
    soup = get_soup('https://community.chocolatey.org/packages/lightshot.install')
    version = soup.find('title').text.split('|')[-1].split()[-1]
    print('Lightshot:', version)

def scrapper5():
    # paint.net
    soup = get_soup('https://github.com/paintdotnet/release/releases/latest')
    version = soup.find(class_='d-inline mr-3').text
    print('paint.net:', version)

    # FreeScrenVideoRecorder
    soup = get_soup('https://www.dvdvideosoft.com/ru/products/dvd/Free-Screen-Video-Recorder.htm')
    version = soup.find(class_='spec_table_padding1 spec_table_content_1').text.split()[-1]
    print('FrScVidRec:', version)

    # iTunes
    soup = get_soup('https://community.chocolatey.org/packages/iTunes')
    version = soup.find('title').text.split('|')[-1].split()[-1]
    print('iTunes:', version)

    # Joplin
    soup = get_soup('https://github.com/laurent22/joplin/releases/latest')
    version = soup.find(class_='d-inline mr-3').text[1:]
    print('Joplin:', version)

    # Joxi - нет версии на сайте
    soup = get_soup('https://www.kcsoftwares.com/sumo/start/searchsumo.php?query=joxi')
    version = soup.find('table').find('font').text[2:]
    print('Joxi:', version)
    
    # KeePassXC
    soup = get_soup('https://keepassxc.org/download/#windows')
    version = soup.find(class_='label label-success').text[1:]
    print('KeePassXC:', version)


if __name__ == '__main__':
    try:
        set = int(argv[1])
        if set == 1:
            scrapper1()
        if set == 2:
            scrapper2()
        if set == 3:
            scrapper3()
        if set == 4:
            scrapper4()
        if set == 5:
            scrapper5()
    except:
        None

          