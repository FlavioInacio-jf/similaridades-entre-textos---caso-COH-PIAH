import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]



def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    return textos



def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas



def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)



def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas



def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    Sab = 0
    for i in range(len(as_b)):
        Sab += abs(as_a[i] - as_b[i]) 
    Sab /= 6
    return Sab



def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    infectado = 0
    for i in range(len(textos)):
        assinatura = compara_assinatura(calcula_assinatura(textos[i]), ass_cp)
        if assinatura > infectado:
            infectado = i
    return infectado
        

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    tamanho_palavra = 0
    palavras = []
    frases = []
    n_caracteres_sentenca = 0
    n_caracteres_frases = 0
    n_sentencas = 0  
    for sentenca in separa_sentencas(texto):
        frase = separa_frases(sentenca)
        n_caracteres_sentenca += len(sentenca)
        n_sentencas += 1
        for f in frase:
            frases.append(f)
            n_caracteres_frases += len(f)
            palavra = separa_palavras(f)
            for p in palavra:
                tamanho_palavra += len(p)
                palavras.append(p)
                
    palavras_unicas = n_palavras_unicas(palavras)
    total_palavras_diferentes = n_palavras_diferentes(palavras)
            
    tamanhoMedioPalavras = tamanho_palavra / len(palavras)
    relacaoTypeToken = total_palavras_diferentes / len(palavras)
    razaoHapax = palavras_unicas / len(palavras)
    tam_medio_setenca = n_caracteres_sentenca / n_sentencas
    complexidade_setenca = len(frases) / n_sentencas
    
    tamanho_medio_frase = n_caracteres_frases/ len(frases)
    
    return [tamanhoMedioPalavras, relacaoTypeToken, razaoHapax, tam_medio_setenca, complexidade_setenca, tamanho_medio_frase]
