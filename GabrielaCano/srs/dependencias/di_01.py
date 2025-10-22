
"""
#Clase que almacena el pedido
class RepositorioBD:
    def guardar(self,pedido: str):
        print (f"Pedido {pedido} alamcenado exitosamente")

#Clase que implementa lógica de negocio del pedido
class ServicePedidos:
    def __init__(self, repositorio: RepositorioBD):
        self.repositorio = repositorio

    def crear_pedido(self, pedido: str):
        print("Notificación por mensaje")
        print("Impresión de orden")
        self.repositorio.guardar(pedido)
        print("Notificación de almacenamiento")

#Inyección de dependencias por constructor
repo=RepositorioBD()
service = ServicePedidos(repo)

service.crear_pedido("hamburguesita")



''' 
POR SETTER 
'''
class RepositorioBD:
    def guardar(self,pedido: str):
        print (f"Pedido {pedido} alamcenado exitosamente")

#Clase que implementa lógica de negocio del pedido
class ServicePedidos:
    def set_repo(self, repositorio:RepositorioBD):
        ''' inicializa la instancia de mi repo '''
        self.repositorio = repositorio

    def crear_pedido(self, pedido: str):
        print("Notificación por mensaje")
        print("Impresión de orden")
        self.repositorio.guardar(pedido)
        print("Notificación de almacenamiento")

#Inyección de dependencias por constructor
repo=RepositorioBD()
service = ServicePedidos()

#Llamada al setter
service.set_repo(repo)

service.crear_pedido("hamburguesita")
"""


''' 
Interfaces como patrones

'''
from abc import ABC, abstractmethod

class IRepositorioBD(ABC):
    @abstractmethod
    def guardar (self, pedido):
        pass

class RepositorioBD(IRepositorioBD):
    def guardar(self, pedido):
        print(f"Pedido {pedido} almacenado exitosamente")

class ApiTercerosAdapter(IRepositorioBD):
    def guardar (self, pedido):
        print(f"Guardado pero de forma distinta: {pedido}")

class ServicePedido:
    def __init__(self, repositorio: IRepositorioBD):
        self.repo = repositorio

    def crear_pedido(self, pedido: str):
        print("Notificación por mensaje")
        print("Impresión de orden")
        self.repo.guardar(pedido)
        print("Notificación de almacenamiento")

#repoBD: IRepositorioBD = RepositorioBD()
#repoApi: IRepositorioBD = ApiTercerosAdapter()

#service = ServicePedido(repoApi)

#service.crear_pedido("tacos")


'''
Inyección manual de dependencias

'''

class Container:
    def __init__(self):
        self._servicios = {} #diccionario

    def register(self, nombre, creator):
        self._servicios[nombre] = creator

    def resolver(self, nombre):
        return self._servicios[nombre]()

container = Container()
container.register("repositorio", lambda: ApiTercerosAdapter())
container.register("service", lambda: ServicePedido(container.resolver("repositorio")))

service = container.resolver("service")

service.crear_pedido("Taquitos")