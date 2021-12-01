import dados
#Exercio para ler dados da eficacia da vacina contra o covida
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
    #menu para navegar entre os topicos sugeridos
    a = int(input("Qual informação quer visualizar?: "))
    if a == 0:
    #mosta a pocentagem dos generos na pesquisa
        print(dados.Genero())
    elif a == 1:
    #Dados de todos os participantes definidos por pocentagem
        print(dados.Genero())
        print(dados.idades())
        print(dados.VacinaPlacebo())
        print(dados.SecontrauCovid())
    elif a == 2:
    #Dados da eficacia da vacina
        print(dados.eficaciadaVacina())
    elif a == 3:
    #dados da eficacia da vacina por idade
        print(dados.pocentagemIdades())
    elif a == 4:
    #dados da eficacia da vacina por genero
        print(dados.pocengener())
    else :
        break