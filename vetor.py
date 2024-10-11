def main():
    vetor = []

    for i in range(10):
        vetor.append(int(input("Digite o elemento %d: " % i)))
    maior = vetor[0]
    menor = vetor[0]

    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
        elif vetor[i] < menor:
            menor = vetor[i]

    print("O maior elemento do vetor é %d." % maior)
    print("O menor elemento do vetor é %d." % menor)
    
if __name__ == "__main__":
 main()