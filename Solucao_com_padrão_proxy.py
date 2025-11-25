# Exemplo COM Proxy (Proxy de Proteção)

class Estacionamento:
    def __init__(self, valor_hora=10.0):
        self.valor_hora = valor_hora

    def calcular_valor(self, horas, eh_vip: bool):
        valor = self.valor_hora * horas

        if eh_vip:
            print("Estacionamento: Aplicando desconto de 50% para cliente VIP.")
            valor *= 0.5

        return valor


class ProxyEstacionamento:
    def __init__(self, estacionamento_real: Estacionamento):
        self.estacionamento_real = estacionamento_real
        # Lista de placas realmente VIP (exemplo)
        self.placas_vip = {"ABC1234", "XYZ9999"}

    def pagar(self, placa: str, horas: int):
        print("\n[Proxy] Recebendo solicitação de pagamento...")
        eh_vip = self._verificar_se_eh_vip(placa)

        if eh_vip:
            print(f"[Proxy] Placa {placa} é VIP. Desconto autorizado.")
        else:
            print(f"[Proxy] Placa {placa} NÃO é VIP. Sem desconto.")

        valor = self.estacionamento_real.calcular_valor(horas, eh_vip)
        print(f"[Proxy] Pagamento concluído. Valor final: R$ {valor:.2f}")
        return valor

    def _verificar_se_eh_vip(self, placa: str) -> bool:
        # Aqui poderia buscar em banco de dados, API, etc.
        return placa.upper() in self.placas_vip


if __name__ == "__main__":
    estacionamento_real = Estacionamento()
    proxy = ProxyEstacionamento(estacionamento_real)

    print("=== Pagamento COM Proxy ===")

    # Tentativa 1: placa que não é VIP
    proxy.pagar("JKL5678", horas=3)

    # Tentativa 2: placa VIP
    proxy.pagar("ABC1234", horas=3)

# O que mudou com o Proxy?
# O cliente não acessa diretamente o Estacionamento.
#Ele passa por ProxyEstacionamento, que:
#verifica se a placa está cadastrada como VIP;
#decide se manda eh_vip=True ou False para o estacionamento real.
#Isso é exatamente a ideia do Proxy de Proteção:
#um objeto intermediário que controla o acesso a um recurso sensível (no caso, o desconto).