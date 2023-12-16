import re

NUM_OR_DOR_REGEX = re.compile(r'^[0-9.]$')

# print(NUM_OR_DOR_REGEX.search('11'))

def numero_ou_ponto(string: str):
    return bool(NUM_OR_DOR_REGEX.search(string))

def vazio(string: str):
    return len(string) == 0
