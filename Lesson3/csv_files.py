import csv
with open('users.csv', 'r', encoding='utf-8') as f:
    fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
    reader = csv.DictReader(f, fields, delimeter=';') # умеет читать файл в формате с разделителями, читает каждый файл построчно
    money_total = 0
    for row in reader:
        money_total += float(row['balance'])
    print(row)

# сохрарнение в файл, используем csv.DictWriter
import csv
with open('export.csv', 'w', encoding='utf-8') as f:
    fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
    writer = csv.DictWriter(f, fields, delimeter=',')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)