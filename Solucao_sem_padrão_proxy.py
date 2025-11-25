# Exemplo SEM Proxy

class Estacionamento:
    def __init__(self, valor_hora=10.0):
        self.valor_hora = valor_hora

    def calcular_valor(self, horas, tipo_cliente):
        valor = self.valor_hora * horas

        # Qualquer um que falar que é VIP ganha desconto (inseguro)
        if tipo_cliente == "VIP":
            print("Aplicando desconto de 50% para cliente 'VIP' (sem verificação!)")
            valor *= 0.5

        return valor


if __name__ == "__main__":
    estacionamento = Estacionamento()

    horas = 3

    print("=== Pagamento SEM Proxy ===")
    # Cliente comum fingindo ser VIP
    tipo_cliente = "VIP"
    valor = estacionamento.calcular_valor(horas, tipo_cliente)
    print(f"Cliente informou tipo '{tipo_cliente}'. Valor a pagar: R$ {valor:.2f}")
