import requests as r
import os 

def isAvaliable(nick):
    status_codes = int(r.get(f'https://api.mojang.com/users/profiles/minecraft/{nick}').status_code)
    if status_codes == 200:
        return 'False'
    elif status_codes == 204:
        return 'True'
    else: return 'ERROR'

char = []

for i in range(97, 123):
    char.append(chr(i))

char.append('_')

# print(char)
with open('nicks.txt', 'a') as f:
    for i in char:
        for j in char:
            for n in char:
                nick = i+j+n
                if isAvaliable(nick) == 'True':
                    print(nick+' is', 'avaliable.')
                elif isAvaliable(nick) == 'False':
                    print(nick+' is', 'not avaliable.')
                elif isAvaliable(nick) == 'ERROR':
                    print(nick+':', 'Error.')
                f.write(nick+'\n')

