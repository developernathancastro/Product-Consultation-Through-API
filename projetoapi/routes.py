from projetoapi import app, jsonify, request, token, server, database
from projetoapi.conexao_banco import ConectorBancodeDados
from projetoapi.conexao_api import ConexaoAPI

conexao_api = ConexaoAPI()
@app.route("/api/produtos", methods=['GET'])
def produtos():
    token_recebido = request.args.get('token')
    resultado = conexao_api.verificar_token(token_recebido, token)
    if resultado:
        banco_de_dados = ConectorBancodeDados(driver="{SQL Server}", server=server,
                                                  database=database)
        banco_de_dados.conectar()
    else:
        return jsonify({"error": "Token inválido"}), 401

    try:
        query = """
        SELECT x.ProductKey, x.ProductName,
        x.ProductDescription,x.ProductSubcategoryKey,
        x.ColorName, x.BrandName,
        x.UnitCost, x.UnitPrice,
        x.ClassName
        FROM DimProduct as x
        """
        consulta_produtos = banco_de_dados.executar_consulta(query)
        produtos_dict = [dict(zip(['ProductKey', 'ProductName',
                                                   'ProductDescription', 'ProductSubcategoryKey',
                                                   'ColorName', 'BrandName', 'UnitCost',
                                                   'UnitPrice', 'ClassName'], row)) for row in consulta_produtos]
        return jsonify(produtos_dict)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        banco_de_dados.fechar_conexao()


@app.route("/api/produto/<nome_produto>")
def produto(nome_produto):
    token_recebido = request.args.get('token')
    resultado = conexao_api.verificar_token(token_recebido, token)
    if resultado:
        banco_de_dados = ConectorBancodeDados(driver="{SQL Server}", server=server,
                                                  database=database)
        banco_de_dados.conectar()
    else:
        return jsonify({"error": "Token inválido"}), 401

    try:
        query = f"""
        SELECT x.ProductKey, x.ProductName,
        x.ProductDescription,x.ProductSubcategoryKey,
        x.ColorName, x.BrandName,
        x.UnitCost, x.UnitPrice,
        x.ClassName
        FROM DimProduct as x
        WHERE x.ProductName = '{nome_produto.replace("'", "''")}'
        """
        consulta_produto = banco_de_dados.executar_consulta(query)

        if consulta_produto:
            produto_dict = dict(zip(['ProductKey', 'ProductName', 'ProductDescription', 'ProductSubcategoryKey',
                                 'ColorName', 'BrandName', 'UnitCost', 'UnitPrice', 'ClassName'], consulta_produto[0]))
            return jsonify(produto_dict)
        else:
            return jsonify({"message": "Produto não encontrado"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        banco_de_dados.fechar_conexao()



