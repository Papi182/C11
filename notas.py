def leer_notas():
    nota = input('Introduce las notas separadas por espacios: ')
    nota = nota.split(' ')
    notaf = []
    for i in range(len(nota)):
        notaf.append(float(nota[i]))
    return notaf
def calcular_media(notaf):
    media = 0
    for i in range(len(notaf)):
        media += notaf[i]
    media /= len(notaf)
    return media
def mostrar_resumen(notaf):
    print(len(notaf))
    print(max(notaf))
    print(min(notaf))
    print(calcular_media(notaf))

if __name__ == '__main__':
    notas = leer_notas()
    mostrar_resumen(notas)