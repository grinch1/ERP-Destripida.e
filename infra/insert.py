
def query_insert_product():
  # query to insert product
  add_product = ("""
    INSERT INTO produto
      (idProduto, codigo, descricao, situacao, unidade, preco, precoCusto, dataInclusao, 
          dataAlteracao, nomeFornecedor, marca, idFabricante, estoqueMinimo, estoqueMaximo)
      VALUES (%(id)s, %(codigo)s, %(descricao)s, %(situacao)s, %(unidade)s, %(preco)s, %(precoCusto)s, %(dataInclusao)s, 
          %(dataAlteracao)s, %(nomeFornecedor)s, %(marca)s, %(idFabricante)s, %(estoqueMinimo)s, %(estoqueMaximo)s)""")
  
  return add_product

def query_update_product():
  # query to upodate product
  update_product = ("""
  UPDATE produto 
    SET  
      codigo = %(codigo)s,
      descricao = %(descricao)s,
      situacao = %(situacao)s,
      unidade = %(unidade)s,
      preco = %(preco)s,
      precoCusto = %(precoCusto)s,
      dataInclusao = %(dataInclusao)s,
      dataAlteracao = %(dataAlteracao)s,
      nomeFornecedor = %(nomeFornecedor)s,
      marca = %(marca)s,
      idFabricante = %(idFabricante)s,
      estoqueMinimo = %(estoqueMinimo)s,
      estoqueMaximo = %(estoqueMaximo)s 
    WHERE codigo = %(idProduto)s
      """)
  
  return update_product