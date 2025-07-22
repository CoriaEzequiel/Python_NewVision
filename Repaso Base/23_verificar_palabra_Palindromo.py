'''
verificar si el string es palíndromo
'''

palabra = 'radar'

es_palin = palabra == palabra[::-1]

print("Es palíndromo", es_palin)