
def calcular_IMC(peso: float, altura: float) -> float:
    altura = altura / 100 
    imc = peso / (altura * altura)
    return imc

def classificar_IMC(imc: float) -> str:
    if imc < 18.5:
        return "Fora do peso normal"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif imc >= 25:
        return "Fora do peso normal"
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