from html.parser import HTMLParser
import os
import requests

# класс уникальной ошибки 
class stop_parse(Exception):
    def __init__(self, text):
        self.txt = text

# класс, который парсит страницы 
class text_parser(HTMLParser):
    
    # флаг, что бы понять, когда начался текст
    flag = False
    
    # флаг на парсинг картинок
    images = True
    
    # метод, который 
    def handle_starttag(self, tag, attrs):
        
        # здесь текст начинается. Ставим флажок
        if ('class', 'reader-container container container_center') in attrs:
            self.flag = True
        
        # если в тектсе попалась картинка
        if self.flag and self.images and tag == "img":
            download_file(attrs[2][1])
        
    def handle_data(self, data):
        
        if "Реклама" in data: # прекращаем парс на словах
            raise stop_parse(" parsed!")
            
        if self.flag: # парсим текст
            
            data = data.replace('\n', ' ') # чистим текст
            write_text(data)
            

# cкачать html страницы
def download_page(url):

    request = requests.get(url, headers = {"User-Agent": "M"})
    text = request.text
    
    return text

# скачать файл и записать его
def download_file(url):
    
    request = requests.get(url, allow_redirects=True)

    filename = os.path.basename(url)

    file = open(filename, 'wb')
    file.write(request.content)
    
    file.close()

# записываем текст из главы в файл
def write_text(text):

    file = open("text.txt", "a", encoding = "utf-8")
    file.write(text + "\n\n")
    
    file.close()
    
# создаём файлы и папки нужные для работы
def setup():
    
    # если не существует root файла
    if not os.path.exists('charapters/root'): 
    
        os.mkdir('charapters')
        open('charapters/root', 'a').close()    
    
    os.chdir('charapters')
    
# меняем текущую дерикторю на дерикторию другой главы
def change_dir(charapter):

    if 'root' not in os.listdir(): 
        os.chdir('..')
        
    if os.path.exists(charapter):
        raise stop_parse(" was alredy parsed")
        
    os.mkdir(charapter)
    os.chdir(charapter)
    
    
