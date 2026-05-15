from flask import Blueprint, request, jsonify

from modelos.autor import Autor

from repositorios.repositorio_autor import RepositorioAutor

autor_bp = Blueprint("autor", __name__, url_prefix="/autor")
repositorio = RepositorioAutor()

@autor_bp.get("/")
def obtener_todos():
    autores = repositorio.obtener_todos()
    return jsonify([autor.get_diccionario() for autor in autores])

@autor_bp.post("/")
def crear():
    datos = request.get_json()
    if not datos or not datos.get("nombre") or not datos.get("pais"): 
        return  jsonify({"mensaje":"Verificar los datos de entrada para verificar"})
    autor = Autor(
        nombre = datos["nombre"],
        pais = datos["pais"],
    )
    repositorio.crear(autor)
    return jsonify(autor.get_diccionario), 201