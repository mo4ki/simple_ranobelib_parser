
# simple_ranobelib_parser
Простой парсер ранобе. Некоторые вещи прийдётся делать руками, но в остальном он работает сам

# ДИСКлеймер
Ну и конечно за все ваши действия вы ответственны сами. Стоит понимать, что если сами создатели **`ranobelib.com`** не предусмотрели функцию скачивания глав, то на то была причина. Так что все последствия от ваших действий будут ложится только на ваши плечи.  

# Установка
Для работы скрипта потребуется библиотека **`requests`** . Установить её можно через **`pip`**:

 - `pip intall requests`

В остальном остаётся только скачать и запустить **`main.py`**

# Настройки
Настройки скрипта находятся в **`configs.py`**
там вы можете настроить:

 - **`root`** - ссылка на ваше ронобэ, главы которого вы хотите спарсить
 - **`images`** - флаг, который указывает, собираетесь ли вы парсить и картинки в довесок. С картинками чаще всего процесс парсинга будет дольше и итоговая папка **charapters** будет больше. Если вы будете парсить картинки то оставляйте **True**, иначе ставьте **False**
 - **`translate`** - вариант перевода, который вы собираетесь читать (его можно получить из ссылки, когда вы выбрали перевод)
 - **`charapters`** - список глав формата **["v1/c0.1"]**, где **V** - том, а **C** - глава, которую вы  собираетесь парсить. 

# Работа скрипта
Скрипт выведет страницу ронобэ, указанную в настройках и начнёт парсить. По мере этого, главы, которые уже спарсил, он так же будет выводить на экран.

После того, как скрипт отработает вы сможете увидеть главы в папке **`charapters`** 

## Возможные улучшения
За время написания скрипта я не нашёл возможных улучшений производительности, за исключением одного. Запросы на **`ranobelib.com`** идут долго, я уверен, что их можно оптимизировать нормальной библиотекой для запросов, используя вместо **`requests`** что-то другое. Но ради простоы проекта я оставил всё так, как оно есть. Однако проект построен таким образом, что поменять библиотеку будет не самой сложной задачей и если кто-то захочет этим заняться, то флаг ему в руки.

Из важного стоит подметить, что удобство не на высоком уровне. Те же картинки не появляются в тексте, а просто находятся в папке с нми.
Я решил этого не делать, но если кто-то захочет засунуть весь текст в pdf, html или docx, то я только за. Ведь картинки в тексте - это то, что я хотел изначально. Так же если вы реализуете pdf, html или docx, то вы сможете настроить красивый шрифт и его размер, что позволит сконцентрироваться на чтении.

Уверен есть ещё множество разных улучшений, которые я не заметил, так что жду фидбэка.

## Важно!
после работы скрипта либо полностью удалите/перенесите папку **`charapters`**,  либо не избавляйтесь от файла **`root`**. Скрипт не будет работать корректно этого файла. 

Если файл был удалён/перенесён, но не была перенесена/удалена вся папка, то ничего сильно страшного не случилось. Тут есть 2 варианта исправления поломки, возникающей при запуске скрипта:

 - Просто-напросто удалите/перенесите всю папку **`charapters`**
 - Создайте файл **`root`**. Он может быть пусты и без расширения, так и должно быть
