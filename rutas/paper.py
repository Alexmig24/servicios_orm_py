from flask import Blueprint, request, jsonify

from modelos.paper import Paper

from repositorios.repositorio_paper import RepositorioPaper

paper_bp = Blueprint("paper", __name__, url_prefix="/paper")
repositorio = RepositorioPaper()

@paper_bp.get("/")
def obtener_todos():
    papers = repositorio.obtener_todos()
    return jsonify([paper.get_diccionario() for paper in papers])

@paper_bp.post("/")
def crear():
    datos = request.get_json()
    if not datos or not datos.get("titulo") or not datos.get("doi") or not datos.get("id_autor"): 
        return  jsonify({"mensaje":"Verificar los datos de entrada para verificar"})
    paper = Paper(
        titulo = datos["titulo"],
        doi = datos["doi"],
        id_autor = datos["id_autor"] 
    )
    repositorio.crear(paper)
    return jsonify(paper.get_diccionario), 201