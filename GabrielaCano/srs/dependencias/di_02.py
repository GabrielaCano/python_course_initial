from abc import ABC, abstractmethod
from dependency_injector import containers, providers

class IRepositorio(ABC):
    @abstractmethod
    def guardar(self, pedido):      
        pass

class RepositorioBD(IRepositorio):
    def guardar(self, pedido):      
        print(f"Pedido {pedido} almacenado correctamente")

class ApiTercerosAdapter(IRepositorio):
    def guardar(self, pedido):
        print(f"Pedido {pedido} enviado a API de terceros correctamente")   
           
class ServicioPedidos:
    def __init__(self, repositorio: IRepositorio) -> None:
        # Inyección de dependencia via constructor 
        self.repositorio = repositorio  
    
    def crear_pedido(self, pedido: str) -> None:
        print("Notificación por mensaje")
        print("Impresión de orden")
        self.repositorio.guardar(pedido)
        print("Notificación de almacenado")

class Container(containers.DeclarativeContainer):
    repositorio = providers.Singleton(RepositorioBD)
    servicio = providers.Factory(ServicioPedidos, repositorio=repositorio)  # Corregido el nombre
    
container = Container()
servicio_instancia = container.servicio() 
servicio_instancia_dos = container.servicio() 
servicio_instancia.crear_pedido("Pedido005")
servicio_instancia_dos.crear_pedido("Pedido006")
