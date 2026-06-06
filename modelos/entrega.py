from interfaces.calculo_frete_interface import CalculoFreteInterface

class Entrega(CalculoFreteInterface):
    def calcular_frete(self):
        pass
    
class EntregaComum(Entrega):
    def calcular_frete(self, distancia):
        return distancia * 1.5
    
class EntregaExpressa(Entrega):
    def calcular_frete(self, distancia):
        return distancia * 3
    
class EntregaPremium(Entrega):
    def calcular_frete(self, distancia):
        return distancia * 5 + 20