
def calcular_IMC(peso: float, altura: float) -> float:

    altura = altura / 100 
    imc = peso / (altura * altura)
    return imc

def classificar_IMC(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Excesso de peso"
    elif imc >= 30:
         return "Obesidade"
    else:
        return "Fora do peso normal"
    

def media_IMC(imc_total: float, pessoas_calculadas: int) -> float:
    if pessoas_calculadas > 0:
        return imc_total / pessoas_calculadas
    else:
        return 0.0

def classificacao_frequente(lista_classificacoes: list) -> str:
    
    return max(lista_classificacoes, key=lista_classificacoes.count)


def main():
    
    continuar = 's'
    pessoas_calculadas = 0
    imc_total = 0.0
    lista_classificacoes = [] 

    print("\nCalculadora de IMC")

    while continuar.lower() == 's': 
        
        try:

            
            peso = float(input("\nDigite seu peso em kg: "))
            altura = float(input("Digite sua altura em centímetros: "))

            if peso <= 0 or altura <= 0:
                print("\nPeso e altura devem ser maiores que zero ")
                continue

            imc = calcular_IMC(peso, altura)
            classificacao = classificar_IMC(imc)
            imc_total += imc

            print(f"Seu IMC é: {imc:.2f}")
            print(f"Classificação: {classificacao}")

            pessoas_calculadas += 1
            lista_classificacoes.append(classificacao)

            print(f"\nNº total de consultas realizadas: {pessoas_calculadas}")
            print(f"Média do IMC: {media_IMC(imc_total, pessoas_calculadas):.2f}")
            print(f"Classificação mais frequente: {classificacao_frequente(lista_classificacoes)}")

            continuar = input("\nDeseja continuar a calcular? (s/n): ")
            print('------------------------------------')
            

        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número válido para peso e altura.")

            continuar = input("Deseja tentar novamente? (s/n): ")
            print('------------------------------------')


if __name__ == "__main__":
    main()
