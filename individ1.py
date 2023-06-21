#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Список работников.
    people = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о человеке.
            name = input("Фамилия, Имя:  ")
            number = input("Номер телефона:  ")
            birthday = input("Дата рождения: ")

            # Создать словарь.
            human = {
                'name': name,
                'number': number,
                'birthday': birthday,
            }

            # Добавить словарь в список.
            people.append(human)
            # Отсортировать список в случае необходимости.
            if len(people) > 1:
                people.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 7,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^7} | {:^30} | {:^20} | {:^20} |'.format(
                    "№",
                    "Фамилия, Имя",
                    "Номер телефона",
                    "Год рождения"
                )
            )

            print(line)

            # Вывести данные о всех людях.
            for idx, human in enumerate(people, 1):
                print(
                    '| {:>7} | {:<30} | {:<20} | {:<20} |'.format(
                        idx,
                        human.get('name', ''),
                        human.get('number', ''),
                        human.get('birthday', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):
            # Разбить команду на части для выделения Фамилии.
            parts = command.split(' ', maxsplit=1)
            # Получить требуемый стаж.
            month = parts[1]
            search_month = []

            # Проверить сведения работников из списка.
            for human in people:
                dr = human["birthday"].split(" ")[1].lower()
                if dr == month:
                    search_month.append(human)

            if len(search_month) > 0:
                line_new = '+-{}-+-{}-+-{}-+-{}-+'.format(
                    '-' * 7,
                    '-' * 30,
                    '-' * 20,
                    '-' * 20
                )
                print(line_new)

                print(
                    '| {:^7} | {:^30} | {:^20} | {:^20} | '.format(
                        "№",
                        "Фамилия, Имя",
                        "Номер телефона",
                        "Дата рождения"
                    )
                )
                print(line_new)

                for idx_new, spisok_new in enumerate(search_month, 1):
                    print(
                        '| {:>7} | {:<30} | {:<20} | {:<20} | '.format(
                            idx_new,
                            spisok_new.get('name', ''),
                            spisok_new.get('number', ''),
                            spisok_new.get('birthday', '')
                        )
                    )

                print(line_new)

            else:
                print("Работники с заданной датой не найдены.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("select <месяц> - запросить данные о человеке;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
