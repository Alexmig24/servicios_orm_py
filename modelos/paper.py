from modelos import db

class Paper(db.Model):
    __tablename__ = "paper"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    doi = db.Column(db.String(50))

    id_autor = db.Column(db.Integer,db.ForeignKey("autor.id"), nullable = False)
    autor = db.relationship("Autor", back_populates="paper")

    def get_diccionario(self, incluir_autor=True):
        datos = {
            "id" : self.id,
            "titulo" : self.titulo,
            "doi" : self.doi,
            "id_autor" : self.id_autor,
        }
        if incluir_autor and self.autor:
            datos["autor"] = self.autor.nombre

        return datos