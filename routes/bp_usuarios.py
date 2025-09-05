from flask import Blueprint, jsonify
from database.connect_db import abrir_cursor
from config import require_api_key

bp_usuarios = Blueprint("bp_usuarios", __name__)

@bp_usuarios.route("/usuarios", methods=['GET'])
@require_api_key
def consulta_usuarios():
    try:
        cursor, conn = abrir_cursor()
        sql = "SELECT CAMPO1, CAMPO2, CAMPO3, CAMPO4, CAMPO5 FROM SCHEMA.TABELA ORDER BY CAMPO6"
        cursor.execute(sql)
        retorno = cursor.dict_fetchall()

        return jsonify(retorno), 200
    except Exception as e:
        return jsonify({"erro": f"falha ao realizar consulta no banco de dados: {e}"}), 500
    finally:
        cursor.close()
        conn.close()

@bp_usuarios.route("/usuarios/<int:id>", methods=['GET'])
@require_api_key
def consulta_usuario(id):
    try:
        cursor, conn = abrir_cursor()
        sql = "SELECT CAMPO1, CAMPO2, CAMPO3, CAMPO4, CAMPO5 FROM SCHEMA.TABELA WHERE CAMPO6 = :id"
        cursor.execute(sql, {"id": id})
        retorno = cursor.dict_fetchall()

        # Caso não tenha retorno resulta em 404
        if not retorno:
            return jsonify({"erro": "Nenhum registro encontrado"}), 404

        return jsonify(retorno), 200
    except Exception as e:
        return jsonify({"erro": f"falha ao realizar consulta no banco de dados: {e}"}), 500
    finally:
        cursor.close()
        conn.close()

