"""
crawler study code 

Author: smilexie1113@gmail.com

"""
import requests
from bs4 import BeautifulSoup

class ZhihuInspect(object):
    header = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Host': 'www.zhihu.com',
        'DNT': '1'
    }
    url = r"http://www.zhihu.com/"
    id = r"xxxxx"
    password = r"xxxxx"
    
    def __init__(self):
        pass
    
    def save_file(self, path, str):
        with open(path, 'w') as fp:
            fp.write(str)
    
    def get_xsrf(self):
        response = requests.get(self.url, headers = self.header)
        text = response.text
        save_file("1.htm", text)
        soup = BeautifulSoup(text);
        input_tag = soup.find("input", {"name": "_xsrf"})
        xsrf = input_tag["value"]
        return xsrf
        
    def get_login_page(self, xsrf):
        login_url = self.url + r"login"
        post_dict = {
            'rememberme': 'y',
            'password': self.password,
            'email': self.id,
            '_xsrf':xsrf    
        }
        reponse_login = requests.post(login_url, headers = self.header, data = post_dict)
        save_file('2.htm', reponse_login.text)
    
if __name__ == "__main__":
    z = ZhihuInspect()
    xsrf = z.get_xsrf()
    z.get_login_page(xsrf)
    
    