# ====== imports block ================================== #
import requests
from bs4 import BeautifulSoup
import csv
from sys import argv
from os import getcwd
from random import choice

# ====== constants block ================================== #
desktop_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Mozilla/5.0 (X11; Linux i686; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Mozilla/5.0 (Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (X11; Linux i686; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/97.0.1072.69',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/97.0.1072.69',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 OPR/83.0.4254.16',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 OPR/83.0.4254.16',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 OPR/83.0.4254.16',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 OPR/83.0.4254.16',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Vivaldi/4.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Vivaldi/4.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Vivaldi/4.3',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Vivaldi/4.3',
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Vivaldi/4.3',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 YaBrowser/22.1.0 Yowser/2.5 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 YaBrowser/22.1.0 Yowser/2.5 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 YaBrowser/22.1.0 Yowser/2.5 Safari/537.36',
]

apps = {
    'chrome':        {'packageid': 'AAA00014', 'checkurl': 'https://omahaproxy.appspot.com/win', 'isofficiallink': True,
                      'findmethod': "str(soup)", 'ver': '',
                      'downurl': 'https://chromeenterprise.google/browser/download/thank-you/?platform=WIN64_MSI&channel=stable&usagestats=0'},
    'edge':          {'packageid': 'AAA00025', 'checkurl': 'https://www.microsoft.com/ru-ru/edge/business/download', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='m-product-placement-item f-size-large').find(class_='build-version').text[1:-1]", 'ver': '',
                      'downurl': 'https://www.microsoft.com/ru-ru/edge/business/download'},
    'yandex':        {'packageid': 'AAA00022', 'checkurl': 'https://browser.yandex.ru/corp/', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='lc-styled-text__text lc-styled-text__text_align_initial').text.split()[-1]", 'ver': '',
                      'downurl': 'https://browser.yandex.ru/constructor/build/2bbda80e-1d48-4c3c-99a0-3dce6f25edd8/'},
    'firefox':       {'packageid': 'AAA000BA', 'checkurl': 'https://www.mozilla.org/en-US/firefox/releases/', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='c-release-list').find('li').find('a').text", 'ver': '',
                      'downurl': 'https://www.mozilla.org/ru/firefox/enterprise/#download'},
    'reader':        {'packageid': 'AAA00012', 'checkurl': 'https://www.adobe.com/devnet-docs/acrobatetk/tools/ReleaseNotesDC/index.html', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='std std-ref').text.split()[0]", 'ver': '',
                      'downurl': 'https://www.adobe.com/devnet-docs/acrobatetk/tools/ReleaseNotesDC/index.html'},
    'xmind':         {'packageid': 'AAA00071', 'checkurl': 'https://www.xmind.net/download/previous/', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='container clearfix').find('p').text.split()[7][1:-2]", 'ver': '',
                      'downurl': 'https://www.xmind.net/download/xmind8'},
    'java':          {'packageid': 'AAA00016', 'checkurl': 'https://www.oracle.com/java/technologies/', 'isofficiallink': True,
                      'findmethod': "soup.find(href='/java/technologies/downloads/#java8').text.split()[-1]", 'ver': '',
                      'downurl': 'https://java.com/ru/download/manual.jsp'},
    'far':           {'packageid': 'AAA0000B', 'checkurl': 'https://www.farmanager.com/download.php?l=ru', 'isofficiallink': True,
                      'findmethod': "soup.find('b').text.split()[2][1:] + '.' + soup.find('b').text.split()[4]", 'ver': '',
                      'downurl': 'https://www.farmanager.com/download.php?l=ru'},
    'powerbi':       {'packageid': 'AAA000B8', 'checkurl': 'https://www.microsoft.com/ru-RU/download/details.aspx?id=58494', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='fileinfo').find('p').text", 'ver': '',
                      'downurl': 'https://www.microsoft.com/ru-ru/download/confirmation.aspx?id=58494'},
    'notepad':       {'packageid': 'AAA00070', 'checkurl': 'https://notepad-plus-plus.org/downloads/', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='patterns-list').find('a').text.split()[1]", 'ver': '',
                      'downurl': 'https://notepad-plus-plus.org/downloads/'},
    'bitrix':        {'packageid': 'AAA0001E', 'checkurl': 'https://bitrix24.ru.malavida.com/windows/#gref', 'isofficiallink': False,
                      'findmethod': "soup.find(class_='ver').text", 'ver': '',
                      'downurl': 'https://www.bitrix24.ru/features/desktop.php'},
    'microsip':      {'packageid': 'AAA0006F', 'checkurl': 'https://www.microsip.org/downloads', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='box-inner').find('a').text.split('-')[-1][:-4]", 'ver': '',
                      'downurl': 'https://www.microsip.org/downloads'},
    'skype':         {'packageid': 'AAA00042', 'checkurl': 'https://www.techspot.com/downloads/50-skype.html', 'isofficiallink': False,
                      'findmethod': "soup.find(itemprop='softwareVersion').text", 'ver': '',
                      'downurl': 'https://go.skype.com/windows.desktop.download'},
    'openshell':     {'packageid': 'AAA00023', 'checkurl': 'https://github.com/Open-Shell/Open-Shell-Menu/tags', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='Box-row position-relative d-flex').find('a').text.strip()", 'ver': '',
                      'downurl': 'https://github.com/Open-Shell/Open-Shell-Menu/releases'},
    'aimp':          {'packageid': 'AAA0008A', 'checkurl': 'https://www.aimp.ru', 'isofficiallink': True,
                      'findmethod': "'.'.join(soup.find(class_='button_download_text').text.split()[::2])[1:]", 'ver': '',
                      'downurl': 'https://www.aimp.ru/?do=download.file&id=4'},
    'freecommander': {'packageid': 'AAA00062', 'checkurl': 'https://freecommander.com/ru/%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8/', 'isofficiallink': True,
                      'findmethod': "' '.join(soup.find(class_='entry-content').find('span').text.split()[2:-2])", 'ver': '',
                      'downurl': 'https://freecommander.com/ru/%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8/'},
    'rdm':           {'packageid': 'AAA000B9', 'checkurl': 'https://remotedesktopmanager.com/home/downloadenterprise', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='compare-editions-right').find(class_='compare-editions-link').text.split()[1]", 'ver': '',
                      'downurl': 'https://remotedesktopmanager.com/home/downloadenterprise'},
    '7zip':          {'packageid': 'AAA00017', 'checkurl': 'https://www.7-zip.org/', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='NewsTitle').text.split()[-1]", 'ver': '',
                      'downurl': 'https://www.7-zip.org/'},
    'winrar':        {'packageid': 'AAA00027', 'checkurl': 'https://www.rarlab.com/download.htm', 'isofficiallink': True,
                      'findmethod': "' '.join(soup.find(class_='headtbl').find('a').find('b').text.split()[4:])", 'ver': '',
                      'downurl': 'https://www.rarlab.com/download.htm'},
    'vlc':           {'packageid': 'AAA00013', 'checkurl': 'https://www.videolan.org/vlc/index.ru.html', 'isofficiallink': True,
                      'findmethod': "soup.find(id='downloadDetails').find(id='downloadVersion').text.strip()", 'ver': '',
                      'downurl': 'https://get.videolan.org/vlc/last/win64/'},
    'freecam':       {'packageid': 'AAA0003A', 'checkurl': 'https://www.ispring.ru/ispring-free-cam/thanks-for-download?said=1683793&type=static', 'isofficiallink': True,
                      'findmethod': "'.'.join(soup.find(id='downloadItemLink').get('href').split('/')[-1][-9:-4].split('_'))", 'ver': '',
                      'downurl': 'https://www.ispring.ru/ispring-free-cam'},
    'lightshot':     {'packageid': 'AAA00047', 'checkurl': 'https://community.chocolatey.org/packages/lightshot.install', 'isofficiallink': False,
                      'findmethod': "soup.find('title').text.split('|')[-1].split()[-1]", 'ver': '',
                      'downurl': 'https://app.prntscr.com/ru/download.html'},
    'paintnet':      {'packageid': 'AAA000BE', 'checkurl': 'https://github.com/paintdotnet/release/releases/latest', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='d-inline mr-3').text", 'ver': '',
                      'downurl': 'https://github.com/paintdotnet/release/releases'},
    'fsvrecorder':   {'packageid': 'AAA0004C', 'checkurl': 'https://www.dvdvideosoft.com/ru/products/dvd/Free-Screen-Video-Recorder.htm', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='spec_table_padding1 spec_table_content_1').text.split()[-1]", 'ver': '',
                      'downurl': 'https://www.dvdvideosoft.com/ru/products/dvd/Free-Screen-Video-Recorder.htm'},
    'itunes':        {'packageid': 'AAA00046', 'checkurl': 'https://community.chocolatey.org/packages/iTunes', 'isofficiallink': False,
                      'findmethod': "soup.find('title').text.split('|')[-1].split()[-1]", 'ver': '',
                      'downurl': 'https://www.apple.com/itunes/download/win64'},
    'joplin':        {'packageid': 'AAA0002E', 'checkurl': 'https://github.com/laurent22/joplin/releases/latest', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='d-inline mr-3').text[1:]", 'ver': '',
                      'downurl': 'https://github.com/laurent22/joplin/releases/latest'},
    'joxi':          {'packageid': 'AAA0003B', 'checkurl': 'https://softobase.com/ru/joxi', 'isofficiallink': False,
                      'findmethod': "soup.find(itemprop='softwareVersion').text.strip()", 'ver': '',
                      'downurl': 'http://joxi.ru/download/win'},
    'keepassxc':     {'packageid': 'AAA00044', 'checkurl': 'https://keepassxc.org/download/#windows', 'isofficiallink': True,
                      'findmethod': "soup.find(class_='label label-success').text[1:]", 'ver': '',
                      'downurl': 'https://keepassxc.org/download/#windows'}
}

# ====== defining functions ============================= #


def random_headers():
    return {'User-Agent': choice(desktop_agents), 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


def get_soup(app):
    checkurl = apps[app]['checkurl']
    print('checking:', checkurl, end='')
    if app == 'aimp':
        responce = requests.get(checkurl, headers=random_headers(), verify=False)
    else:
        responce = requests.get(checkurl, headers=random_headers())
    print(' - ok')
    return BeautifulSoup(responce.content, 'html.parser')


def write_csv(model, filename='output.csv'):
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=['PackageID', 'Name', 'VersionOnWeb', 'CheckUrl', 'IsOfficialLink', 'DownloadUrl'],
            delimiter=',',
            extrasaction='ignore',
            lineterminator='\r',
            quoting=csv.QUOTE_NONE,
        )
        writer.writeheader()
        for name, data in model.items():
            writer.writerow({'PackageID': data['packageid'], 'Name': name, 'VersionOnWeb': data['ver'],
                             'CheckUrl': data['checkurl'], 'IsOfficialLink': data['isofficiallink'], 'DownloadUrl': data['downurl']})
        print(fr'CSV stored in: {getcwd()}\{filename}')


def scrap(objects):
    for app in objects:
        try:
            soup = get_soup(app)
        except Exception as e:
            print(' - ', e)
            apps[app]['ver'] = 'failed'
        else:
            apps[app]['ver'] = eval(apps[app]['findmethod'])
        finally:
            print(f"{app}: {apps[app]['ver']}")


# ====== main code ====================================== #
if __name__ == '__main__':
    match argv:
        case program, :
            print("Supported single app keys: ")
            print(*[app for app in apps])
            print("For scrap all apps and export to CSV, use key: all")
        case program, app if app in apps:
            scrap([app])
        case program, 'all':
            scrap(apps)
            write_csv(apps)
        case program, any_other:
            print(f"Application '{any_other}' not supported")
