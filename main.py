
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

def main():
    print("Calculadora de IMC")
    peso = float(input("\nDigite seu peso em kg: "))
    altura = float(input("Digite sua altura em centímetros: "))
    
    imc = calcular_IMC(peso, altura)
    classificacao = classificar_IMC(imc)
    
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

if __name__ == "__main__":
    main()

# Se o IMC for menor que 18.5 -> Abaixo do peso
#- Se o IMC for maior ou igual a 18.5 e menor que 25 -> Peso normal
#- Se o IMC for maior ou igual a 25 e menor que 30 -> Excesso de peso
#- Se o IMC for maior ou igual a 30 -> Obesidade