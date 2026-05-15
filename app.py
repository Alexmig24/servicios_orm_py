from flask import Flask
from config.configuracion import Configuracion

from modelos.autor import Autor 
from modelos.paper import Paper

from rutas.autor import autor_bp
from rutas.paper import paper_bp

from modelos import db

def iniciar_app(configuracion=Configuracion):
    app = Flask(__name__)
    app.config.from_object(Configuracion)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    app.register_blueprint(autor_bp)
    app.register_blueprint(paper_bp)
    return app
    

if __name__=="__main__":
    app=iniciar_app()
    app.run(debug=True, port=5000)
