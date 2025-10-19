from abc import ABC, abstractmethod

class IDAO(ABC):
    """Interfaz para Data Access Objects"""
    
    @abstractmethod
    def agregar(self, obj):
        """Agrega un objeto a la base de datos"""
        pass
    
    @abstractmethod
    def obtener(self, id):
        """Obtiene un objeto por su identificador"""
        pass
    
    @abstractmethod
    def actualizar(self, obj):
        """Actualiza un objeto existente"""
        pass
    
    @abstractmethod
    def eliminar(self, id):
        """Elimina un objeto de la base de datos"""
        pass
    
    @abstractmethod
    def listar_todos(self):
        """Lista todos los objetos"""
        pass
