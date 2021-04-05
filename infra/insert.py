import json

def query_insert_product():
  # query to insert product
  add_product = ("""
    INSERT INTO produto
      (idProduto, codigo, descricao, situacao, unidade, preco, precoCusto, dataInclusao, 
      dataAlteracao, nomeFornecedor, marca, idFabricante, estoqueMinimo, estoqueMaximo, estoqueAtual)
  	VALUES
    (%(id)s, %(codigo)s, %(descricao)s, %(situacao)s, %(unidade)s, %(preco)s, 
      %(precoCusto)s, %(dataInclusao)s, %(dataAlteracao)s, %(nomeFornecedor)s, 
      %(marca)s, %(idFabricante)s, %(estoqueMinimo)s, %(estoqueMaximo)s, %(estoqueAtual)s)""")

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
      estoqueAtual = %(estoqueAtual)s 
    WHERE codigo = %(id)s""")
  
  return update_product


def query_insert_client():
  # query to insert client
  add_client = ("""
  INSERT INTO cliente
    (idCliente, nome, cpf, rg, endereco, numero, complemento,
     cidade, bairro, cep, uf, email, celular, fone)
  VALUES
  (%(id)s, %(nome)s, %(cpf)s, %(rg)s, %(endereco)s, %(numero)s, %(complemento)s, 
  %(cidade)s, %(bairro)s, %(cep)s, %(uf)s, %(email)s, %(celular)s, %(fone)s)""")
  return add_client


def query_update_client():
  # query to update client
  update_client = ("""
  UPDATE cliente
    SET
      nome = %(nome)s,
      cpf = %(cpf)s,
      rg = %(rg)s,
      endereco = %(endereco)s,
      numero = %(numero)s,
      complemento =  %(complemento)s,
      cidade = %(cidade)s,
      bairro = %(bairro)s,
      cep = %(cep)s,
      uf = %(uf)s,
      email = %(email)s,
      celular = %(celular)s,
      fone = %(fone)s
    WHERE idCliente = %(id)s
  """)
  return update_client


def query_insert_item():
  # query to insert item
  add_item = ("""
  INSERT INTO item
    (idItem, descricao, quantidade, valorunidade, idPedido, codProduto)
  VALUES
    ( %(idItem)s, %(descricao)s, %(quantidade)s, 
    %(valorunidade)s, %(idPedido)s, %(codigo)s)""")
  return add_item


def query_update_item():
  update_item = ("""
  UPDATE item
    SET
      descricao = %(descricao)s,
      quantidade = %(quantidade)s,
      valorunidade = %(valorunidade)s,
      un = %(un)s,
      idPedido = %(idPedido)s,
      idProduto = %(idProduto)s,
    WHERE idItem = %(idItem)s""")
  return update_item

def query_insert_order():
  insert_order = ("""
    INSERT INTO pedido
    (idPedido, idCliente, desconto, data, vendedor, valorfrete, 
    totalprodutos, totalvenda, situacao, dataSaida)
    VALUES
    (%(numero)s, %(idCliente)s, %(desconto)s, %(data)s, %(vendedor)s, 
    %(valorfrete)s, %(totalprodutos)s, %(totalvenda)s, %(situacao)s, %(dataSaida)s)""")
  return insert_order

def query_update_order():
  update_order = ("""
  UPDATE `destripida`.`pedido`
    SET
      idCliente = %(idCliente)s,
      desconto = %(desconto)s,
      data = %(data)s,
      vendedor = %(vendedor)s,
      valorfrete = %(valorfrete)s,
      totalprodutos = %(totalprodutos)s,
      totalvenda = %(totalvenda)s,
      situacao = %(situacao)s,
      dataSaida = %(dataSaida)s
    WHERE idPedido = %(numero)s""")
  return update_order