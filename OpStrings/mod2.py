def conta_palavras(h):
    palavras = {}
    for palavra in h.split():
        if palavra in palavras:
            palavras[palavra] +=1
        else:
            palavras[palavra] = 1
    return palavras

def conta_media_palavras(h):
    palavras= conta_palavras(h)
    qntd = len(h.split())
    media = {}

    for palavra, freque in palavras.items():
     media[palavra] = freque / qntd

     return media
