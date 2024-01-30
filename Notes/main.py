import os
import functions


if os.path.exists('notes.csv'):
    print("Добро пожаловать!")
else:
    functions.create_file()
    print("Исходный файл создан. Добро пожаловать.")

print('\nГлавное меню '
      '\n1. Список всех заметок '
      '\n2. Выбрать заметку '
      '\n3. Добавить заметку '
      '\n4. Редактировать заметку '
      '\n5. Удалить заметку '
      '\n6. Выход')

menu_input = input()

if menu_input == '1':
    functions.show_notes()
elif menu_input == '2':
    functions.select_note()
elif menu_input == '3':
    functions.create_note()
elif menu_input == '4':
     functions.edit_note()
elif menu_input == '5':
     functions.delete_note()
elif menu_input == '6':
     print("До свидания!")

