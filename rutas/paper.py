from flask import Blueprint, request, jsonify

from modelos.paper import Paper
from repositorios.repositorio_paper import RepositorioPaper

paper_bp = Blueprint("paper", __name__, url_prefix="/paper")
repositorio = RepositorioPaper()

@paper_bp.get("/")
def obtener_todos():
    papers = repositorio.obtener_todos()
    return jsonify([paper.get_diccionario() for paper in papers])

@paper_bp.get("/<int:id>")
def obtener_por_id(id):
    paper = repositorio.obtener_por_id(id)
    if not paper:
        return jsonify({"mensaje": "Paper no encontrado"}), 404
    return jsonify(paper.get_diccionario())

@paper_bp.post("/")
def crear():
    datos = request.get_json()
    if not datos or not datos.get("titulo") or not datos.get("doi") or not datos.get("id_autor"):
        return jsonify({"mensaje": "Verificar los datos de entrada para verificar"}), 400
    paper = Paper(
        titulo=datos["titulo"],
        doi=datos["doi"],
        id_autor=datos["id_autor"],
    )
    repositorio.crear(paper)
    return jsonify(paper.get_diccionario()), 201

@paper_bp.put("/<int:id>")
def actualizar(id):
    paper = repositorio.obtener_por_id(id)
    if not paper:
        return jsonify({"mensaje": "Paper no encontrado"}), 404
    datos = request.get_json()
    if not datos:
        return jsonify({"mensaje": "Verificar los datos de entrada para verificar"}), 400

    titulo = datos.get("titulo")
    doi = datos.get("doi")
    id_autor = datos.get("id_autor")
    if titulo:
        paper.titulo = titulo
    if doi:
        paper.doi = doi
    if id_autor:
        paper.id_autor = id_autor
    repositorio.actualizar()
    return jsonify(paper.get_diccionario())

@paper_bp.delete("/<int:id>")
def eliminar(id):
    paper = repositorio.obtener_por_id(id)
    if not paper:
        return jsonify({"mensaje": "Paper no encontrado"}), 404
    repositorio.eliminar(paper)
    return jsonify({"mensaje": "Paper eliminado correctamente"})
