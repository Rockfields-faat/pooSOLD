from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def pagar(self, pedido):
        pass

class PagamentoCartaoCredito(MetodoPagamento):
    def pagar(self, pedido):
        print(f"Pagando R$ {pedido['valor']:.2f} com cartão de crédito...")

class PagamentoBoleto(MetodoPagamento):
    def pagar(self, pedido):
        print(f"Gerando boleto no valor de R$ {pedido['valor']:.2f}...")

class PagamentoPix(MetodoPagamento):
    def pagar(self, pedido):
        print(f"Pagando R$ {pedido['valor']:.2f} via Pix...")
        print(f"Enviando notificação automática para {pedido['cliente_email']}...")  # Violação do SRP

class MetodoNotificacao(ABC):
    @abstractmethod
    def notificar(self, pedido):
        pass

class NotificacaoEmail(MetodoNotificacao):
    def notificar(self, pedido):
        print(f"Enviando e-mail de confirmação para {pedido['cliente_email']}...")

class NotificacaoSMS(MetodoNotificacao):
    def notificar(self, pedido):
        print(f"Enviando SMS de confirmação para o cliente...")

class ProcessadorDePedidos:
    def __init__(self, metodo_pagamento: MetodoPagamento, metodo_notificacao: MetodoNotificacao):
        self.metodo_pagamento = metodo_pagamento
        self.metodo_notificacao = metodo_notificacao

    def processar(self, pedido):
        print(f"Processando o pedido #{pedido['id']} no valor de R$ {pedido['valor']:.2f}...")
        self.metodo_pagamento.pagar(pedido)
        self.metodo_notificacao.notificar(pedido)
        pedido['status'] = 'concluido'
        print("Pedido concluído!")

if __name__ == "__main__":
    meu_pedido = {
        'id': 123,
        'valor': 150.75,
        'cliente_email': 'cliente@exemplo.com',
        'status': 'pendente'
    }

    processador = ProcessadorDePedidos(PagamentoCartaoCredito(), NotificacaoEmail())
    processador.processar(meu_pedido)

    print("-" * 20)

    meu_pedido_2 = meu_pedido.copy()
    meu_pedido_2['id'] = 456
    processador = ProcessadorDePedidos(PagamentoBoleto(), NotificacaoSMS())
    processador.processar(meu_pedido_2)

    print("-" * 20)

    meu_pedido_3 = meu_pedido.copy()
    meu_pedido_3['id'] = 789
    processador = ProcessadorDePedidos(PagamentoPix(), NotificacaoEmail())
    processador.processar(meu_pedido_3)
