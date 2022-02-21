import requests
from bs4 import BeautifulSoup
import csv

apps = {'chrome'       :{'packageid':'AAA00014', 'checkurl':'https://omahaproxy.appspot.com/win', 'isofficiallink': True, 'ver':'',
                         'downurl': 'https://chromeenterprise.google/browser/download/thank-you/?platform=WIN64_MSI&channel=stable&usagestats=0'},
        'edge'         :{'packageid':'AAA00025', 'checkurl':'https://www.microsoft.com/ru-ru/edge/business/download','isofficiallink': True,'ver':'',
                         'downurl': 'https://msedge.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/6a6c1d52-db7d-4a6f-9acb-8bde082025ed/MicrosoftEdgeEnterpriseX64.msi'},
        'yandex'       :{'packageid':'AAA00022', 'checkurl':'https://browser.yandex.ru/constructor/','isofficiallink': True,'ver':'',
                         'downurl': 'https://browser.yandex.ru/constructor/build/2bbda80e-1d48-4c3c-99a0-3dce6f25edd8/'},
        'firefox'      :{'packageid':'AAA000BA', 'checkurl':'https://www.mozilla.org/en-US/firefox/releases/','isofficiallink': True,'ver':'',
                         'downurl': 'https://www.mozilla.org/ru/firefox/enterprise/#download'},
        'reader'       :{'packageid':'AAA00012', 'checkurl':'https://www.adobe.com/devnet-docs/acrobatetk/tools/ReleaseNotesDC/index.html','isofficiallink': True,'ver':'',
                         'downurl': 'https://www.adobe.com/devnet-docs/acrobatetk/tools/ReleaseNotesDC/index.html'},
        'xmind'        :{'packageid':'AAA00071', 'checkurl':'https://www.xmind.net/download/previous/','isofficiallink': True,'ver':'',
                         'downurl': 'https://www.xmind.net/download/xmind8'},
        'java'         :{'packageid':'AAA00016', 'checkurl':'https://www.oracle.com/java/technologies/','isofficiallink': True,'ver':'',
                         'downurl': 'https://java.com/ru/download/manual.jsp'},
        'far'          :{'packageid':'AAA0000B', 'checkurl':'https://www.farmanager.com/download.php?l=ru','isofficiallink': True,'ver':'',
                         'downurl': 'https://www.farmanager.com/download.php?l=ru'},
        'powerbi'      :{'packageid':'AAA000B8', 'checkurl':'https://www.microsoft.com/ru-RU/download/details.aspx?id=58494','isofficiallink': True,'ver':'',
                         'downurl': 'https://www.microsoft.com/ru-ru/download/confirmation.aspx?id=58494'},
        'notepad'      :{'packageid':'AAA00070', 'checkurl':'https://notepad-plus-plus.org/downloads/','isofficiallink': True,'ver':'',
                         'downurl': 'https://notepad-plus-plus.org/downloads/'},
        'bitrix'       :{'packageid':'AAA0001E', 'checkurl':'https://bitrix24.ru.malavida.com/windows/#gref','isofficiallink': False,'ver':'',
                         'downurl': 'https://www.bitrix24.ru/features/desktop.php'},
        'microsip'     :{'packageid':'AAA0006F', 'checkurl':'https://www.microsip.org/downloads','isofficiallink': True,'ver':'',
                         'downurl': 'https://www.microsip.org/downloads'},
        'skype'        :{'packageid':'AAA00042', 'checkurl':'https://www.techspot.com/downloads/50-skype.html','isofficiallink': False,'ver':'',
                         'downurl': 'https://go.skype.com/windows.desktop.download'},
        'openshell'    :{'packageid':'AAA00023', 'checkurl':'https://github.com/Open-Shell/Open-Shell-Menu/tags','isofficiallink': True,'ver':'',
                         'downurl': 'https://github.com/Open-Shell/Open-Shell-Menu/releases'},
        'aimp'         :{'packageid':'AAA0008A', 'checkurl':'https://www.aimp.ru/?do=download&os=windows','isofficiallink': True,'ver':'',
                         'downurl': 'https://www.aimp.ru/?do=download&os=windows'},
        'freecommander':{'packageid':'AAA00062', 'checkurl':'https://freecommander.com/ru/%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8/','isofficiallink': True,'ver':'',
                         'downurl': 'https://freecommander.com/ru/%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8/'},
        'rdm'          :{'packageid':'AAA000B9', 'checkurl':'https://remotedesktopmanager.com/home/downloadenterprise','isofficiallink': True,'ver':'',
                         'downurl': 'https://remotedesktopmanager.com/home/downloadenterprise'},
        '7zip'         :{'packageid':'AAA00017', 'checkurl':'https://www.7-zip.org/','isofficiallink': True,'ver':'',
                         'downurl': 'https://www.7-zip.org/'},
        'winrar'       :{'packageid':'AAA00027', 'checkurl':'https://www.rarlab.com/download.htm','isofficiallink': True,'ver':'',
                         'downurl': 'https://www.rarlab.com/download.htm'},
        'vlc'          :{'packageid':'AAA00013', 'checkurl':'https://www.videolan.org/vlc/index.ru.html','isofficiallink': True,'ver':'',
                         'downurl': 'https://get.videolan.org/vlc/last/win64/'},
        'freecam'      :{'packageid':'AAA0003A', 'checkurl':'https://www.ispring.ru/ispring-free-cam/thanks-for-download?said=1683793&type=static','isofficiallink': True,'ver':'',
                         'downurl': 'https://www.ispring.ru/ispring-free-cam'},
        'lightshot'    :{'packageid':'AAA00047', 'checkurl':'https://community.chocolatey.org/packages/lightshot.install','isofficiallink': False,'ver':'',
                         'downurl': 'https://app.prntscr.com/ru/download.html'},
        'paintnet'     :{'packageid':'AAA000BE', 'checkurl':'https://github.com/paintdotnet/release/releases/latest','isofficiallink': True,'ver':'',
                         'downurl': 'https://github.com/paintdotnet/release/releases'},
        'fsvrecorder'  :{'packageid':'AAA0004C', 'checkurl':'https://www.dvdvideosoft.com/ru/products/dvd/Free-Screen-Video-Recorder.htm','isofficiallink': True,'ver':'',
                         'downurl': 'https://www.dvdvideosoft.com/ru/products/dvd/Free-Screen-Video-Recorder.htm'},
        'itunes'       :{'packageid':'AAA00046', 'checkurl':'https://community.chocolatey.org/packages/iTunes','isofficiallink': False,'ver':'',
                         'downurl': 'https://www.apple.com/itunes/download/win64'},
        'joplin'       :{'packageid':'AAA0002E', 'checkurl':'https://github.com/laurent22/joplin/releases/latest','isofficiallink': True,'ver':'',
                         'downurl': 'https://github.com/laurent22/joplin/releases/latest'},
        'joxi'         :{'packageid':'AAA0003B', 'checkurl':'https://softobase.com/ru/joxi','isofficiallink': False,'ver':'',
                         'downurl': 'http://joxi.ru/download/win'},
        'keepassxc'    :{'packageid':'AAA00044', 'checkurl':'https://keepassxc.org/download/#windows','isofficiallink': True,'ver':'',
                         'downurl': 'https://keepassxc.org/download/#windows'}
        }

def get_soup(checkurl):
    '''getting soup, if requests failed - returns None'''
    print('checking:', checkurl, end='')
    responce = requests.get(checkurl)
    print(' - ok')
    return BeautifulSoup(responce.content, 'html.parser')

def write_csv(dict, filename='output.csv'):
    '''at the end - writes data to csv'''
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames = ['PackageID', 'Name', 'VersionOnWeb', 'CheckUrl', 'IsOfficialLink', 'DownloadUrl'],
            delimiter = ',',
            extrasaction='ignore',
            lineterminator='\r',
            escapechar=' ',
            quoting=csv.QUOTE_NONE
            )

        writer.writeheader()
        for name, data in dict.items():
            writer.writerow({'PackageID': data['packageid'], 'Name': name, 'VersionOnWeb': data['ver'],
                             'CheckUrl': data['checkurl'], 'IsOfficialLink': data['isofficiallink'], 'DownloadUrl': data['downurl'] })


def scrapper():
    for app in apps:
        try:
            soup = get_soup(apps[app]['checkurl'])
        except Exception as e:
            print(' - ', e)
            continue
        if app == 'chrome':
            version = str(soup)
        if app == 'edge':
            version = soup.find(class_='m-product-placement-item f-size-large').find(class_='build-version').text[1:-1]
        if app == 'yandex':
            version = soup.find(class_='lc-styled-text__text lc-styled-text__text_align_initial').text.split()[-1]
        if app == 'firefox':
            version = soup.find(class_='c-release-list').find('li').find('a').text
        if app == 'reader':
            version = soup.find(class_='std std-ref').text.split()[0]
        if app == 'xmind':
            version = soup.find(class_='container clearfix').find('p').text.split()[7][1:-2]
        if app == 'java':
            version = soup.find(href='/java/technologies/downloads/#java8').text.split()[-1]
        if app == 'far':
            tag = soup.find('b').text.split()
            version = tag[2][1:] + '.' + tag[4]
        if app == 'powerbi':
            version = soup.find(class_='fileinfo').find('p').text
        if app == 'notepad':
            version = soup.find(class_='patterns-list').find('a').text.split()[1]
        if app == 'bitrix':
            version = soup.find(class_='ver').text
        if app == 'microsip':
            version = soup.find(class_='box-inner').find('a').text.split('-')[-1][:-4]
        if app == 'skype':
            version = soup.find(itemprop='softwareVersion').text
        if app == 'openshell':
            version = soup.find(class_='Box-row position-relative d-flex').find('a').text.strip()
        if app == 'aimp':
            version = '.'.join(soup.find(class_='button_download_text').text.split()[::2])[1:]
        if app == 'freecommander':
            version = ' '.join(soup.find(class_='entry-content').find('span').text.split()[2:-2])
        if app == 'rdm':
            version = soup.find(class_='compare-editions-right').find(class_='compare-editions-link').text.split()[1]
        if app == '7zip':
            version = soup.find(class_='NewsTitle').text.split()[-1]
        if app == 'winrar':
            version = soup.find(class_='headtbl').find('a').find('b').text.split()[-1]
        if app == 'vlc':
            version = soup.find(id='downloadDetails').find(id='downloadVersion').text.strip()
        if app == 'freecam':
            version = '.'.join(soup.find(id='downloadItemLink').get('href').split('/')[-1][-9:-4].split('_'))
        if app == 'lightshot':
            version = soup.find('title').text.split('|')[-1].split()[-1]
        if app == 'paintnet':
            version = soup.find(class_='d-inline mr-3').text
        if app == 'fsvrecorder':
            version = soup.find(class_='spec_table_padding1 spec_table_content_1').text.split()[-1]
        if app == 'itunes':
            version = soup.find('title').text.split('|')[-1].split()[-1]
        if app == 'joplin':
            version = soup.find(class_='d-inline mr-3').text[1:]
        if app == 'joxi':
            version = soup.find(itemprop='softwareVersion').text.strip()
        if app == 'keepassxc':
            version = soup.find(class_='label label-success').text[1:]
        apps[app]['ver'] = version


if __name__ == '__main__':
    scrapper()
    write_csv(apps)
    print('done')