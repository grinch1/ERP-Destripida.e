import mysql.connector  
from infra.api import Api, ApiError
from infra.apiKey import api_key
from infra.connection import Database
# import pandas as pd
import json

api = Api(api_key)
class Import():
	
	def products(self):
		try:
			# opening database
			db = Database()
			# getting products from api
			products = api.get_products()
			# opening file with products records
			p_file = open("infra/imported/produtos.json", "r")
			records = json.load(p_file)
			p_file.close()
			# checking every product
			for product in products:
				# checking if product was imported already
				if records[product['id']] != product or not records[product['id']]:
					print(f'Updated: {product["codigo"]}')
					records[product['id']] = product
					p_file = open("infra/imported/produtos.json", "w")
					json.dump(records, p_file)
					p_file.close()
					# self._insert_database(table='produto', obj=product)
				
		except ApiError as e:
			print(e.response)
		db.close()
		
	def orders(self):
		try:
			db = Database()
			orders = api.get_orders()
			df = pd.DataFrame(orders)


			desc = df.pop("desconto")
			desc.to_json('desconto.json')

			data = df.pop("data")
			data.to_json('data.json')

			nume = df.pop("numero")
			nume.to_json('numero.json')

			nocp = df.pop("numeroOrdemCompra")
			nocp.to_json('nocp.json')

			vndr = df.pop('vendedor')
			vndr.to_json('vendedor.json')

			vlfr = df.pop("valorfrete")
			vlfr.to_json('valfrete.json')

			situ = df.pop('situacao')
			situ.to_json('situ.json')

			dtsd = df.pop('dataSaida')
			dtsd.to_json('DTsaida.json')

			loja = df.pop('loja')
			loja.to_json('loja.json')

			clnt = df.pop("cliente")
			clnt.to_json('cliente.json')

			pgmt = df.pop('pagamento')
			pgmt.to_json('pagamento.json')

			itns = df.pop("itens")
			itns.to_json('itens.json')

			pcls = df.pop('parcelas')
			pcls.to_json('parcelas.json')



			# dfa = df.pd.DataFrame.colums("desconto","data","numero","numeroOrdemCompra","vendedor","valorfrete","situacao","dataSaida","loja","cliente","pagamento","itens","parcelas","dataPrevista")
			print(desc)
			# cli.to_sql('cliente', db.encnx, index = False , schema = 'destripida', if_exists = 'append')

			# df.to_json('orders.json')

			# df_par = df.drop(labels= 'parcelas',axis = 1, inplace=True)
			# df.drop(labels= 'observacoes',axis = 1, inplace=True)
			# df.drop(labels= 'observacaointerna',axis = 1, inplace=True)
			# df.drop(labels= 'dataPrevista',axis = 1, inplace=True)
			# df_pag = df.drop(labels= 'pagamento',axis = 1, inplace=True)
			# df.drop(labels= 'numeroOrdemCompra',axis = 1, inplace=True)

			


			# print(df.itens)
			

			# print(df_par)

			# for o in orders:
			# 	f = o.pop('cliente')
			# 	i = o.pop ('itens')
			# 	m = o.pop 

			# 	j = o.pop('forma_pagamento')
			# 	print(o)
			# 	df = pd.DataFrame(o)
			# 	o.to_csv('pedido.csv', index=True)
			# 	dff =pd.DataFrame(j)
			# 	dff.to_csv('forma_pagamento.csv', index=False)
			# 	df0 = pd.DataFrame(f)
			# 	print(df0)
			# 	df0.to_csv('clientes.csv', index=True)
			# 	df1 = pd.DataFrame(i)
			# 	df1.to_csv('ítens.csv', index=False)S
				
			# 	print(df)
			# 	print(o)
			
			# 	df.to_sql('itens', db.encnx, index = False , schema = 'destripida', if_exists = 'append')
			# 	df1.to_sql('parcelas', db.encnx, index = False , schema = 'destripida', if_exists = 'append')
			
		except ApiError as e:
			print(e.response)

	def contacts(self):
		try:
			db = Database()
			print(1)
		except ApiError as e:
			print(e.response)


