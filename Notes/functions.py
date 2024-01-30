import csv
from datetime import datetime

fields = ['ID', 'Title', 'Text', 'Creation Date']


def create_file():
    with open('notes.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

def read_file():
    with open('notes.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        notes = list(reader)
    return notes

def overwrite_file(notes):
    with open('notes.csv', "w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(notes)


def show_notes():
    with open('notes.csv', 'r',encoding='utf-8') as file:
        print(file.read())


def select_note():
    id = input("Введите номер интересующей вас заметки - ")
    with open('notes.csv', 'rt', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if id in row[0]:
                print(row[0], row[1], row[2], row[3])


def create_note():
    notes = read_file()
    id = len(notes) + 1
    title = input('Введите заголовок заметки: ')
    text = input('Введите текст: ')
    creation_date = datetime.now().date()
    with open('notes.csv', 'a', encoding='UTF8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writerow({'ID': id, 'Title': title, 'Text': text, 'Creation Date': creation_date})

def edit_note():
     id = input("Введите номер интересующей вас заметки - ")
     notes = read_file()
     for el in notes:
         if id == el['ID']:
             el['Title'] = input("Введите новый заголовок заметки: ")
             el['Text'] = input("Введите новый текст заметки:")
             el['Creation Date'] = datetime.now().date()
             overwrite_file(notes)
def delete_note():
    id = input("Введите номер заметки который вы хотите удалить: ")
    notes = read_file()
    for el in notes:
        if id == el['ID']:
            notes.remove(el)
            overwrite_file(notes)



