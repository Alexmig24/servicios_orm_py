from modelos import db

class Autor(db.Model):
    __tablename__ = "autor"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    pais = db.Column(db.String(50))

    def get_diccionario(self):
        return {
            "id" : self.id,
            "nombre" : self.nombre,
            "pais" : self.pais,
        }