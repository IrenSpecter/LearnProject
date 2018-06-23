def which_more(line1,line2):
    if line1==line2:
        return 1
    elif len(line1) > len(line2):
            return 2
    elif line2=='learn':
            return 3


line1=input('строка1: ')
line2=input('строка2: ')            
print(which_more(line1, line2))4