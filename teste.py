#recebe input de usuario
print("Bem vindo a o hortti sabor!")
nome = input("Diga o seu nome por favor:")
print()
endere = input(f"{nome}, Digite seu endereço por favor:")
print()
nasc = int(input(f"{nome}, Digite o ano em que voce  nasceu:"))
print()
calc = (nasc - 2024)
print(f"Voce tem {calc} anos de idade.")
print()

#descriçao das frutas do dia
uva = 10.50
morango = 20.10
melancia = 15.40
banana = 2.75
maca = 4.50
print(f"{nome}, As frutas do dia são as seguintes:")

print('''
-----frutas ------ preço-----

-----uva ---------- 10.50----
-----morango ------- 20.10---
-----melancia ------ 15.40---
-----banana -------- 2.75----
-----maca ---------- 4.50----
''')
print("escolha o numero da frura que gostaria:")