import json
from datetime import datetime


def get_data():
    """
    Функция для получения данных
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data, filtred_empty_from):
    """
    Функция для фильтрации данных по параметру EXECUTED
    """
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    if filtred_empty_from:
        data = [x for x in data if 'from' in x]
    return data


def get_last_values(data, count_values):
    """
    Функция для сортировки данных по дате в обратном порядке в количестве count_values
    """
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:count_values]


def get_formated_data(data):
    """
    Функция для формирования вывода в необходимом виде
    """
    formated_data = []

    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = row['description']
        if 'from' in row:
            sender = row['from'].split()
            from_bill = sender.pop(-1)
            from_bill = f'{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}'
            from_info = ' '.join(sender)
        else:
            from_info, from_bill = 'Счет не указан', ''

        recipient = row['to'].split()
        recipient_bill = recipient.pop(-1)
        recipient_bill = f'**{recipient_bill[-4:]}'
        to_info = ' '.join(recipient)
        amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"

        formated_data.append(f"""
{date} {description}
{from_info} {from_bill} -> {to_info} {recipient_bill}
{amount}""")

    return formated_data
