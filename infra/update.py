from infra.api import Api, ApiError
from infra.apiKey import api_key
from infra.connection import Database
from infra.filters import *
from infra.insert import * 
import pandas as pd
import json
from jsondiff import diff

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
				product_id = product['id']
				product = filter_product(product)
				# checking if product was imported already
				if product_id not in records:
					records[product_id] = product

					# inserting product into database
					db.cursor.execute(query_insert_product(), product)
					# making sure data is committed to the database
					db.cnx.commit()
					print(f'INSERTED PRODUCT: {product_id}')

					p_file = open("infra/imported/produtos.json", "w")
					json.dump(records, p_file)
					p_file.close()
				# if the product was already imported but we need to update it
				elif records[product_id] != product:
						print(f'UPDATE PRODUCT: {product_id}\n')
						print(f'\tOLD: {diff(product, records[product_id])}\n')
						print(f'\tNEW: {diff(records[product_id], product)}\n')

						records[product_id] = product

						# updating product into database
						db.cursor.execute(query_update_product(), product)
						# making sure data is committed to the database
						db.cnx.commit()

						p_file = open("infra/imported/produtos.json", "w")
						json.dump(records, p_file)
						p_file.close()
			# closing database
			db.close()

		except ApiError as e:
			print(e.response)
		

	def orders(self):
		try:
			# opening database
			db = Database()
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
				client = filter_client(client)
				order.pop('cliente')
				# inserting idCliente to order 
				order['idCliente'] = int(client_id)
				# splitting itens
				itens = order['itens']
				order.pop('itens')
				
				# checking if client was imported already
				if client_id not in c_records:
					c_records[client_id] = client

					c_file = open("infra/imported/clientes.json", "w")
					json.dump(c_records, c_file)
					c_file.close()

					# inserting client into database
					db.cursor.execute(query_insert_client(), client)
					# making sure data is committed to the database
					db.cnx.commit()
					print(f'INSERTED CLIENT: {client_id}')

				elif c_records[client_id] != client:
					print(f'UPDATE CLIENT: {client_id}\n')
					print(f'\tOLD: {diff(client, c_records[client_id])}\n')
					print(f'\tNEW: {diff(c_records[client_id], client)}\n')

					c_records[client_id] = client

					# updating client on database
					db.cursor.execute(query_update_client(), client)
					# making sure data is committed to the database
					db.cnx.commit()

					c_file = open("infra/imported/clientes.json", "w")
					json.dump(c_records, c_file)
					c_file.close()

				for item in itens:
					# filtering relevant data
					item = filter_item(item['item'])
					# referencing item to order id
					cod_item = item['codigo']
					cod_item_order = f"{order_id}-{cod_item}"
					item['idPedido'] = order['numero']
					item['idItem'] = cod_item_order

					if cod_item_order not in ip_records:
						ip_records[cod_item_order] = item

						ip_file = open("infra/imported/itens_pedido.json", "w")
						json.dump(ip_records, ip_file)
						ip_file.close()

						# inserting item into database
						db.cursor.execute(query_insert_item(), item)
						# making sure data is committed to the database
						db.cnx.commit()
						print(f'INSERTED ITEM: {cod_item_order}')


					elif ip_records[cod_item_order] != item:
						print(f'UPDATE ITEM: {cod_item_order}\n')
						print(f'\tOLD: {diff(item, ip_records[cod_item_order])}\n')
						print(f'\tNEW: {diff(ip_records[cod_item_order], item)}\n')
						
						ip_records[cod_item_order] = item

						# updating item on database
						db.cursor.execute(query_update_item(), item)
						# making sure data is committed to the database
						db.cnx.commit()

						ip_file = open("infra/imported/itens_pedido.json", "w")
						json.dump(ip_records, ip_file)
						ip_file.close()


				# checking if order was imported already
				if order_id not in o_records:
					o_records[order_id] = order

					o_file = open("infra/imported/pedidos.json", "w")
					json.dump(o_records, o_file)
					o_file.close()

					# inserting order into database
					db.cursor.execute(query_insert_order(), order)
					# making sure data is committed to the database
					db.cnx.commit()
					print(f'INSERTED ORDER: {order_id}')

				elif o_records[order_id] != order:
					print(f'UPDATE ORDER: {order_id}\n')
					print(f'\tOLD: {diff(order, o_records[order_id])}\n')
					print(f'\tNEW: {diff(o_records[order_id], order)}\n')
					
					o_records[order_id] = order

					# updating order on database
					db.cursor.execute(query_update_order(), order)
					# making sure data is committed to the database
					db.cnx.commit()

					o_file = open("infra/imported/pedidos.json", "w")
					json.dump(o_records, o_file)
					o_file.close()
			# closing database
			db.close()
		except ApiError as e:
			print(e.response)


	def accounts(self):
		try:
			accounts = api.get_accounts_receivable()

			# opening file with account records
			a_file = open ("infra/imported/contas_receber.json", "r")
			records = json.load(a_file)
			a_file.close()

			for account in accounts:
				account_id = account['id']
				account = filter_account(account)
				if account == {}:
					break
				# checking if account was imported already
				if account_id not in records or records[account_id] != account:
					if account_id in records:
						print(f'UPDATE: {account_id}\n')
						print(f'\tOLD: {diff(account, records[account_id])}\n')
						print(f'\tNEW: {diff(records[account_id], account)}\n')

					records[account_id] = account
					a_file = open("infra/imported/contas_receber.json", "w")
					json.dump(records, a_file)
					a_file.close()

		except ApiError as e:
			print(e.response)
