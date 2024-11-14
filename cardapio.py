nome = input("Digite seu nome: ")

doce1 = "Torta"
doce2 = "Banofe"
doce3 = "Pudim"

print(doce1, doce2, doce3)

escolha = input(f"{nome} escolha uma das opções acima: ")

if escolha == doce1:
    print(f"Ótima escolha! o valor é:", 15.0)

elif escolha == doce2:
    print(f"Ótima escolha! o valor é:", 20.0)

elif escolha == doce3:
    print(f"Ótima escolha! o valor é:", 25.0)

else:
    print("Escolha uma opção válida!")


opcao1 = "pix"
opcao2 = "debito"
opcao3 = "credito"
pagamento = input(f"Qual será o tipo de pagamento? Aceitamos {opcao1}, {opcao2} e {opcao3}: ")

if pagamento == opcao1:
    print("Pagamento realizado com sucesso")

elif pagamento == opcao2:
    print("Pagamento realizado com sucesso")

elif pagamento == opcao3:
    print("Pagamento realizado com sucesso")
else:
    print("Escolha uma forma de pagamento correta!")