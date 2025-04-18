import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

ans = []
tt = []
text = []
main_title = []

titles_f = []
for i in range(10):
    url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'

    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    tt = []
    t = soup.find_all("h2")
    s = ""
    for i in t:
        a = i.get_text()
        if a != "" and a != "\n":
            s = a
            s = s.replace(u'\xa0', u' ')
            s = s.replace(u'\n', u' ')
            s = s.replace(u'[править | править код]', u' ')
            tt.append(s)
    titles_f.append(tt)
    
    
    t = soup.find_all("p")
    s = ""
    for i in t:
        a = i.get_text()
        if a != "" and a != "\n":
            s += a
    s = s.replace(u'\xa0', u' ')
    s = s.replace(u'\n', u' ')
    text.append(s)
    

    
    t = soup.find_all("h1")
    s = ""
    for i in t:
        a = i.get_text()
        if a != "" and a != "\n":
            s += a
    s = s.replace(u'\xa0', u' ')
    s = s.replace(u'\n', u' ')
    main_title.append(s)
    

    cat = []
    t = soup.find_all(class_='mw-normal-catlinks')
    s = ""
    for i in t:
        a = i.get_text()
        s = a
        s = s.replace(u'\xa0', u' ')
        s = s.replace(u'\n', u' ')
        s = s[11::]
        cat.append(s)


    
    s = ""
    prev = ""
    c = 0
    flag = True
    if len(cat) > 0:
        for i in cat[0]:
            if prev.isupper():
                c += 1
            else:
                c = 0
            if prev == "X" or prev == "V" or prev == "I" or prev == "А":
                c += 1
            if i.isupper() and prev.isalpha() and (not(prev.isupper()) and c < 3):
                if len(s)!= 0:
                    ans.append(s)
                    flag = False
                    break
                    
                s = i
            else:
                s += i
            prev = i
        if flag:
            ans.append(s)
    
    


print(main_title)       
print(text)
print(ans)

print(titles_f)


    
import sqlite3



conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS articles (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  titles TEXT,
                  text TEXT,
                  cat_id INTEGER,
                  FOREIGN KEY (cat_id) REFERENCES categories(id)
              )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
                  id INTEGER PRIMARY KEY,
                  category_name TEXT
              )''')


import json
from tabulate import tabulate
conn = sqlite3.connect('mydatabase.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cursor = conn.cursor()


for i in ans:
    cursor.execute("INSERT INTO categories (category_name) VALUES (?)", (i,))


cat_id = []
for i in ans:
    category_name = i
    cursor.execute("SELECT id FROM categories WHERE category_name=?", (category_name,))
    result = cursor.fetchone()

    if result:
        cat_id.append(result[0])

for i in range(10):
    name = main_title[i]
    t =json.dumps(titles_f[i], ensure_ascii=False).encode('utf-8')
    tex = text[i]
    c = cat_id[i]
    cursor.execute("INSERT INTO articles (name, titles, text, cat_id) VALUES (?, ?, ?, ?)", (name, t, tex, c))



def wrap_text(text, width):
    # Разбиваем текст на строки, учитывая максимальную ширину
    wrapped_lines = []
    current_line = ''
    for word in text.split():
        if len(current_line) + len(word) <= width:
            current_line += word + ' '
        else:
            wrapped_lines.append(current_line)
            current_line = word + ' '
    wrapped_lines.append(current_line)
    
    return '\n'.join(wrapped_lines)




conn.commit()

cursor.execute("SELECT * FROM categories")
categories = cursor.fetchall()
print("Таблица 'categories':")
for category in categories:
    print(category)

cursor.execute("SELECT * FROM articles")


rows = cursor.fetchall()


headers = ["ID", "Name", "Titles", "Text", "Cat_id"]

table_data = []
i = 0
for row in rows:
    id, name, titles, text, cat_id = row
    my_list = json.loads(titles.decode('utf-8'))

    w = wrap_text(text, 100)
    table_data.append([id, name, my_list, w, cat_id])

print(tabulate(table_data, headers, tablefmt="grid"))

conn.close()
    
    

import sqlite3
import PySimpleGUI as sg

# Создаем соединение с базой данных
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Определение макета GUI
layout = [
    [sg.Text('Имя:'), sg.InputText(key='name')],
    [sg.Text('Заголовки:'), sg.InputText(key='titles')],
    [sg.Text('Текст:'), sg.InputText(key='text')],
    [sg.Button('Добавить запись'), sg.Button('Изменить запись'), sg.Button('Удалить запись')],
    [sg.Text('Поиск по имени:'), sg.InputText(key='search_name'), sg.Button('Поиск')],
    [sg.Table(values=[], headings=['ID', 'Имя', 'Заголовки', 'Текст'], auto_size_columns=False, display_row_numbers=False,
              justification='right', num_rows=20, key='table')],
    [sg.Button('Выход')]
]

# Создаем окно
window = sg.Window('Управление базой данных', layout)

# Функция для обновления данных в таблице
def update_table():
    cursor.execute("SELECT id, name, titles, text FROM articles")
    data = cursor.fetchall()
    window['table'].update(values=data)

# Главный цикл приложения
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Выход'):
        break
    elif event == 'Добавить запись':
        name = values['name']
        titles = values['titles']
        text = values['text']
        cursor.execute("INSERT INTO articles (name, titles, text) VALUES (?, ?, ?)", (name, titles, text))
        conn.commit()
        update_table()
    elif event == 'Изменить запись':
        selected_row = window['table'].get()
        if selected_row:
            name = values['name']
            titles = values['titles']
            text = values['text']
            article_id = selected_row[0]
            cursor.execute("UPDATE articles SET name=?, titles=?, text=? WHERE id=?", (name, titles, text, article_id))
            conn.commit()
            update_table()
    elif event == 'Удалить запись':
        selected_row = window['table'].get()
        if selected_row:
            article_id = selected_row[0]
            cursor.execute("DELETE FROM articles WHERE id=?", (article_id,))
            conn.commit()
            update_table()
    elif event == 'Поиск':
        search_name = values['search_name']
        cursor.execute("SELECT id, name, titles, text FROM articles WHERE name LIKE ?", ('%' + search_name + '%',))
        data = cursor.fetchall()
        window['table'].update(values=data)

update_table()
window.close()
