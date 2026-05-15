from modelos.autor import Autor

from repositorios.repositorio_base import RepositorioBase

class RepositorioAutor(RepositorioBase):
    def __init__(self):
        super().__init__(Autor)
    
    def buscar_por_nombre(self, nombre):
        return Autor.query.filter(Autor.nombre.ilike(f"%{nombre}%")).first()