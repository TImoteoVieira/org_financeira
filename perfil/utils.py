def calcula_total(colecao, campo):
    total = 0
    for obj in colecao:
        total += getattr(obj, campo)
    return total