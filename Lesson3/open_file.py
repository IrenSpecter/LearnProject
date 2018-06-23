# with open('text.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(content)

# with open('text.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.upper()
#         line = line.replace('\n', '')
#         print(line

with open('referat.txt','r', encoding='utf-8') as referat:
    content = referat.read()
    print(content)
    count = 0
    gap = 0
    for i in range(len(content)):
        if content[i] != ' ' and gap == 0:
            count += 1
            gap = 1
        else:
            if content[i] == ' ':
                gap = 0
   
    print(count)