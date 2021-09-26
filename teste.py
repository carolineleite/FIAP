alimento_ingerido = ""
qtd_alimentos = 0
calorias_alimento = 0
qtd_calorias_ingeridas = 0
qtd_alimentos_ingeridos = 0
adicionar = ""

while adicionar != "NÃO":
    alimento_ingerido = input("Qual alimento voce consumiu? ")
    qtd_alimentos = int(input("Quantidade consumida? "))
    calorias_alimento = int(input("Quantas calorias tem esse alimento? "))
    qtd_alimentos_ingeridos = int(qtd_alimentos_ingeridos) + int(qtd_alimentos)
    qtd_calorias_ingeridas = int(qtd_calorias_ingeridas) + int(qtd_alimentos) * int(calorias_alimento)
    adicionar = input("Gostaria de adicionar mais alimentos? 'Sim' ou 'Não' ").upper()

print("Voce consumiu {} alimentos com um total de {} Kcal.".format(qtd_alimentos_ingeridos, qtd_calorias_ingeridas))
