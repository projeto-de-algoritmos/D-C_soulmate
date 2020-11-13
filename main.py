from pyfiglet import Figlet
from clint.textui import puts, colored, indent
from inversion_counter import mergeSort
from data import personagens
import os


title = Figlet(font='slant')
print(colored.magenta(title.renderText('SOULMATE')))
print(colored.red('Bem vindo ao ' + colored.magenta('SOULMATE')  + colored.red(', o programa que vai achar sua alma gêmea da ficção!')))

print(colored.green('Digite qualquer tecla para continuar para continuar!'))
comecou = input()
os.system('cls' if os.name == 'nt' else 'clear')

string_ordem_inicial = '''
1 - Bondade
2 - Humor
3 - Lealdade
4 - Inteligencia
5 - Coragem
'''

stats = {1:'bondade', 2:'humor', 3:'lealdade', 4:'inteligencia', 5:'coragem'}

print(colored.yellow('Para jogar é muito facil! Você só precisa rankear o que você mais valoriza em uma pessoa de acordo com a relação abaixo:'))
print(colored.red(string_ordem_inicial))
print(colored.white('Os números devem ser inseridos na ') + colored.red('ordem')  + colored.white(' de o que você mais valoriza para o que você menos valoriza.'))
print(colored.green("Ex: 1,4,3,5,2"))

string_usuario = input(colored.magenta('Insira sua ordem com virgula:\n'))

lista_usuario = string_usuario.split(',')
lista_usuario = [int(x) for x in lista_usuario]

nova_ordem = {}
cont = 0
for i in lista_usuario:
    cont += 1
    nova_ordem[stats[i]] = cont

lista_personagem = []
lista_pontuacao = []

for personagem in personagens:
    lista_personagem.clear()
    for valores in personagem.values():
        for valor in valores:
            lista_personagem.append(nova_ordem[valor])
        lista_pontuacao.append(mergeSort(lista_personagem)[0])

os.system('cls' if os.name == 'nt' else 'clear')

result = Figlet(font='banner3-D')

p = lista_pontuacao.index(min(lista_pontuacao))
nome = list(personagens[p].keys())[0]
print(result.renderText('DEU MATCH !'))
print(colored.red(result.renderText(nome)))
print(colored.green(f'Parabéns, sua alma gêmea é o(a) {nome} !'))
