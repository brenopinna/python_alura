endereco = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120'


import re # Regular Expression -- RegEx

# cep -- > 5 dígitos + - (opcional) + 3 dígitos
                         # ? é o caractere opcional     0,1 é que pode aparecer 0 ou 1 vez
padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)