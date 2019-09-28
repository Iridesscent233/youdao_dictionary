from bs4 import BeautifulSoup
import requests
import re

def crawler(url):
    word = input("Please input word that you want to know:\n")
    url = url + word
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html,'html.parser')
    initial_soup = soup.find_all(class_ = 'trans-container')
    for i in range(len(initial_soup)):
        translation = initial_soup[i].get_text()
        translation = translation.strip()
        translation = re.sub('[\r\n\ \f\t";"|"","]{2,}','\n',translation)
        print(translation)
        with open('result.txt','a',encoding='utf-8') as f:
            f.write(str(translation))
            f.write("="*20)
            f.close()
        print('='*20)

if __name__=='__main__':
    while True:
        crawler('http://dict.youdao.com/w/')
        press = input("Input q to quit it\n")
        if press=='q':
            break;
        else:
            continue;
