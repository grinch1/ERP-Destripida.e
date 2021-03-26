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
			records = json.load(o_file)
			o_file.close()
			# checking every order
			for order in orders:
				# checking if order was imported already
				if order['numero'] not in records or records[order['numero']] != order:
					print(f'UPDATE: {order["numero"]}\n')
					print(f'\tOLD: {diff(order, records[order["numero"]])}\n')
					print(f'\tNEW: {diff(records[order["numero"]], order)}\n')

					records[order['numero']] = order
					o_file = open("infra/imported/pedidos.json", "w")
					json.dump(records, o_file)
					o_file.close()
					# self._insert_database(table='pedido', obj=order)
			
		except ApiError as e:
			print(e.response)
		# db.close(


	def contacts(self):
		try:
			db = Database()
			print(1)
		except ApiError as e:
			print(e.response)


