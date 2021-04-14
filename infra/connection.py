from infra.config import config, url
import mysql.connector
from mysql.connector.cursor import MySQLCursor
from mysql.connector import errorcode
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

class Database():

  def __init__(self):
    self.connect()
    # self.raw_connect()
    # self.connect_engine()
    self.cursor = self.cnx.cursor()

  def connect(self):
    try:
      self.cnx = mysql.connector.connect(**config)
      print("Connection succefully established")
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)

  def connect_engine(self):
    try:
      self.encnx = create_engine(url)
      print("Engine succefully generated")
    except SQLAlchemyError as err:
      error = str(err._dict_['orig'])
      return error

  def raw_connect(self):
    try:
      self.raw_cnx = mysql.connector.connect(**config, raw=True)
      print("Raw_Connection succefully established")
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
  
  def insert_product(self, product):
    try:
      add_product = ("""
        INSERT INTO produto
          (idProduto, codigo, descricao, situacao, unidade, preco, precoCusto, dataInclusao, 
          dataAlteracao, nomeFornecedor, marca, idFabricante, estoqueMinimo, estoqueMaximo, estoqueAtual)
        VALUES
        (%(id)s, %(codigo)s, %(descricao)s, %(situacao)s, %(unidade)s, %(preco)s, 
          %(precoCusto)s, %(dataInclusao)s, %(dataAlteracao)s, %(nomeFornecedor)s, 
          %(marca)s, %(idFabricante)s, %(estoqueMinimo)s, %(estoqueMaximo)s, %(estoqueAtual)s)""")
      
      self.cursor.execute(add_product, product)
      self.cnx.commit()
      print(f'INSERTED PRODUCT: {product["id"]}')
    except mysql.connector.Error as err:
      if err.errno == 1062:
        print(err.msg)


  def update_product(self, product):
    try:
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
            estoqueMaximo = %(estoqueMaximo)s,
            estoqueAtual = %(estoqueAtual)s 
          WHERE codigo = %(id)s""")
      self.cursor.execute(update_product, product)
      self.cnx.commit()
    except mysql.connector.Error as err:
      print(err)


  def insert_client(self, client):
    try:
      add_client = ("""
        INSERT INTO cliente
          (idCliente, nome, cpf, rg, endereco, numero, complemento,
          cidade, bairro, cep, uf, email, celular, fone)
        VALUES
        (%(id)s, %(nome)s, %(cpf)s, %(rg)s, %(endereco)s, %(numero)s, %(complemento)s, 
        %(cidade)s, %(bairro)s, %(cep)s, %(uf)s, %(email)s, %(celular)s, %(fone)s)""")
      
      self.cursor.execute(add_client, client)
      self.cnx.commit()
      print(f'INSERTED CLIENT: {client["id"]}')
    except mysql.connector.Error as err:
      if err.errno == 1062:
        print(err.msg)


  def update_client(self, client):
    try:
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
      self.cursor.execute(update_client, client)
      self.cnx.commit()
    except mysql.connector.Error as err:
      print(err)


  def insert_item(self, item):
    try:
      add_item = ("""
        INSERT INTO item
          (idItem, descricao, quantidade, valorunidade, idPedido, codProduto)
        VALUES
          ( %(idItem)s, %(descricao)s, %(quantidade)s, 
          %(valorunidade)s, %(idPedido)s, %(codigo)s)""")
      
      self.cursor.execute(add_item, item)
      self.cnx.commit()
      print(f'INSERTED ITEM: {item["idItem"]}')
    except mysql.connector.Error as err:
      if err.errno == 1062:
        print(err.msg)


  def update_item(self, item):
    try:
      update_item = ("""
        UPDATE item
          SET
            codProduto = %(codigo)s,
            descricao = %(descricao)s,
            quantidade = %(quantidade)s,
            valorunidade = %(valorunidade)s,
            idPedido = %(idPedido)s,
          WHERE idItem = %(idItem)s""")
      self.cursor.execute(update_item, item)
      self.cnx.commit()
    except mysql.connector.Error as err:
      print(err)


  def insert_order(self, order):
    try:
      add_order = ("""
        INSERT INTO pedido
        (idPedido, idCliente, desconto, data, vendedor, valorfrete, 
        totalprodutos, totalvenda, situacao, dataSaida)
        VALUES
        (%(numero)s, %(idCliente)s, %(desconto)s, %(data)s, %(vendedor)s, 
        %(valorfrete)s, %(totalprodutos)s, %(totalvenda)s, %(situacao)s, %(dataSaida)s)""")
      
      self.cursor.execute(add_order, order)
      self.cnx.commit()
      print(f'INSERTED ORDER: {order["numero"]}')
    except mysql.connector.Error as err:
      if err.errno == 1062:
        print(err.msg)


  def update_order(self, order):
    try:
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
      self.cursor.execute(update_order, order)
      self.cnx.commit()
    except mysql.connector.Error as err:
      print(err)

  def close(self):
    self.cnx.close()
    # self.raw_cnx.close() 
    self.cursor.close()