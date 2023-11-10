import re  #  Эта строка импортирует модуль регулярных выражений (re), который предоставляет функции для работы с шаблонами в строках.
def read_html_file(filename): # Эта строка определяет функцию с именем read_html_file, которая принимает параметр filename.
    with open(filename, 'r') as f:
        html_string = f.read() # Эта строка считывает содержимое объекта файла (f) и присваивает его переменной
    return html_string # Эта строка возвращает переменную html_string в качестве результата функции read_html_file.
def parse_all_emails(html_string): #  Эта строка определяет функцию с именем parse_all_emails, которая принимает параметр html_string.
    pattern =  r'<a href="(.*?)">.*?</a>' # Эта строка определяет шаблон регулярного выражения.
    return re.findall(pattern, html_string) # Эта строка использует функцию re.findall для поиска всех соответствий шаблону в html_string. Она возвращает список всех найденных строк.

html_string = read_html_file('test.html') #Эта строка вызывает функцию read_html_file с именем файла 'test.html' и присваивает возвращенное содержимое HTML переменной html_string.
print(parse_all_emails(html_string)) #Эта строка вызывает функцию parse_all_emails с переменной html_string и выводит результат, который представляет собой список всех найденных адресов электронной почты в HTML-содержимом.
