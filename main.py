import dados
print ('''0 - imprime os percentuais de partipantes do genero Feminino / Masculino;
1 - linha: Imprime os percentuais de participantes do genero Feminino / Masculino;
    Linha: % de jovens, adultos, idosos;
    Linha: % de quem tomou vacina e % de placebo;
    Linha: % de quem contraiu covid e de quem não contraiu covid;
2 - A % de eficácia geral da vacina.
3 - A % de eficácia por linha considerando os jovens, adultos e idosos
4 - A % de eficácia por linha, onde a primeira linha restringe a população somente ao gênero masculino e 
    a segunda linha, restringe a população ao gênero feminino.
5 - sair''' )
while True:
    a = int(input("Qual informação quer visualizar?: "))
    if a == 0:
        print(dados.Genero())
    elif a == 1:
        print(dados.Genero())
        print(dados.idades())
        print(dados.VacinaPlacebo())
        print(dados.SecontrauCovid())
    elif a == 2:
        print(dados.eficaciadaVacina())
    elif a == 3:
        print(dados.pocentagemIdades())
    elif a == 4:
        print(dados.pocengener())
    else :
        break