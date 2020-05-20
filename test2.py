

import requests
import re

def parse_url(url):
    headers = {
    # ':authority':'music.163.com',
    # ':method':'GET',
    # ':path':'/playlist?id=3037568471',
    # ':scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9',
    'cookie':'iuqxldmzr_=32; _ntes_nnid=fe37c602d0968b674655bc5776aa84c3,1579053678156; _ntes_nuid=fe37c602d0968b674655bc5776aa84c3; WM_TID=AP8GlcpVD85EBAQQBEZsqokovbtENsoF; ntes_kaola_ad=1; __remember_me=true; JSESSIONID-WYYY=f3aTset3%2BwjlMtYhwJ803J%2FDxvQkQrqOa3O0UeOPZxflRQsSjUAgY66EVCqtP%2Fnabpm5ksd35viUzpZ5jIJzOFc4y185pHcQf3MXXbKpSRS28J8qgAw31fHRHwdD7wSu6pPjnu4%2BW%5CAu92R0xmeTr4%5CnnXXM0TQaYe1me%5C62XTri22Gn%3A1581992571277; WM_NI=si44q6WYJ4pJuuj9SfjguCe9Y3K58HjttSszg8OakDxjm%2FKihekY1bJUcxd9TKhdCvT98yK1DwaD2VqUpY62Rsuw9djQZXmFZKuTPp%2B%2B2eZXZza4gCbPpFpFLx%2FHSs5FN20%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee88e467f58cbe95c83b8d9e8aa3c45b879b9aaef55e9892a6ccaa7b8691a1acae2af0fea7c3b92ab1b7fcd5f43e958786d5f342b7aba6dad26eaab9bba4e8339bed85d6bb44aaacbcb4f272a5e88182ea50bcb6a3d0ca63acbba5bab46a8a8bad99e7339895a885c27e98e7f89aca3b88a9afa5b15eb38bc0bab53a92adbb98bc70aa8f96b9f04e9a95bbb5d37ce9f5fe86d9549aa6afd5e649a290c0a7f34e90a8e1a9d279f79a82d3b337e2a3; MUSIC_U=e15eb88d8e4624f72ecf18bd8ef249dace6dcd65ddb5495e1756258dc646c48615d458450d7f037a4d5f434be6a0fe2241049cea1c6bb9b6; __csrf=a23761afe1ae85d1fcda6715d1816acc',
    'referer':'https://music.163.com/',
    'sec-fetch-dest':'iframe',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'upgrade-insecure-requests':'1',

    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return  response.text
# 获取歌单里的数据
def getlist(data):
    pattern = re.compile(r'li.*?song.id=(\d+).>(.*?)</a>',re.S)
    items = re.findall(pattern, data)
    for item in items:
        # http://music.163.com/song/media/outer/url?id=421137559.mp3
        mp3url = 'http://music.163.com/song/media/outer/url?id=' + item[0] + '.mp3'
        name = item[1]+'.mp3'
        print(mp3url)
        data = parse_data(mp3url)
        save_mp3(data,name)


def parse_data(url):
    headers={
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 78.0.3904.97Safari / 537.36'
    }
    response = requests.get(url,headers=headers)
    return response.content

def save_mp3(data,name):
    with open(name,'wb') as f:
        f.write(data)
        f.close()

def main():
    # 输入网易云的id号
    id = '2086826215'
    url = 'https://music.163.com/playlist?id='+id
    data = parse_url(url)
    getlist(data)

main()