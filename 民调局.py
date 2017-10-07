from bs4 import BeautifulSoup
import requests
body=requests.get('http://www.wddsnxn.org/mindiaojuyiwenlu/244.html')
# print(body.text)
body.encoding='utf-8'

def func(body):
    soup = BeautifulSoup(body.text, 'html.parser')
    h=soup.find_all('h1')[1]
    print(h.get_text())
	 
    print(h.get_text(),file=open('民调局.txt','a+'))
    firstChapter=soup.find( id="BookText")
    print(firstChapter.get_text(),file=open('民调局.txt','a+'))
    # file=open('file','w')

    # print(soup.find_all("a",{"span":"下一页(快捷键:→)"}))

    for line in soup.find_all("a"):

        if "下一页" in str(line) :
            url=str(line).split('"')[1]
            body = requests.get(url)
            body.encoding = 'utf-8'
            func(body)

func(body)