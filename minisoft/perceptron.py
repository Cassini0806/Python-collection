import random 

weight = random.uniform(-1, 1)
bias = random.uniform(-1, 1)

def gera_numeros():
    """
    Gera o conjunto de dados de treinamento do perceptron.
 
    Cria 5000 exemplos positivos (números de 0.1 a 500.0, rotulados como True)
    e 5000 exemplos negativos (números de -500.0 a -0.1, rotulados como False),
    depois embaralha a ordem dos exemplos.
 
    Retorna:
        list[tuple[float, bool]]: lista de pares (valor, rotulo), embaralhada.
    """
    # positive numbers are True, negative numbers are False 
    data  = [(i * 0.1, True)  for i in range(1, 5001)]
    data += [(i * 0.1, False) for i in range(-5000, 0)]
    random.shuffle(data)
    return data

def treinar():
    """
    Treina o perceptron ajustando 'weight' e 'bias' globais.
 
    Usa a regra de aprendizado do perceptron: para cada exemplo do dataset,
    calcula a previsão atual, compara com o rótulo esperado e, se estiver
    errada, corrige weight e bias proporcionalmente ao erro e à taxa de
    aprendizado (learning_rate), repetindo por EPOCHS épocas.
 
    Não recebe parâmetros nem retorna valor; o efeito é a atualização das
    variáveis globais 'weight' e 'bias'.
    """
    global weight, bias
    dados = gera_numeros()
    learning_rate = 0.1
    EPOCHS = 1000
    for epoch in range(EPOCHS):
        for value, result in dados:
            prediction = (weight * value + bias) > 0
            if prediction != result:
                error = result - prediction          # +1 or -1
                weight += learning_rate * error * value
                bias   += learning_rate * error
        
def perceptron(num):
    """
    Aplica o perceptron treinado a um número e retorna a previsão.
 
    Args:
        num (float): valor de entrada a ser classificado.
 
    Retorna:
        bool: True se o valor for classificado como positivo, False caso
        contrário, de acordo com a fronteira de decisão weight * num + bias > 0.
    """

    prediction = (weight * num + bias) > 0
    return prediction

if __name__ == '__main__':
    treinar()
    decision_boundary = -bias / weight
    print(weight, bias)
    print(decision_boundary)
    num = int(input(">"))
    print(perceptron(num))

