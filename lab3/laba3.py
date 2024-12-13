def wwod(filename, a):
    try:
        strs = ''
        if a == 'full':
            with open(filename, 'r', encoding='utf - 8') as file:
                contet = file.read()
            return contet
        elif a == 'str':
            with open(filename, 'r', encoding='utf - 8') as file2:
                for line in file2:
                    strs = strs + line
                return strs
        else:
            print('error:str or full')
    except FileNotFoundError:
        return f'error file {filename} not found'


print('выберете файл')
filename = input()
print('введите тип считывания')
a = input()
print(wwod(filename,a))

print('введите текст')
nt = input()
with open('text', 'a', encoding='utf - 8') as file:
    file.write('\n'+nt)
with open('text', 'r', encoding='utf-8') as file2:
    content = file2.read()
print(content)