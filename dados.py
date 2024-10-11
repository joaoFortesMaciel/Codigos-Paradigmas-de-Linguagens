def coleta_dados():

    dados = []
    while True:
        nome = input("digete o nome(ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        idade = input("digite a idade: ")
        try:
            idade = int(idade)
        except ValueError:
            print("Idade deve ser um inteiro. Tente novamente.")
            continue

        dados.append({'nome': nome, 'idade': idade})
    return dados

def salvar_em_arquivo(dados, nome_arquivo):

    with open(nome_arquivo, 'w') as arquivo:
        for item in dados:
            linha = f"nome: {item['nome']}, Idade: {item['idade']}\n"
            arquivo.write(linha)
def main():

    dados = coleta_dados()
    if dados:
        salvar_em_arquivo(dados, 'dados_pessoas.txt')
        print("dados salvar no arquivo 'dados_pessoas.txt'.")
    else:
        print("Nenhum dado foi coletado.")

if __name__ == "__main__":
 main()
