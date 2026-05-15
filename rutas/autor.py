from flask import Blueprint, request, jsonify

from modelos.autor import Autor
from repositorios.repositorio_autor import RepositorioAutor

autor_bp = Blueprint("autor", __name__, url_prefix="/autor")
repositorio = RepositorioAutor()

@autor_bp.get("/")
def obtener_todos():
    autores = repositorio.obtener_todos()
    return jsonify([autor.get_diccionario() for autor in autores])

@autor_bp.get("/<int:id>")
def obtener_por_id(id):
    autor = repositorio.obtener_por_id(id)
    if not autor:
        return jsonify({"mensaje": "Autor no encontrado"}), 404
    return jsonify(autor.get_diccionario())

@autor_bp.post("/")
def crear():
    datos = request.get_json()
    if not datos or not datos.get("nombre") or not datos.get("pais"):
        return jsonify({"mensaje": "Verificar los datos de entrada para verificar"}), 400
    autor = Autor(
        nombre=datos["nombre"],
        pais=datos["pais"],
    )
    repositorio.crear(autor)
    return jsonify(autor.get_diccionario()), 201

@autor_bp.put("/<int:id>")
def actualizar(id):
    autor = repositorio.obtener_por_id(id)
    if not autor:
        return jsonify({"mensaje": "Autor no encontrado"}), 404
    datos = request.get_json()
    if not datos:
        return jsonify({"mensaje": "Verificar los datos de entrada para verificar"}), 400

    nombre = datos.get("nombre")
    pais = datos.get("pais")
    if nombre:
        autor.nombre = nombre
    if pais:
        autor.pais = pais
    repositorio.actualizar()
    return jsonify(autor.get_diccionario())

@autor_bp.delete("/<int:id>")
def eliminar(id):
    autor = repositorio.obtener_por_id(id)
    if not autor:
        return jsonify({"mensaje": "Autor no encontrado"}), 404
    repositorio.eliminar(autor)
    return jsonify({"mensaje": "Autor eliminado correctamente"})
