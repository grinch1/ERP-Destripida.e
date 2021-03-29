import mysql.connector  
from infra.api import Api, ApiError
from infra.apiKey import api_key
from infra.connection import Database
# import pandas as pd
import json
from jsondiff import diff

api = Api(api_key)
class Import():
	
	def products(self):
		try:
			# opening database
			# db = Database()
			# getting products from api
			products = api.get_products()
			# opening file with products records
			p_file = open("infra/imported/produtos.json", "r")
			records = json.load(p_file)
			p_file.close()
			# checking every product
			for product in products:
				# checking if product was imported already
				if product['id'] not in records or records[product['id']] != product:
					if product['id'] in records:
						print(f'UPDATE: {product["id"]}\n')
						print(f'\tOLD: {diff(product, records[product["id"]])}\n')
						print(f'\tNEW: {diff(records[product["id"]], product)}\n')

					records[product['id']] = product
					p_file = open("infra/imported/produtos.json", "w")
					json.dump(records, p_file)
					p_file.close()

				
					# self._insert_database(table='produto', obj=product)
				
		except ApiError as e:
			print(e.response)
		# db.close()
		

	def orders(self):
		try:
			# db = Database()
			orders = api.get_orders()
			# opening file with order records
			o_file = open("infra/imported/pedidos.json", "r")
			o_records = json.load(o_file)
			o_file.close()
			# opening file with client records
			c_file = open("infra/imported/cliente.json", "r")
			c_records = json.load(c_file)
			c_file.close()
			
			for order in orders:
				# splitting cliente
				client = order['cliente']
				order.pop('cliente')
				# insert idCliente to order 
				order['idCliente'] = client['id']

				# checking if order was imported already
				if order['numero'] not in o_records or o_records[order['numero']] != order:
					if order['numero'] in o_records:
						print(f'UPDATE: {order["numero"]}\n')
						print(f'\tOLD: {diff(order, o_records[order["numero"]])}\n')
						print(f'\tNEW: {diff(o_records[order["numero"]], order)}\n')
					
					o_records[order['numero']] = order
					o_file = open("infra/imported/pedidos.json", "w")
					json.dump(o_records, o_file)
					o_file.close()
				# checking if client was imported already
				if client['id'] not in c_records or c_records[client['id']] != client:
					print(client)
					if client['id'] in c_records:
						print(f'UPDATE: {client["id"]}\n')
						print(f'\tOLD: {diff(client, c_records[client["id"]])}\n')
						print(f'\tNEW: {diff(c_records[client["id"]], client)}\n')

					c_records[client['id']] = client
					c_file = open("infra/imported/cliente.json", "w")
					json.dump(c_records, c_file)
					c_file.close()
					# self._insert_database(table='pedido', obj=order)

		except ApiError as e:
			print(e.response)
		# db.close(


	def receivable(self):
		try:
			#db = Database()
			accounts_r = api.get_accounts_receivable()

			# opening file with account_r records
			tr_file = open ("infra/imported/contas_receber.json", "r")
			records = json.load(tr_file)
			tr_file.close()
			for account_r in accounts_r:
				# checking if account_r was imported already
				if account_r['id'] not in records or records[account_r['id']] != account_r:
					if account_r['id'] in records:
						print(f'UPDATE: {account_r["id"]}\n')
						print(f'\tOLD: {diff(account_r, records[account_r["id"]])}\n')
						print(f'\tNEW: {diff(records[account_r["id"]], account_r)}\n')

					records[account_r['id']] = account_r
					o_file = open("infra/imported/contas_receber.json", "w")
					json.dump(records, o_file)
					o_file.close()
			 # checking every account_r

		except ApiError as e:
			print(e.response)
	
	
	