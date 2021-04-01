import mysql.connector  
from infra.api import Api, ApiError
from infra.apiKey import api_key
from infra.filters import *
from infra.connection import Database
import pandas as pd
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
				product_id = product['id']
				product = filter_product(product)
				# checking if product was imported already
				if product_id not in records or records[product_id] != product:
					if product_id in records:
						print(f'UPDATE: {product_id}\n')
						print(f'\tOLD: {diff(product, records[product_id])}\n')
						print(f'\tNEW: {diff(records[product_id], product)}\n')

					records[product_id] = product
					# transpose colums and rows
					
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
			c_file = open("infra/imported/clientes.json", "r")
			c_records = json.load(c_file)
			c_file.close()
			# opening file with itens records
			ip_file = open("infra/imported/itens_pedido.json", "r")
			ip_records = json.load(ip_file)
			ip_file.close()
			
			for order in orders:
				order_id = order['numero']
				# filtering relevant data
				order = filter_order(order)
				# splitting cliente
				client = order['cliente']
				client_id = client['id']
				order.pop('cliente')
				# inserting idCliente to order 
				order['idCliente'] = int(client_id)
				# splitting itens
				itens = order['itens']
				order.pop('itens')

				for item in itens:
					# filtering relevant data
					item = filter_item(item['item'])
					# referencing item to order id
					cod_item = item['codigo']
					cod_item_order = f"{order_id}-{cod_item}"
					item['idPedido'] = order['numero']

					if cod_item_order not in ip_records or ip_records[cod_item_order] != item:
						if cod_item_order in ip_records:
							print(f'UPDATE: {cod_item_order}\n')
							print(f'\tOLD: {diff(item, ip_records[cod_item_order])}\n')
							print(f'\tNEW: {diff(ip_records[cod_item_order], item)}\n')
						
						ip_records[cod_item_order] = item
						ip_file = open("infra/imported/itens_pedido.json", "w")
						json.dump(ip_records, ip_file)
						ip_file.close()
					

				# checking if order was imported already
				if order_id not in o_records or o_records[order_id] != order:
					if order_id in o_records:
						print(f'UPDATE: {order_id}\n')
						print(f'\tOLD: {diff(order, o_records[order_id])}\n')
						print(f'\tNEW: {diff(o_records[order_id], order)}\n')
					
					o_records[order_id] = order
					o_file = open("infra/imported/pedidos.json", "w")
					json.dump(o_records, o_file)
					o_file.close()
				# checking if client was imported already
				if client_id not in c_records or c_records[client_id] != client:
					if client_id in c_records:
						print(f'UPDATE: {client_id}\n')
						print(f'\tOLD: {diff(client, c_records[client_id])}\n')
						print(f'\tNEW: {diff(c_records[client_id], client)}\n')

					c_records[client_id] = client
					c_file = open("infra/imported/clientes.json", "w")
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
	
	
	
