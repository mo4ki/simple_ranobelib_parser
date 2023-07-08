# * - потому что нам нужно всё (плохая практика, не делайте так, прошу)
from utils import * 
from configs import *

# создаём папки и файлы, нужные для работы
setup()

print('url: ' + root + '\n\n')

# парсим главы
for non_changed_charapter in charapters:

    try:
    
        print('parsing...    ', end = '')
        
        # заменяем / на -, т.к / нельзя использовать в названии папки
        charapter = non_changed_charapter.replace("/","-")
        
        # меняем рабочую дерикторию
        change_dir(charapter) 
        
        # генерируем url главы, которую парсим
        url = root + non_changed_charapter + translate
        html = download_page(url)
        
        #парсим
        parser = text_parser()
        parser.images = images
        parser.feed(html)
        
    except stop_parse as e:
        print(charapter + '    ' + str(e))
        
    except Exception as e:
        print(e)
        
    except KeyboardInterrupt:
        print('\n зачем прерывать процесс?')
        exit()
