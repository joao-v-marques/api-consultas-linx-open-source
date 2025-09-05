from flask import Blueprint, jsonify, request
from database.connect_db import abrir_cursor
from config import require_api_key

bp_origens = Blueprint('bp_origens', __name__)

# Rota para consulta de todas as origens.
@bp_origens.route('/origens', methods=['GET'])
@require_api_key
def consulta_origens():
    try:
        cursor, conn = abrir_cursor()
        sql = "SELECT CAMPO1, CAMPO2, CAMPO3, CAMPO4 FROM SCHEMA.TABELA WHERE CAMPO5 != 'LIVRE' AND CAMPO7 = 'N'"
        cursor.execute(sql)
        retorno = cursor.dict_fetchall()

        return jsonify(retorno), 200
    except Exception as e:
        return jsonify({"erro": f"falha ao realizar consulta no banco de dados: {e}"}), 500
    finally:
        cursor.close()
        conn.close()

# Rota para consulta de uma origem especifica, com base no código.
@bp_origens.route('/origens/<int:origem>', methods=['GET'])
@require_api_key
def consulta_origem(origem):
    try:
        cursor, conn = abrir_cursor()
        sql = "SELECT CAMPO1, CAMPO2, CAMPO3, CAMPO4 FROM SCHEMA.TABELA WHERE CAMPO5 != 'LIVRE' AND CAMPO6 = 'N' AND CAMPO7 = :origem"
        cursor.execute(sql, {"origem": origem})
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

# Rota para consulta de uma origem especifica com filtros
@bp_origens.route('/origens/<int:origem>/filtros', methods=['GET'])
def consulta_origem_filtros(origem):
    empresa = request.args.get("empresa")
    revenda = request.args.get("revenda")

    try:
        cursor, conn = abrir_cursor()
        sql = "SELECT CAMPO1, CAMPO2, CAMPO3, CAMPO4 FROM SCHEMA.TABELA WHERE CAMPO5 != 'LIVRE' AND CAMPO6 = 'N' AND CAMPO7 = :origem"

        params = {"origem": origem}

        try:
            if empresa:
                sql += f" AND CAMPO8 = :empresa"
                params["empresa"] = int(empresa)
            if revenda:
                sql += f" AND CAMPO9 = :revenda"
                params["revenda"] = int(revenda)
        except ValueError:
            return jsonify({"erro": "Empresa e revenda devem ser números inteiros"}), 400

        cursor.execute(sql, params)
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