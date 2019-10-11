import requests
import os
from urllib import request
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
root=r'F:/untitled1/lol'
url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
def get_pic():
    response = requests.get(url=url,headers=headers).json()
    for a in response['hero']:
        path = a['name']
        if not os.path.exists(path):
            os.makedirs(path)
        id_number = a['heroId']
        muban_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/%s.js'
        detail_url = format(muban_url % id_number)
        response1 = requests.get(url=detail_url,headers=headers).json()
        for i in response1['skins']:
            if 'K/DA' in i['name']:
                i['name'] = i['name'].replace('K/DA','KDA')
            img_path = root + '/'+ path + '/' + i['name'] + '.jpg'
            if i['mainImg'] is '':
                continue
            request.urlretrieve(url=i['mainImg'],filename=img_path)
            # print(i['mainImg'])

        # break


get_pic()