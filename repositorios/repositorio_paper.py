from modelos.paper import Paper

from repositorios.repositorio_base import RepositorioBase

class RepositorioPaper(RepositorioBase):
    def __init__(self):
        super().__init__(Paper)

    def buscar_por_doi(self, doi):
        return Paper.query.filter(Paper.doi.ilike(f"%{doi}%")).first()
