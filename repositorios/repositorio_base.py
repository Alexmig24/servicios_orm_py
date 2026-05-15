from modelos import db

class RepositorioBase:
    def __init__(self, modelo):
        self.modelo = modelo

    def obtener_todos(self):
        return self.modelo.query.all()
    
    def obtener_por_id(self, id):
        return self.modelo.query.get(id)
    
    def crear(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto
    
    def actualizar(self):
        db.session.commit()
    
    def eliminar(self, objeto):
        db.session.delete(objeto)
        db.session.commit()