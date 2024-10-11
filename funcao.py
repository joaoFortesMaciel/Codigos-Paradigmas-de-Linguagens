def main():
    vetor = [0] * 8

    for i in range(8):
        vetor[i] = int(input("digite o valor da posição {}: ".format(i)))
        
    x = int(input("digite o valor de x: "))
    y = int(input("digite o valor de y: "))

    soma = vetor[x] + vetor[y]

    print("A soma dos valores x e y será: {}".format(soma))

if __name__ == "__main__":
 main()
 